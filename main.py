import json
from pathlib import Path

FILE = Path("expenses.json")

def load_expenses():
    if FILE.exists():
        with open(FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)


from datetime import date


from datetime import date

def add_expense():
    title = input("Expense name: ")
    category = input("Expense category: ")

    try:
        amount = float(input("Amount (Rs): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    expense_date = date.today().isoformat()

    expenses = load_expenses()

    expenses.append({
        "title": title,
        "category": category,
        "amount": amount,
        "date": expense_date
    })

    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n===== YOUR EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense #{i}")
        print(f"Name: {expense['title']}")
        print(f"Category: {expense.get('category', 'Not set')}")
        print(f"Amount: Rs {expense['amount']:.2f}")
        print(f"Date: {expense.get('date', 'Not set')}")


def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to delete. ")
        return
    
    view_expenses()

    try:
        number = int(input("Enter expense number to delete:"))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)

            print(f"{removed['title']} delete successfully!")
        else:
            print("Invalid expense number. ")

    except ValueError:
        print("Please enter a valid number.")

def total_expenses():
    expenses = load_expenses()
    total = sum(item["amount"] for
item in expenses)
    print(f"Total expenses: Rs {total:.2f}")


def category_report():
    expenses = load_expenses()
    category = input("Enter category: ").strip().lower()

    total = 0

    for expense in expenses:
        if expense.get("category", "").lower() == category:
            total += expense["amount"]

    print(f"Total spent on {category}: Rs {total:.2f}")



def monthly_report():
    expenses = load_expenses()
    month = input("Enter month (YYYY-MM): ").strip()

    if len(month) != 7 or month[4] != "-":
        print("Invalid format! Use YYYY-MM, e.g. 2026-10.")
        return

    try:
        year = int(month[:4])
        month_number = int(month[5:])

        if year < 1 or not 1 <= month_number <= 12:
            print("Invalid year or month.")
            return

    except ValueError:
        print("Please enter numbers in YYYY-MM format.")
        return

    total = 0
    count = 0

    for expense in expenses:
        expense_date = expense.get("date", "")

        if expense_date.startswith(month):
            total += expense["amount"]
            count += 1

    print(f"\n===== REPORT: {month} =====")
    print(f"Number of expenses: {count}")
    print(f"Total spent: Rs {total:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Category Report")
        print("6. Monthly Report")
        print("7. Exit")

        choice = input("Choose an option:")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            category_report()
        elif choice == "6":
            monthly_report()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again. ")

if __name__ == "__main__":
            main()