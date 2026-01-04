import csv
import datetime
import os

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        print("\nAll Expenses:")
        for row in reader:
            print(row)

def total_expense():
    total = 0
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[2])

    print("Total Expense:", total)

def category_wise_total():
    totals = {}

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[2])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    print("\nCategory-wise Expense:")
    for cat, amt in totals.items():
        print(cat, ":", amt)

def menu():
    print("\n==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category-wise Total")
    print("5. Exit")


while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expense()
    elif choice == '4':
        category_wise_total()
    elif choice == '5':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Try again.")

