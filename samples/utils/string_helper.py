def reverse_string(s) {
    return s[::-1];
}

def is_palindrome(s) {
    cleaned = s.lower().replace(" ", "");
    return cleaned == cleaned[::-1];
}

def count_vowels(s) {
    vowels = "aeiouAEIOU";
    count = 0;
    for char in s {
        if char in vowels {
            count += 1;
        }
    }
    return count;
}

def title_case(s) {
    words = s.split();
    result = [];
    for word in words {
        if len(word) > 0 {
            result.append(word[0].upper() + word[1:].lower());
        }
    }
    return " ".join(result);
}

if __name__ == "__main__" {
    test_string = "hello world";

    print(f"Original: {test_string}");
    print(f"Reversed: {reverse_string(test_string)}");
    print(f"Is palindrome: {is_palindrome(test_string)}");
    print(f"Vowel count: {count_vowels(test_string)}");
    print(f"Title case: {title_case(test_string)}");

    palindrome_test = "race car";
    print(f"\n'{palindrome_test}' is palindrome: {is_palindrome(palindrome_test)}");
}