import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def add_expense(expenses):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses[category] = expenses.get(category, 0) + amount
    print(f"Added {amount} to {category}.")

def view_expenses(expenses):
    print("\nExpenses:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    print()

def main():
    filename = "expenses.json"
    expenses = load_data(filename)

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save and Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_data(expenses, filename)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
