# this is my python script
# notebooks are good for experimentation, but production work _often_ moves core logic to a script.

# below is a silly example to show you how our analytical work can be packages as programs for deployment

import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low, try again.")
            elif guess > number_to_guess:
                print("Too high, try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
