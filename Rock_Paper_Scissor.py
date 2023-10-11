import random
def get_my_turn():
    while True:
        my_turn = input("Choose R (Rock), P (Paper), or S (Scissors): ").strip().lower()
        if my_turn in ["r", "p", "s"]:
            return my_turn
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_comp_turn():
    choices = ["r", "p", "s"]
    return random.choice(choices)

def evaluate_turns(my_turn, comp_turn):
    if my_turn == comp_turn:
        return "DRAW!!!"
    if (
        (my_turn == "r" and comp_turn == "scissors") or
        (my_turn == "p" and comp_turn == "rock") or
        (my_turn == "s" and comp_turn == "paper")
    ):
        return "You win🎉✨"
    return "Computer wins🎊🎉"

def main():
    user_score = 0
    computer_score = 0

    while True:
        my_turn = get_my_turn()
        if my_turn == 'n':
            break
        comp_turn = get_comp_turn()

        print(f"You chose {my_turn.upper()}")
        print(f"Computer chose {comp_turn.capitalize()}")

        result = evaluate_turns(my_turn, comp_turn)
        print(result)

        if result == "You win🎉✨":
            user_score += 1
        elif result == "Computer wins🎊🎉":
            computer_score += 1

        print(f"Score Board :-\nYou: {user_score},\nComputer: {computer_score}")

        play_again = input("Play again? (y(yes)/n(no)): ").strip().lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    main()

