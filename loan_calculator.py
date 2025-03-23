#get details from user
money_owed = float(input("How much money do you owe, in dollars?\n")) #50000
apr = float(input("What is the annual percentage rate?\n")) # 3%
payment= float(input("How much will you pay each month?\n")) # 1,000
months =int(input("How many months do you want to see payments for?\n")) #24
#divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    #calculate interest to pay
    interest_payment = money_owed * monthly_rate
    #add interest to the money owed
    money_owed += interest_payment

    if (money_owed - payment< 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months.")
        break
    #make payment
    money_owed -= payment    
    
    print("Paid", payment, "of which", interest_payment, "was interest.", end=' ')
    print("Now I owe", money_owed)

