import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT
)
""")
conn.commit()

def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
                   (amount, category, date))
    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    print("\nID | Amount | Category | Date")
    print("-" * 30)
    for row in rows:
        print(row)

def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print("\nTotal Expense:", total if total else 0)

def category_summary():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    print("\nCategory-wise Summary:")
    for row in rows:
        print(row[0], ":", row[1])

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amt = float(input("Enter amount: "))
        cat = input("Enter category: ")
        add_expense(amt, cat)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expense()
    elif choice == '4':
        category_summary()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")

conn.close()