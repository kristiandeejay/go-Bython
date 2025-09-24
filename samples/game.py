import random;

class GuessTheNumber {
    def __init__(self, min_num=1, max_num=100) {
        self.min_num = min_num;
        self.max_num = max_num;
        self.secret_number = random.randint(min_num, max_num);
        self.attempts = 0;
    }

    def guess(self, number) {
        self.attempts += 1;

        if number < self.secret_number {
            return "Too low!";
        } elif number > self.secret_number {
            return "Too high!";
        } else {
            return f"Correct! You got it in {self.attempts} attempts!";
        }
    }

    def reset(self) {
        self.secret_number = random.randint(self.min_num, self.max_num);
        self.attempts = 0;
    }
}

def play_game() {
    game = GuessTheNumber(1, 100);
    print("Welcome to Guess the Number!");
    print("I'm thinking of a number between 1 and 100.");

    while True {
        try {
            guess = int(input("Enter your guess: "));
            result = game.guess(guess);
            print(result);

            if "Correct!" in result {
                play_again = input("Play again? (y/n): ");
                if play_again.lower() == 'y' {
                    game.reset();
                    print("\nNew game started!");
                } else {
                    print("Thanks for playing!");
                    break;
                }
            }
        } except ValueError {
            print("Please enter a valid number!");
        }
    }
}

if __name__ == "__main__" {
    play_game();
}