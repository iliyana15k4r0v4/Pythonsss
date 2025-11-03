'''Assignment 5: Loops and Iterations
Deliverable: Multi-Week Budget Tracker (Version 4.0)
Topic Focus: Using while loops and for loops
Task: Extend your budget system to track data across multiple weeks using a
menu-driven interface. Since we're not using lists yet, you'll track summary
statistics (running totals and averages) rather than storing individual week
details.
Requirements:
▪ Add a menu system with options:
▪ Add This Week's Budget
▪ Show Overall Summary
▪ Exit
IS1110 Tutorial Portfolio Project 4/10
▪ Use a while loop to keep the programme running until the user chooses
to exit
▪ Track across all weeks entered:
▪ Total number of weeks entered
▪ Total income across all weeks
▪ Total expenses across all weeks
▪ Running averages (average weekly income and expenses)
▪ Use loops to validate input (keep asking until valid)
▪ After each week is entered, show how it compares to the running averages
▪ Continue using functions to organize your code (building on Assignment
4)
Hints:
week_count = 0
total_income = 0
total_expenses = 0
while True: # keeps going until user chooses to exit
# show menu and get choice
if choice == 1: # Add week
week_count += 1
total_income += this_week_income
total_expenses += this_week_expenses
# calculate and show averages
Sample Output:
=== Week 3 Added ===
This week's income: €200
This week's expenses: €150
Average weekly income so far: €210
Average weekly expenses so far: €140
Submission: Python file (budget_tracker_v4.py)'''


def get_positive_input(value):
    """Ask the user for a positive float and validate input."""
    if value.isdigit():
        value=float(value)
        if value < 0:print("Please enter a number greater than 0.")
        else: return value
    else:   print("Invalid input. Please enter a valid number.")

def get_user_input():
    """Gets user input and validates input."""
    weekly_income = get_positive_input(input("Enter the weekly income: "))
    rent=get_positive_input(input("Enter the rent: "))
    groceries=get_positive_input(input("Enter the amount spent on groceries: "))
    transport=get_positive_input(input("Enter the amount spent on transport: "))
    ent_costs=get_positive_input(input("Enter the amount spent on entertainment: "))
    return weekly_income, rent, groceries, transport, ent_costs

def calculate_budget(weekly_income,rent,groceries,transport,ent_costs):
    """Calculates total expenses"""
    total_expenses = rent + groceries + transport + ent_costs
    money_left = weekly_income - total_expenses
    return total_expenses, money_left

def analyse_status(money_left):
    if money_left > 0:
        print(
            "You have enough money\nAdvice:\n1) Build an Emergency Fund\n2) Invest for Growth\n3) Pay Off High-Interest Debt\n4) Allocate with a Simple Rule (Example: 50/30/20)")
    elif money_left == 0:
        print(
            "You have balanced spending\nAdvice:\n1) Maintain your current level.\n2) Automate payments to stay consistent.\n3) Review occasionally for efficiency.")
    else:
        print("OVERSPENDING! You need to cut expenses by €", money_left,
              "\nAdvice:\n1) Reduce non-essential expenses (e.g., dining out, entertainment, subscriptions).\n2) Set limits or use budgeting tools.\n3) Redirect the excess to savings, debt repayment, or investments.\n4) Typical surplus categories:\n* Eating Out / Coffee Shops\n* Shopping / Lifestyle\n* Entertainment & Leisure\n* Convenience Transportation (taxis, ride-share)")


def show_results(weekly_income, rent, groceries, transport, ent_costs,total_expences,money_left):
    """Displays budget summary"""
    print("\n-----BUDGET SUMMARY----- \n")
    print("Weekly income: €",weekly_income)
    print("Rent : €",rent)
    print("Groceries : €",groceries)
    print("Transport : €",transport)
    print("Entertainment : €",ent_costs)
    print("---------------------------")
    print("Total : €",total_expences)
    print("Money left : €",money_left)

    analyse_status(money_left)

    print("\n-----END-----")

def main():
    """Main function"""

    weeks_count = 0
    total_income = 0
    all_expenses = 0

while True:
    print("--+MENU---------------------\n1)+ Add this weeks budget   |\n2)+ Show overall summary    |\n3)+ Exit                    |")
    choice = input("C +Choose an option (1-3): ")
    print("--+-------------------------|")
    choice = int(choice)

    if choice == 1:
        weeks_count=+1
        weelkly_income,rent,groceries,transport, ent_costs = get_user_input()
        total_expenses,money_left=calculate_budget(weelkly_income,rent,groceries,transport,ent_costs)
        total_income=+weelkly_income
        all_expenses=+total_expenses
        avg_income = total_income/weeks_count
        avg_expenses = all_expenses/weeks_count
    elif choice == 2:
        if weeks_count == 0:
            print("\nNo data available yet. Please add at least one week first.\n")
        else:
            avg_income = total_income / weeks_count
            avg_expenses = all_expenses/ weeks_count
            print("\n------ OVERALL SUMMARY -------------")
            print("Weeks entered:", weeks_count)
            print("Total income for all weeks: €",total_income)
            print("Total expenses for all weeks: €",all_expenses)
            print("Average weekly income: €",avg_income)
            print("Average weekly expenses: €",avg_expenses)
            print("-------------------------------------\n")

    elif choice == 3:
        print("Exiting the program.")
        quit()

