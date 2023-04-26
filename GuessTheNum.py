import random

def play_game(max_number):
    random_number = random.randint(1, max_number)
    num_guesses = 0
    while True:
        user_guess = int(input("Enter your guess (between 1 and " + str(max_number) + "): "))
        num_guesses += 1
        if user_guess == random_number:
            print("Congratulations! You guessed the number in " + str(num_guesses) + " guesses.")
            break
        elif user_guess < random_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

def main():
    print("Welcome to the guessing game!")
    max_number = int(input("Enter the maximum number you want to guess: "))
    play_game(max_number)
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()

#Another method for guessing numbers("Run separately")
import random

def play_game(top_of_range):
    random_number = random.randint(1, top_of_range)
    guesses = 0

    while True:
        user_guess = int(input("Make a guess: "))
        guesses += 1

        if user_guess == random_number:
            print(f"You got it in {guesses} guesses!")
            break
        elif user_guess < random_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

    return guesses

while True:
    top_of_range = int(input("Enter a maximum number: "))
    num_of_games = int(input("How many games would you like to play? "))
    total_guesses = 0

    for i in range(num_of_games):
        print(f"\nGame #{i+1}")
        guesses = play_game(top_of_range)
        total_guesses += guesses

    average_guesses = total_guesses / num_of_games
    print(f"\nAverage number of guesses per game: {average_guesses:.2f}")

    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again != "y":
        break
    