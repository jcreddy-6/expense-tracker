budget_limit = 0

def set_budget(amount):
    global budget_limit
    budget_limit = amount
    print(f"\n✅ Budget set to ₹{amount:.2f} for this session!")

def check_budget(total):
    if budget_limit == 0:
        return
    if total > budget_limit:
        over = total - budget_limit
        print(f"\n⚠️  BUDGET ALERT! You are over budget by ₹{over:.2f}!")
    else:
        remaining = budget_limit - total
        print(f"\n✅ Within budget! ₹{remaining:.2f} remaining.")

def get_budget():
    return budget_limit