import tracker
import visualizer
import budget

def main():
    tracker.initialize_csv()

    print("\n" + "=" * 40)
    print("   💰 PERSONAL EXPENSE TRACKER")
    print("=" * 40)

    while True:
        print("\n📋 MAIN MENU")
        print("─" * 30)
        print("  1. ➕ Add Expense")
        print("  2. 📊 View Monthly Report")
        print("  3. 📋 View All Expenses")
        print("  4. 🎯 Set Session Budget")
        print("  5. 📈 Compare Months (Bar Chart)")
        print("  6. 🥧 Generate Pie Chart")
        print("  7. 🚪 Exit")
        print("─" * 30)

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            result = tracker.view_monthly_report()
            if result:
                selected, _ = result
                sub = input("\nGenerate pie chart for this month? (y/n): ")
                if sub.lower() == "y":
                    visualizer.generate_pie_chart(str(selected))

        elif choice == "3":
            tracker.view_all_expenses()

        elif choice == "4":
            while True:
                try:
                    amount = float(input("\nEnter budget limit (₹): "))
                    if amount > 0:
                        budget.set_budget(amount)
                        break
                    else:
                        print("Budget must be greater than 0.")
                except ValueError:
                    print("Invalid input.")

        elif choice == "5":
            tracker.compare_months()
            sub = input("\nGenerate bar chart? (y/n): ")
            if sub.lower() == "y":
                visualizer.generate_bar_chart()

        elif choice == "6":
            visualizer.generate_pie_chart()

        elif choice == "7":
            print("\n👋 Goodbye! Track your expenses daily! 💰")
            break

        else:
            print("❌ Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()