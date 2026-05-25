import pandas as pd
import os
from datetime import datetime
import budget

CSV_FILE = "data/expenses.csv"
CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Health", "Other"]

def initialize_csv():
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(CSV_FILE, index=False)

def add_expense():
    print("\n========== ADD EXPENSE ==========")
    print("Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("\nSelect category (1-7): "))
            if 1 <= choice <= 7:
                category = CATEGORIES[choice - 1]
                break
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            amount = float(input("Amount (₹): "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    df = pd.read_csv(CSV_FILE)
    new_row = pd.DataFrame([[date, category, amount, description]],
                           columns=["Date", "Category", "Amount", "Description"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

    print(f"\n✅ Expense added! ₹{amount:.2f} for {category}")

    total = df["Amount"].sum()
    budget.check_budget(total)

def view_monthly_report():
    print("\n========== MONTHLY REPORT ==========")
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        print("No expenses recorded yet!")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    months = df["Date"].dt.to_period("M").unique()

    print("Available months:")
    for i, m in enumerate(months, 1):
        print(f"  {i}. {m}")

    while True:
        try:
            choice = int(input("\nSelect month: "))
            if 1 <= choice <= len(months):
                selected = months[choice - 1]
                break
            else:
                print(f"Enter between 1 and {len(months)}")
        except ValueError:
            print("Invalid input.")

    monthly = df[df["Date"].dt.to_period("M") == selected]
    summary = monthly.groupby("Category")["Amount"].sum()
    total = monthly["Amount"].sum()

    print(f"\n📅 Report for {selected}")
    print("─" * 45)
    print(f"{'Category':<20} {'Amount (₹)':>10}   {'%':>5}")
    print("─" * 45)

    for cat, amt in summary.items():
        pct = (amt / total) * 100
        print(f"{cat:<20} ₹{amt:>9.2f}   {pct:>4.1f}%")

    print("─" * 45)
    print(f"{'TOTAL':<20} ₹{total:>9.2f}")

    if budget.get_budget() > 0:
        b = budget.get_budget()
        if total > b:
            print(f"\n⚠️  Over budget by ₹{total - b:.2f}!")
        else:
            print(f"\n✅ Within budget! ₹{b - total:.2f} remaining.")

    return selected, monthly

def view_all_expenses():
    print("\n========== ALL EXPENSES ==========")
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        print("No expenses recorded yet!")
        return

    print(f"\n{'Date':<12} {'Category':<16} {'Amount':>10}  Description")
    print("─" * 60)

    for _, row in df.iterrows():
        print(f"{row['Date']:<12} {row['Category']:<16} ₹{row['Amount']:>9.2f}  {row['Description']}")

    print("─" * 60)
    print(f"{'TOTAL':<30} ₹{df['Amount'].sum():>9.2f}")

def compare_months():
    print("\n========== COMPARE MONTHS ==========")
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        print("No expenses recorded yet!")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    summary = df.groupby(["Month", "Category"])["Amount"].sum().unstack(fill_value=0)

    print(summary.to_string())
    return df