
look_up = input("What acronym would you look up?\n")

with open('c:/users/cbrav/Documents/input.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            break
    else:
        print("Acronym not found.")