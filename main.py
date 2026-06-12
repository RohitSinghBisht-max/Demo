# Expense Tracker Project

expensesList = [] #List of expenses in form of dictionary
print("Welcome to Expense Tracker")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

# 1. Add Expense
    if(choice == 1):
        date = input("Enter the Date: ")
        category = input("Enter the category (Food, Travel, Makeup, Books, etc): ")
        description = input("Give More Detail: ")
        amount = float(input("Enter the amount: "))

        expenses = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expenses)
        print(" \n DONE bro. Expense is added succesfully")

# 2. View All Expenses
    elif(choice == 2):
        if(len(expensesList)==0):
            print("No Expenses Added")
        else:
            print("===== Ye y apka sara expense =====")
            count= 1
            for eachKharcha in expensesList:
                print(f"Kharcha Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]}")
                count = count + 1

# 3. View Total Spending
    elif(choice == 3):
        total = 0
        for eachKharcha in expensesList:
            total = total + eachKharcha["amount"]

        print("\n TOTAL KHRCHA = ", total)

# 4. EXIT
    elif(choice == 4):
        print("Thaank you for using our System")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")