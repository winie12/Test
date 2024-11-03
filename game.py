import random

def user_option():
    options = ["Rock", "Paper", "scissors"]
    for i,option in enumerate(options):
        print(f"{i+ 1}:{option}")
    
    choice = int(input("Choose your option: "))
    if choice not in range(1,4):
        print("Invalid option")
        return user_option()
    return options[choice-1]

def computer_option():
    options = ["Rock", "Paper", "scissors"]
    choice = random.randint(0,2)
    return options[choice]


def play():
    user_choice = user_option()
    computer_choice = computer_option()
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("You lose!")
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print("You lose!")
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print("You lose!")
    else:
        print("You win!")

play()
