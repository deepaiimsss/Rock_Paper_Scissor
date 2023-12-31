import random

def get_my_turn():
    while True:
        my_turn = input("Choose R (Rock), P (Paper), or S (Scissors): ").strip().lower()
        if my_turn in ["r", "p", "s"]:
            return my_turn
        else:
            print("Invalid choice!!!Please try again..")

def get_comp_turn():
    choices = ["r", "p", "s"]
    return random.choice(choices)

def cal_turns(my_turn, comp_turn):
    my_turn = my_turn.lower()
    if my_turn == comp_turn:
        return "Result : The match is a DRAW!!!"
    if (
        (my_turn == "r" and comp_turn == "s") or
        (my_turn == "p" and comp_turn == "r") or
        (my_turn == "s" and comp_turn == "p")
    ):
        return "Result : You win🎉✨"
    return "Result : Computer wins🎊🎉"

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
        result = cal_turns(my_turn, comp_turn)
        print(result)
        if result == "Result : You win🎉✨":
            user_score += 1
        elif result == "Result : Computer wins🎊🎉":
            computer_score += 1
        print(f"------Score Board--------\nYou: {user_score}\nComputer: {computer_score}")
        play_again = input("Want to play again? (y(yes)/n(no)): ").strip().lower()
        if play_again != "y":
            break

main()
