 # create a console-based Expense Tracker program in python that allows the user to record daily expenses and view summaries like total spending.

expenses = [] #list of expenses in form of dictionary 
print(" Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

#ADD Expense
    if(choice == 1):
        date= input("date: ")
        category= input("type: ")
        description= input("Description")
        amount= float(input("Amount: "))

        expenses= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expenses)
        print("  Expense is added succesfully")

# 2. VIEW ALL EXPENSES 
    elif(choice == 2):
        if( len(expenses)==0 ):
            print("No Expenses Added. please buy some product. ")
        else:
           print("===== your total Spending ======")
           count= 1
           for eachKharcha in expenses:
                print(f"expense {count} -> {expenses["date"]}, {expenses["category"]}, {expenses["description"]}, {expenses["amount"]} ")
                count= count+1

# 3. View TOtal Spending 
    elif(choice == 3):
        total= 0
        for eaxpenses in expenses:
            total = total + expenses["amount"]

        print("Total expense= ", total)

#4. EXIT 
    elif(choice == 4):
        print("Thankyou for using our system")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
