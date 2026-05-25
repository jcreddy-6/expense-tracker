# 💰 Personal Expense Tracker

> A Python CLI application to log, categorise, and analyse personal expenses — with visual monthly reports, pie charts, bar graphs, and session-based budget alerts.

---

## ✨ Features

- 📝 **Expense Logging** — Add expenses with category, amount, date, and description
- 📊 **Visual Reports** — Pie charts (spending breakdown) and bar graphs (month-over-month trends)
- 📅 **Monthly Analysis** — Filter and compare spending across months
- 🔔 **Budget Reminders** — Get alerts when spending exceeds your set budget for the session
- 🗂️ **Category Tracking** — Organise expenses into Food, Transport, Entertainment, Bills, etc.
- 💾 **CSV Storage** — Lightweight file-based storage, no database needed

---

## 📸 Sample Output

```
========================================
   PERSONAL EXPENSE TRACKER
========================================

> Add Expense
  Amount: 450
  Category: Food
  Description: Lunch at canteen
  ✅ Expense added!

> View Monthly Report — May 2026
─────────────────────────────────
  Category        Amount (₹)   % of Total
  Food              3,200         42%
  Transport         1,500         20%
  Entertainment       900         12%
  Bills             1,800         24%
  ─────────────────────────────
  Total             7,400
  Budget Set        6,000
  ⚠️  Over budget by ₹1,400!

> [Pie chart and bar graph saved to /reports/]
```

---

## 📊 Visualizations

**Pie Chart** — Category-wise spending breakdown for a selected month

**Bar Graph** — Month-over-month expense comparison across categories

Both charts are auto-saved as `.png` files in the `/reports/` folder.

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core application logic |
| Matplotlib | Pie charts and bar graphs |
| Pandas | Data manipulation and monthly filtering |
| CSV | Lightweight persistent storage |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/jcreddy-6/expense-tracker
cd expense-tracker

# Install dependencies
pip install matplotlib pandas

# Run the application
python main.py
```

---

## 📂 Project Structure

```
expense-tracker/
├── main.py               # Entry point — main menu loop
├── tracker.py            # Core logic: add, view, filter expenses
├── visualizer.py         # Matplotlib charts (pie + bar)
├── budget.py             # Session budget management + alerts
├── data/
│   └── expenses.csv      # Expense records (auto-created)
├── reports/              # Generated chart images saved here
└── README.md
```

---

## ⚙️ How It Works

```
User runs main.py
      ↓
Main Menu:
  [1] Add Expense
  [2] View Monthly Report
  [3] Set Budget
  [4] Compare Months
  [5] Exit
      ↓
Expenses saved to expenses.csv (Pandas DataFrame)
      ↓
On report request → Matplotlib generates charts
      ↓
Budget check → alert if total > set limit
```

---

## 🗺️ Roadmap (Planned Features)

- [ ] GUI version using Tkinter
- [ ] Export reports to PDF
- [ ] Recurring expense tracking
- [ ] Multi-user support with login

---

## 📜 License

MIT License — free to use and modify.

---

## 👤 Author

**Thigulla Jhansi Chandra Reddy**
2nd Year B.Tech CSE — Anurag University, Hyderabad
[LinkedIn](https://www.linkedin.com/in/jhansi-chandra-reddy-a14b15382/) | [GitHub](https://github.com/jcreddy-6)
