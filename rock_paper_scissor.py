import random as rd

while True:
    user_action = input("Enter your choice(Rock, Paper, Scissor): ")
    comp_action = rd.choice(["rock", "paper", "scissor"])
    print(f"You choose {user_action} and Computer choose {comp_action}")

    if user_action == comp_action:
        print("🟡 It's a Tie")
    
    elif user_action == "rock":
        if comp_action == "scissor":
            print("🟢 Rock smashed the Scissor, you won!!")
        else:
            print("🔴 Paper cover the Rock, you lose")
    
    elif user_action == "scissor":
        if comp_action == "paper":
            print("🟢 Scissor cuts the Paper, you won!!")
        else:
            print("🔴 Rock smashed the Scissor, you lose")

    elif user_action == "paper":
        if comp_action == "rock":
            print("🟢 Paper covers the Rock, you won!!")
        else:
            print("🔴 Scissor cuts the Paper, you lose")

    play_again = input("Want to play again(Y/N): ")
    if play_again == "N" or "n":
        break