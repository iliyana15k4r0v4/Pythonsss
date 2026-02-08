"""Assignment 6: Strings
Deliverable: Improved Budget Categories (Version 5.0)
Topic Focus: Working with text data using string methods
Task: Enhance the weekly budget entry process by allowing users to add
optional short descriptions to expense categories. These descriptions help
users remember what each expense was for (e.g., 'Tesco weekly shop' for
groceries).
Requirements:
▪ When entering a new week's data, let users add optional short
descriptions for each expense category (rent, groceries, transport,
entertainment)
▪ Use string methods for data cleaning:
▪ .strip() to remove extra spaces
▪ .title() or .capitalize() for proper capitalization
▪ Note that the methods can be chained (.strip().title())
▪ Continue using functions to organize your code
▪ Display the current week's expenses with their cleaned descriptions
immediately after entry
▪ Continue tracking the summary statistics from Assignment 5
IS1110 Tutorial Portfolio Project 5/10
Hints:
# When getting expense input
rent_desc = input("Rent description (optional): ").strip().title()
groceries_desc = input("Groceries description (optional): ").strip().title()
# Display after week entry
print(f"Rent: €{rent:.2f} - {rent_desc}")
print(f"Groceries: €{groceries:.2f} - {groceries_desc}")
Submission: Python file (budget_tracker_v5.py)
Sample Output:
Enter rent amount: 800
Rent description (optional): monthly apartment rent
Enter groceries: 120
Groceries description (optional): tesco weekly shop
=== Week 2 Budget Details ===
Rent: €800.00 - Monthly Apartment Rent
Groceries: €120.00 - Tesco Weekly Shop
Transport: €30.00 -
Entertainment: €50.00 - Cinema And Dinner
Submission: Python file (budget_tracker_v5.py)
Assignment 7: Output Formatting
Deliverable: Professional Budget Reports (Version 6.0)
Topic Focus: Create professionally formatted console reports using string
formatting
Task: Make your budget reports look neat, organized, and professional with
proper alignment and formatting.
Requirements:
▪ Implement consistent currency formatting (€ symbol, 2 decimal places
everywhere)
▪ Add headers and boders to make reports visually clear
▪ Use functions to organize different parts of your output:
▪ Separate functions for weekly reports and summary reports
▪ Functions for formatting different types of output
▪ Create aligned columns for category names and amounts
▪ Add report headers with the current date (use from datetime import date at
the top of the programme file)
▪ Show summary statistics with percentages:
▪ What percentage of average income goes to each expense category
▪ Percentage of income remaining as savings
▪ Format both the weekly detail view AND the overall summary view"""
from datetime import date

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

    print ("Enter weekly expenses and description: " )
    rent=get_positive_input(input("Enter the rent: "))
    rent_desc=input("Enter the rent description (optional): ").strip().title()

    groceries=get_positive_input(input("Enter the amount spent on groceries: "))
    groceries_desc=input("Enter groceries description (optional): ").strip().title()

    transport=get_positive_input(input("Enter the amount spent on transport: "))
    transport_desc=input("Enter transport description (optional): ").strip().title()

    ent_costs=get_positive_input(input("Enter the amount spent on entertainment: "))
    entertainment_desc=input("Enter entertainment description (optional): ").strip().title()

    descriptions ={"Rent :"+rent_desc,"Groceries :"+groceries_desc,"Transport :"+transport_desc,"Entertainment :"+entertainment_desc}

    return weekly_income, rent, groceries, transport, ent_costs,descriptions

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

def weekly_report(weekly_income,rent,groceries,transport,ent_costs,descriptions,total_expenses,money_left):
    date_today=date.today()
    print ("="*40)
    print(f"Your weekly report".center(40))
    print(f" Date: {date_today}".center(40))
    print( "=" * 40 )

    print(f"{'Category':<15}")
    print("-" * 40)
    print(f"{'Income':<15} €{weekly_income:>10,.2f}")

    print(f"{'Rent':<15} €{rent:>10,.2f}")
    print(f"{'Groceries':<15} €{groceries:>10,.2f}")
    print(f"{'Transport':<15} €{transport:>10,.2f}")
    print(f"{'Entertainment':<15} €{ent_costs:>10,.2f}")

    print("-" * 40)
    print(f"{'Total Expenses':<15} €{total_expenses:>10,.2f}")
    print(f"{'Remaining':<15} €{money_left:>10,.2f}")
    print('Descriptions:',descriptions)
    print( "=" * 40 )


def main():
    """Main function"""

    weeks_count = 0
    total_income = 0
    all_expenses = 0

while True:
    print("--+MENU---------------------\n"
          "1)+ Add this weeks budget   |\n"
          "2)+ Show overall summary    |\n"
          "3)+ Exit                    |")
    choice = input("C +Choose an option (1-3): ")
    print("--+-------------------------|")
    choice = int(choice)

    if choice == 1:
        weeks_count=+1
        weelkly_income,rent,groceries,transport,ent_costs,descriptions = get_user_input()
        total_expenses,money_left=calculate_budget(weelkly_income,rent,groceries,transport,ent_costs)
        total_income=+weelkly_income
        all_expenses=+total_expenses
        avg_income = total_income/weeks_count
        avg_expenses = all_expenses/weeks_count
        weekly_report(weelkly_income,rent,groceries,transport,ent_costs,descriptions,total_expenses,money_left)

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

