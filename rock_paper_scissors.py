import random

def play_game():
    print("--- Task 4: Rock-Paper-Scissors ---")
    options = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            break
        if user_choice not in options:
            print("Invalid choice, try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
