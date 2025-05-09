expense = []
def addexpenseAugustin():
    AugustinInput = input("Enter the category eg. Food, Rent, Travel: ")
    AugustinInput2 = input("Please enter the amount spent: ")
    AugustinInputDate = input("Please enter the date you spent the money (YYYY/MM/DD): ")
    expenses = {
        "Category": AugustinInput,
        "Amount": float(AugustinInput2),
        "Date": AugustinInputDate,
    }
    expense.append(expenses)
    print("Expense Added Successfully")
def expenseviewAugustin():
    if (expense) == 0:
        print("There are no expenses")
    else:
        print("All Expenses: ")
        for i in range(len(expense)):
            print(f"{i + 1}. category: {expense[i]['Category']}, amount: ${expense[i]["Amount"]:.2f}, date: {expense[i]["Date"]}")
            print()
def expensefilter():
    AugustinInput = input("Enter the category to filter: ")
    found = False
    for expenses in expense:
        if expenses["Category"].lower() == AugustinInput.lower():
            print(f"category: {expenses["Category"]}, amount: ${expenses["Amount"]:.2f}, date: {expenses["Date"]}")
            found = True
            
    if not found:
        print("No expenses found for this category")
        
def totalAugustinExpenses():
    total = 0
    for expenses in expense:
        total += expenses["Amount"]
    print(f"total expenses: ${total:.2f}")
def expenseAugustinDelete():
    expenseviewAugustin()
    if len(expense) == 0:
        return
    choice = input("Enter the number of expense to delete: ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(expense):
            deletedAugustin = expense.pop(index)
            print(f"Deleted Expense: {deletedAugustin["Category"]} of ${deletedAugustin["Amount"]:.2f}")
        else:
            print("Invalid Expense number")
    else:
        print("Invalid Input, please enter a real number")
def mainAugustin():
    while True:
        print("Expense Tracker Menu")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by category")
        print("4. Calculate total expenses")
        print("5. Delete an expense")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            addexpenseAugustin()
        elif choice == "2":
            expenseviewAugustin()
        elif choice == "3":
            expensefilter()
        elif choice == "4":
            totalAugustinExpenses()
        elif choice == "5":
            expenseAugustinDelete()
        elif choice == "6":
            break
        else:
            print("Invalid choice")
mainAugustin()