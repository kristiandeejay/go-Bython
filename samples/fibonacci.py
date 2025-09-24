def fibonacci(n) {
    if n <= 0 {
        return 0;
    } elif n == 1 {
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

def fibonacci_iterative(n) {
    if n <= 0 {
        return 0;
    } elif n == 1 {
        return 1;
    }

    a = 0;
    b = 1;

    for i in range(2, n + 1) {
        temp = a + b;
        a = b;
        b = temp;
    }

    return b;
}

if __name__ == "__main__" {
    print("Fibonacci sequence (recursive):");
    for i in range(15) {
        print(f"fib({i}) = {fibonacci(i)}");
    }

    print("\nFibonacci sequence (iterative):");
    for i in range(15) {
        print(f"fib({i}) = {fibonacci_iterative(i)}");
    }
}