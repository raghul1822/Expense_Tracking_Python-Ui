from datetime import datetime

class ExpenseTracker:
    def __init__(self, username="Alien De Villiers"):
        # Profile & Initial Balance Setup
        self.username = username
        self.initial_balance = 12458.50
        
        # Transaction Storage
        self.transactions = [
            {"date": "2026-03-01", "type": "Expense", "category": "Meals", "amount": 210000.0, "note": "Dinner out"},
            {"date": "2026-03-02", "type": "Expense", "category": "Groceries", "amount": 650000.0, "note": "Lunar Year Foods"},
            {"date": "2026-03-05", "type": "Income", "category": "Salary", "amount": 210000.0, "note": "Monthly Pay"},
            {"date": "2026-03-10", "type": "Income", "category": "Freelance", "amount": 650000.0, "note": "ITGrate Project"}
        ]
        
        # Financial Goals Storage
        self.goals = {
            "Vacation": {"target": 250000.0, "saved": 175000.0, "end_date": "2026-07-03", "note": "Trip to Mexico"},
            "Technology": {"target": 12000.0, "saved": 175000.0, "end_date": "2026-07-03", "note": "New Iphone 17 Pro Max"}
        }

    # --- Balance Calculation ---
    def get_current_balance(self):
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'Income')
        total_expense = sum(t['amount'] for t in self.transactions if t['type'] == 'Expense')
        return self.initial_balance + total_income - total_expense

    # --- Feature 1: Add New Transaction ---
    def add_transaction(self):
        print("\n--- NEW TRANSACTION ---")
        t_type = input("Select Type (1 for Expense, 2 for Income): ").strip()
        t_type = "Expense" if t_type == "1" else "Income"
        
        print(f"\nSelect Category for {t_type}:")
        categories = ["Meals", "Groceries", "Rent", "Shopping", "Fun", "Transport", "Health"] if t_type == "Expense" else ["Salary", "Freelance", "Business", "Investment", "Gift", "Refund", "Passive Income"]
        
        for idx, cat in enumerate(categories, 1):
            print(f"[{idx}] {cat}")
        
        cat_choice = int(input("Category Number: ")) - 1
        category = categories[cat_choice] if 0 <= cat_choice < len(categories) else "More"
        
        amount = float(input("Enter Amount ($): "))
        note = input("Enter Note/Description: ")
        date_str = input("Enter Date (YYYY-MM-DD or press Enter for Today): ").strip()
        if not date_str:
            date_str = datetime.today().strftime('%Y-%m-%d')
            
        self.transactions.append({
            "date": date_str,
            "type": t_type,
            "category": category,
            "amount": amount,
            "note": note
        })
        print(f" Success! {t_type} of ${amount:,.2f} recorded under '{category}'.")

    # --- Feature 2: Analytics & Breakdown (Pie Chart Representation) ---
    def view_analytics(self):
        print("\n--- ANALYTICS BREAKDOWN ---")
        t_type = input("Select Breakdown (1 for Expense, 2 for Income): ").strip()
        target_type = "Expense" if t_type == "1" else "Income"
        
        filtered = [t for t in self.transactions if t['type'] == target_type]
        total_amt = sum(t['amount'] for t in filtered)
        
        if total_amt == 0:
            print(f"No {target_type} data found to analyze.")
            return

        # Calculate category group sums
        cat_totals = {}
        for t in filtered:
            cat_totals[t['category']] = cat_totals.get(t['category'], 0) + t['amount']
            
        print(f"\nBreakdown for {target_type}s (Total: ${total_amt:,.2f}):")
        print("-" * 50)
        for cat, amt in sorted(cat_totals.items(), key=lambda item: item[1], reverse=True):
            percentage = (amt / total_amt) * 100
            # Visually simulate a distribution bar based on the UX chart percentages
            bar = "||" * int(percentage // 5)
            print(f"{percentage:3.0f}% | {cat:<15} : ${amt:<12,.2f} {bar}")
        print("-" * 50)

    # --- Feature 3: Financial Goals Management ---
    def manage_goals(self):
        while True:
            print("\n--- TARGET FINANCIAL GOALS ---")
            for name, data in self.goals.items():
                progress = (data['saved'] / data['target']) * 100
                print(f"\n Goal: {name} ({data['note']})")
                print(f"   Progress: [{progress:.1f}%] Saved: ${data['saved']:,.2f} / Target: ${data['target']:,.2f}")
                print(f"   Deadline: {data['end_date']}")
            
            print("\n[1] Add New Goal  [2] Delete/Edit Goal  [3] Back to Main Menu")
            choice = input("Action: ").strip()
            
            if choice == "1":
                name = input("Goal Name (e.g., New Car): ")
                note = input("Description: ")
                target = float(input("Target Amount ($): "))
                saved = float(input("Already Saved ($): "))
                date = input("End Date (YYYY-MM-DD): ")
                self.goals[name] = {"target": target, "saved": saved, "end_date": date, "note": note}
                print(" Goal created successfully!")
            elif choice == "2":
                name = input("Enter Goal Name to manage: ")
                if name in self.goals:
                    action = input("Type 'D' to Delete or 'E' to Edit Saved Amount: ").upper()
                    if action == 'D':
                        del self.goals[name]
                        print(" Goal Deleted.")
                    elif action == 'E':
                        new_saved = float(input("Update Current Saved Amount ($): "))
                        self.goals[name]['saved'] = new_saved
                        print(" Goal Updated.")
                else:
                    print("Goal not found.")
            else:
                break

    # --- Feature 4: Overview Dashboard ---
    def show_dashboard(self):
        print("\n=============================================")
        print(f" USER: {self.username} | WELCOME BACK")
        print(f" CURRENT WALLET BALANCE: ${self.get_current_balance():,.2f}")
        print("=============================================")
        
        # Recent Transactions
        print("\n RECENT TRANSACTIONS (Latest 3)")
        for t in self.transactions[-3:]:
            sign = "-" if t['type'] == "Expense" else "+"
            print(f"   [{t['date']}] {t['category']:<12} | {sign}${t['amount']:<10,.2f} ({t['note']})")
            
    # --- Main Navigation Loop ---
    def run(self):
        while True:
            self.show_dashboard()
            print("\n APP NAVIGATION MENU:")
            print("[1] Log New Transaction (Expense/Income)")
            print("[2] Analytics & Category Breakdown")
            print("[3] Financial Goals Tracker")
            print("[4] Exit App Simulation")
            
            choice = input("\nSelect Tab Option (1-4): ").strip()
            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.view_analytics()
            elif choice == "3":
                self.manage_goals()
            elif choice == "4":
                print("\nGoodbye! Keep tracking your spending safely.")
                break
            else:
                print(" Invalid entry, pick an action code between 1 and 4.")

# Execute Tracker Simulation Engine
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
