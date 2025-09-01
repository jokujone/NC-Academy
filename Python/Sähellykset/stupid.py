import random

def guess_the_number():
 
    number = random.randint(1, 10000)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10000: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    print("Can you guess the correct number between 1 and 10000?\n")
    while True:
        guess_the_number()
        print("Starting a new game...\n")