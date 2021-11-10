import random #this allows computer to pick random

while True:
    user_action = input("Welcome to Rock, Paper, Scissors! To play, please choose one of the following actions. (rock, paper, scissors):")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
            print(f"Both of you selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors, you WIN!")
        else:
            print("Paper covers rock, you LOSE!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock, you WIN!")
        else:
            print("Scissors cuts paper, you LOSE!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper, you WIN!")
        else:
            print("Rock smashes scissors, you LOSE!")

    play_again = input("Play again? (yes or no): ")
    if play_again.lower() != "yes":
        print("Thank you for playing!")
        break