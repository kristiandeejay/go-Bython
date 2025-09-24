package processor

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

type PythonPreprocessor struct {
	indentSize  int
	indentChar  string
	indentLevel int
}

func NewPythonPreprocessor(indentSize int) *PythonPreprocessor {
	return &PythonPreprocessor{
		indentSize:  indentSize,
		indentChar:  strings.Repeat(" ", indentSize),
		indentLevel: 0,
	}
}

var controlKeywords = []string{
	"if ", "elif ", "else", "while ", "for ", "def ", "class ", "try", "except", "finally", "with ",
}

func (p *PythonPreprocessor) processLine(line string) []string {
	trimmed := strings.TrimSpace(line)
	if trimmed == "" {
		return []string{""}
	}

	if strings.HasPrefix(trimmed, "#") {
		return []string{p.indent() + trimmed}
	}

	if strings.HasPrefix(trimmed, "}") {
		p.indentLevel--
		remaining := strings.TrimSpace(trimmed[1:])

		if strings.HasPrefix(remaining, "else") || strings.HasPrefix(remaining, "elif") {
			return p.processLine(remaining)
		} else if remaining != "" {
			return p.processLine(remaining)
		}
		return []string{}
	}

	needsColon := false
	openBraceIndex := p.findStructuralBrace(trimmed)

	if openBraceIndex != -1 {
		beforeBrace := strings.TrimSpace(trimmed[:openBraceIndex])
		afterBrace := strings.TrimSpace(trimmed[openBraceIndex+1:])

		if p.isControlStatement(beforeBrace) {
			needsColon = true
		}

		processedLine := beforeBrace
		if needsColon && !strings.HasSuffix(processedLine, ":") {
			processedLine += ":"
		}

		result := []string{p.indent() + processedLine}

		p.indentLevel++

		if afterBrace != "" && afterBrace != "}" {
			if strings.HasSuffix(afterBrace, "}") {
				content := strings.TrimSpace(afterBrace[:len(afterBrace)-1])
				if content != "" {
					content = strings.TrimSuffix(content, ";")
					result = append(result, p.indent()+content)
				}
				p.indentLevel--
			} else {
				afterBrace = strings.TrimSuffix(afterBrace, ";")
				result = append(result, p.indent()+afterBrace)
			}
		}

		return result
	}

	processedLine := trimmed
	processedLine = strings.TrimSuffix(processedLine, ";")

	return []string{p.indent() + processedLine}
}

func (p *PythonPreprocessor) isControlStatement(line string) bool {
	for _, keyword := range controlKeywords {
		if strings.HasPrefix(line, keyword) || line == strings.TrimSpace(keyword) {
			return true
		}
	}

	if strings.Contains(line, "__main__") {
		return true
	}

	return false
}

func (p *PythonPreprocessor) indent() string {
	return strings.Repeat(p.indentChar, p.indentLevel)
}

func (p *PythonPreprocessor) findStructuralBrace(line string) int {
	inString := false
	stringChar := rune(0)

	for i, ch := range line {
		if (ch == '"' || ch == '\'') && (i == 0 || line[i-1] != '\\') {
			if !inString {
				inString = true
				stringChar = ch
			} else if ch == stringChar {
				inString = false
				stringChar = 0
			}
		}
		if ch == '{' && !inString {
			return i
		}
	}
	return -1
}

func (p *PythonPreprocessor) ProcessReader(reader io.Reader, writer io.Writer) error {
	scanner := bufio.NewScanner(reader)
	first := true

	for scanner.Scan() {
		lines := p.processLine(scanner.Text())
		for _, line := range lines {
			if line != "" || !first {
				_, err := fmt.Fprintln(writer, line)
				if err != nil {
					return err
				}
			}
			first = false
		}
	}

	return scanner.Err()
}

func (p *PythonPreprocessor) ProcessFile(inputPath, outputPath string) error {
	p.indentLevel = 0

	inputFile, err := os.Open(inputPath)
	if err != nil {
		return fmt.Errorf("error opening input file: %v", err)
	}
	defer func() { _ = inputFile.Close() }()

	outputFile, err := os.Create(outputPath)
	if err != nil {
		return fmt.Errorf("error creating output file: %v", err)
	}
	defer func() { _ = outputFile.Close() }()

	return p.ProcessReader(inputFile, outputFile)
}

func (p *PythonPreprocessor) ProcessString(input string) string {
	reader := strings.NewReader(input)
	var builder strings.Builder
	_ = p.ProcessReader(reader, &builder)
	return builder.String()
}
