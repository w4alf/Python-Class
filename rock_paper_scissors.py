['rock', 'paper', 'scissors']
import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice =str(input("Do you want - rock, paper, or scissors?\n"))
if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("Invalid choice. You lose!")

print("Computer chose", computer_choice)
print("You chose", user_choice)
if computer_choice == user_choice:
    print("It's a tie!")
elif computer_choice == "rock" and user_choice == "scissors":
    print("Computer wins!")
elif computer_choice == "scissors" and user_choice == "paper":
    print("Computer wins!")
elif computer_choice == "paper" and user_choice == "rock":
    print("Computer wins!")
else:
    print("You win!")
