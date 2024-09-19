import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            # Prompt the user to enter their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")

        except ValueError:
            print("Please enter a valid integer.")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
