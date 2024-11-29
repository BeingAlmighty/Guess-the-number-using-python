import random
import time


def choose_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy (Number between 1 and 100, 30 seconds to guess)")
    print("2. Medium (Number between 1 and 500, 40 seconds to guess)")
    print("3. Hard (Number between 1 and 10000, 60 seconds to guess)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return 100, 30
        elif choice == '2':
            return 500, 40
        elif choice == '3':
            return 10000, 60
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def play_game():
    max_range, timer_duration = choose_difficulty()
    number = random.randint(1, max_range)
    start_time = time.time()

    print(f"\nYou have {timer_duration} seconds to guess the number I am thinking of (between 1 and {max_range}).")
    
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > timer_duration:
            print("\nTime's up! You did not guess the number in time.")
            print(f"The correct number was {number}.")
            break
        
        guess = int(input(f"Guess the number (You have {timer_duration - int(elapsed_time)} seconds left): "))
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number} correctly!")
            print(f"You took {round(elapsed_time, 2)} seconds to guess.")
            break

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
11