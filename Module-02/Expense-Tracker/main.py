

import json
expenses = []

def add_expense():
    print("\n--- Add New Expense ---")


    
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            break

        except ValueError:
            print("Please enter a valid numeric amount!")

    category = input("Enter category (Food/Travel/Shopping): ")
    description = input("Enter description: ")
    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses()
    print("\nExpense added successfully!")
    

def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found!")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(f"Amount: ₹{expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Date: {expense['date']}")



def show_total():
    print("\n--- Total Expenses ---")

    if not expenses:
        print("No expenses recorded yet!")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expenses: ₹{total:.2f}")





def delete_expense():
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses available to delete!")
        return

    view_expenses()

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)

            save_expenses()

            print(f"\nExpense '{removed['description']}' deleted successfully!")
        else:
            print("Invalid expense number!")

    except ValueError:
        print("Please enter a valid number!")


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully!")




def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []


def show_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

load_expenses()
while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
       delete_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
