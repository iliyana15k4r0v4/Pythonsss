'''Assignment 4: Functions
Deliverable: Modular Budget System (Version 3.0)
Topic Focus: Breaking code into separate functions
Task: Refactor code into reusable functions for better code organisation
Requirements:
▪ Create functions for: getting user input, calculating expenses, showing
results
▪ Each function should do one clear job
▪ Add simple docstrings (1-2 lines explaining what each function does)
▪ Use parameters and return values effectively
▪ Use a main() function to run everything
Hints:
▪ def get_positive_float(prompt) # Validates input and returns positive float
▪ def get_user_input(): # gets all budget input from user with validation
▪ def calculate_budget(income, rent, food, transport, entertainment): # calculates total expenses
and money remaining
▪ def analyse_status(money_left): # determines budget status and provides recommendations
▪ def show_results(income, rent, food, transport, entertainment, total_expenses, money_left): #
displays formatted budget report
▪ def main(): # main programme function'''
from Project.budget_tracker_v1 import weelkly_income
from Project.budget_tracker_v2 import total_expenses, money_left


def get_positive_input(value):
    """Ask the user for a positive float and validate input."""
    if value.isdigit():
        value=float(value)
        if value < 0:print("Please enter a number greater than 0.")
        else: return value
    else:   print("Invalid input. Please enter a valid number.")

def get_user_input():
    """Gets user input and validates input."""
    weekly_income = get_positive_input(input(input("Enter the weekly income: ")))
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
    weelkly_income,rent,groceries,transport, ent_costs = get_user_input()
    total_expenses,money_left=calculate_budget(weelkly_income,rent,groceries,transport,ent_costs)
    analyse_status(money_left)
    show_results(weelkly_income,rent,groceries,transport, ent_costs,total_expenses,money_left)



