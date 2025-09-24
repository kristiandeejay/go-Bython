class Calculator {
    def __init__(self, initial_value) {
        self.value = initial_value;
    }

    def add(self, x) {
        self.value += x;
        return self.value;
    }

    def subtract(self, x) {
        self.value -= x;
        return self.value;
    }

    def multiply(self, x) {
        self.value *= x;
        return self.value;
    }

    def divide(self, x) {
        if x == 0 {
            raise ValueError("Cannot divide by zero");
        }
        self.value /= x;
        return self.value;
    }
}

if __name__ == "__main__" {
    calc = Calculator(100);
    print(f"Initial: {calc.value}");
    print(f"Add 50: {calc.add(50)}");
    print(f"Multiply by 2: {calc.multiply(2)}");
    print(f"Subtract 100: {calc.subtract(100)}");
    print(f"Divide by 2: {calc.divide(2)}");
}