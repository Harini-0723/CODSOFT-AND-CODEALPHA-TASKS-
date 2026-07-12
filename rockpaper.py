import random

choices = ["rock", "paper", "scissors"]


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"


def main():
    user_score = 0
    computer_score = 0

    print("=" * 45)
    print("      ROCK PAPER SCISSORS GAME")
    print("=" * 45)

    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_input = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_input not in choices:
            print("Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose      : {user_input}")
        print(f"Computer chose : {computer_choice}")

        result = determine_winner(user_input, computer_choice)

        if result == "user":
            print("🎉 You Win!")
            user_score += 1
        elif result == "computer":
            print("💻 Computer Wins!")
            computer_score += 1
        else:
            print("🤝 It's a Tie!")

        print("\nCurrent Score")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("\n========== FINAL SCORE ==========")
            print(f"You      : {user_score}")
            print(f"Computer : {computer_score}")

            if user_score > computer_score:
                print("🏆 Congratulations! You won the game.")
            elif computer_score > user_score:
                print("💻 Computer won the game.")
            else:
                print("🤝 The game ended in a tie.")

            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()