import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    player1 = input("Enter player 1 name:\n ")
    player2 = input("Enter player 2 name:\n ")    

    player1_roll = roll_dice()
    player2_roll = roll_dice()

    print(player1, "rolled", player1_roll)
    print(player2, "rolled", player2_roll)

    if player1_roll > player2_roll:
        print(player1, "wins!")
    elif player1_roll < player2_roll:
        print(player2, "wins!") 
    else:
        print("It's a tie!")

main()

