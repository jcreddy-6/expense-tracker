import matplotlib.pyplot as plt
import pandas as pd
import os

CSV_FILE = "data/expenses.csv"

def generate_pie_chart(month_str=None):
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print("No data to visualize!")
        return

    df["Date"] = pd.to_datetime(df["Date"])

    if month_str:
        df = df[df["Date"].dt.to_period("M").astype(str) == str(month_str)]

    if df.empty:
        print("No data for selected month!")
        return

    summary = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 8))
    colors = ["#6366f1", "#f78166", "#3fb950", "#f0b429", "#60a5fa", "#c084fc", "#fb923c"]
    plt.pie(summary.values, labels=summary.index, autopct="%1.1f%%",
            colors=colors[:len(summary)], startangle=140)
    plt.title(f"Spending Breakdown — {month_str}", fontsize=14, fontweight="bold")

    os.makedirs("reports", exist_ok=True)
    filename = f"reports/pie_{month_str}.png"
    plt.savefig(filename, bbox_inches="tight", dpi=150)
    plt.show()
    print(f"\n✅ Pie chart saved to {filename}")

def generate_bar_chart():
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print("No data to visualize!")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    summary = df.groupby(["Month", "Category"])["Amount"].sum().unstack(fill_value=0)

    ax = summary.plot(kind="bar", figsize=(12, 6), colormap="tab10")
    plt.title("Month-over-Month Expense Comparison", fontsize=14, fontweight="bold")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.legend(loc="upper right")
    plt.tight_layout()

    os.makedirs("reports", exist_ok=True)
    filename = "reports/bar_comparison.png"
    plt.savefig(filename, bbox_inches="tight", dpi=150)
    plt.show()
    print(f"\n✅ Bar chart saved to {filename}")