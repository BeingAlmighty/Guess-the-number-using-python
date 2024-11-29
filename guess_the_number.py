import random
import math
import time

def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return 10 
        elif choice == '2':
            return 50 
        elif choice == '3':
            return 100
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def play_game():
    max_range = choose_difficulty()

    number = random.randint(1, max_range)

    if max_range == 10:
        attempts = 5
    elif max_range == 50:
        attempts = 7
    else:
        attempts = 10
    
    start_time = time.time()

    print(f"\nI have selected a number between 1 and {max_range}. Try to guess it!")
    print(f"You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            print(f"Congratulations! You guessed the number {number} in {attempt} attempts.")
            print(f"Time taken: {time_taken} seconds.")
            return

    print(f"Sorry, you've run out of attempts. The correct number was {number}.")

def main():
    print("Welcome to the Advanced Number Guessing Game!")
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
