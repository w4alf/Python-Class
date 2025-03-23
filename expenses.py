expenses = [10.5,8,5,15,20,5,3]

total = 0


for x in expenses:
    total = total + x
print("You spent $",total," on lunch this week.",sep='')


total= 0
# or use sum() function to calculate the sum of the list
total = sum(expenses)   
print("You spent $",total," on lunch this week.",sep='')