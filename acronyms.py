# Description: This program reads a file and looks up an acronym in it.

def find_acronym():
    # Ask the user for an acronym to look up
    look_up = input("What acronym would you look up?: ")
    found = False
    try:
        # Open the file and look for the acronym
        with open('c:/users/cbrav/Documents/input.txt') as file:
            for line in file:        #reads the file line by line
                if look_up in line:  #looks up a string in a line - string within a string
                    print("Acronym found: ",line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found.")
        return    
        
    if not found:
        print("Acronym not found.")

    
def add_acronym():
    acronym = input("what acronym would you like to add?\n")
    definition = input("What does the acronym stand for?\n")
    try:
        # Open the file and add the acronym, if the file indicated does not exist, it will create it
        with open('c:/users/cbrav/Documents/input.txt', 'a') as file:
            file.write(acronym + ' - ' + definition + '\n')
           
    except FileNotFoundError as e:
        print("File not found.")
        return
    print("Acronym added to file.")

def main():
   choice = input("Would you like to find an acronym or add one? '('F' for Find 'A' for Add): ")
   if choice == 'F':
       find_acronym()
   elif choice == 'A':
       add_acronym()
   else:
       print("Invalid choice.")   

main()