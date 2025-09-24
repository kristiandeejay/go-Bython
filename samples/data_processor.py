class DataProcessor {
    def __init__(self, data) {
        self.data = data;
    }

    def filter_positive(self) {
        result = [];
        for item in self.data {
            if item > 0 {
                result.append(item);
            }
        }
        return result;
    }

    def filter_negative(self) {
        result = [];
        for item in self.data {
            if item < 0 {
                result.append(item);
            }
        }
        return result;
    }

    def sum_all(self) {
        total = 0;
        for item in self.data {
            total += item;
        }
        return total;
    }

    def average(self) {
        if len(self.data) == 0 {
            return 0;
        }
        return self.sum_all() / len(self.data);
    }
}

def process_file(filename) {
    try {
        with open(filename, 'r') as f {
            content = f.read();
            return content;
        }
    } except FileNotFoundError {
        print(f"File {filename} not found");
        return None;
    } except Exception as e {
        print(f"Error reading file: {e}");
        return None;
    }
}

if __name__ == "__main__" {
    numbers = [10, -5, 20, -15, 30, 0, -8, 45];
    processor = DataProcessor(numbers);

    print(f"Original data: {numbers}");
    print(f"Positive numbers: {processor.filter_positive()}");
    print(f"Negative numbers: {processor.filter_negative()}");
    print(f"Sum: {processor.sum_all()}");
    print(f"Average: {processor.average()}");
}