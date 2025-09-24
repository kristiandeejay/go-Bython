def factorial(n) {
    if n <= 1 {
        return 1;
    }
    return n * factorial(n - 1);
}

def is_prime(n) {
    if n <= 1 {
        return False;
    }
    if n <= 3 {
        return True;
    }
    if n % 2 == 0 or n % 3 == 0 {
        return False;
    }

    i = 5;
    while i * i <= n {
        if n % i == 0 or n % (i + 2) == 0 {
            return False;
        }
        i += 6;
    }
    return True;
}

def gcd(a, b) {
    while b != 0 {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

def lcm(a, b) {
    return abs(a * b) // gcd(a, b);
}

if __name__ == "__main__" {
    print("Factorials:");
    for i in range(1, 11) {
        print(f"{i}! = {factorial(i)}");
    }

    print("\nPrime numbers up to 50:");
    primes = [];
    for i in range(2, 51) {
        if is_prime(i) {
            primes.append(i);
        }
    }
    print(primes);

    print(f"\nGCD(48, 18) = {gcd(48, 18)}");
    print(f"LCM(12, 15) = {lcm(12, 15)}");
}