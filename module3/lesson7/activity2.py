import random#importing random module
while True:#iterate loop
    user_action=input("enter a choice(rock ,paper,scissors):")#take input
    possible_actions=["rock","paper","scissors"]
    #using random Functions
    computer_action=random.choice(possible_actions)
    print(f"\nYou chose {user_action},computer chose{computer_action}.\n")#display both outputs what is selected by you and computer
    
#conditions to check who won the game
    if user_action==computer_action:
        print(f"both players selected{user_action}.It's a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors you win")
        else:
            print("scissors cuts paper u lose")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("scissors cuts paper u win")
        else:
            print("rock smashes scissors u lose")
#take input for playing again
    play_again=input("Play again?(y/n):")
    if play_again !="y":
        break







