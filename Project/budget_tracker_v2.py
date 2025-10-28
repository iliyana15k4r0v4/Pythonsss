#Assignment 2: Variables, Expressions & Statements
#Deliverable: Basic Budget Calculator (Version 1.0)
#Topic Focus: Using variables and calculations properly
#Task: Create a simple calculator that tracks weekly income and expenses
#Requirements:
#▪ Use meaningful variable names following Python naming conventions (e.g.,weekly_income, not x)
#▪ Prompt user for: weekly income, rent, groceries, transport, entertainment costs
#▪ Calculate total expenses and money left over
#▪ Display results showing income vs expenses
#▪ Include header comment and inline comments explaining calculations


weekly_income=input("Enter the weekly income: ")
if weekly_income.isdigit():
    weekly_income = float(weekly_income)
    if weekly_income <= 0: print("Enter a number bigger than 0")
else: print("Please enter a valid number"),exit()

print(type(weekly_income))


rent=input("Enter the rent: ")
rent=float(rent)

groceries=input("Enter the amount spent on groceries: ")
groceries=float(groceries)

transport=input("Enter the amount spent on transportation: ")
transport=float(transport)

ent_costs=input("Enter the amount spent on entertainment: ")
ent_costs=float(ent_costs)

total_expenses=0
money_left=0

total_expenses=rent+groceries+transport+ent_costs
money_left=weekly_income-total_expenses



'''
Assignment 3: Conditional Execution
Deliverable: Budget Status Checker (Version 2.0)
Topic Focus: Using if/elif/else statements to make decisions
Task: Extend calculator to provide financial health analysis and
recommendations, i.e., add logic to tell users if they are overspending or
doing well
Requirements:
▪ Add input validation for monetary amounts (e.g., no negative amounts,
only numeric values)
▪ Add conditional logic to determine budget status
(surplus/deficit/balanced)
▪ Give different messages for different situations
▪ Check if total expenses exceed income and provide appropriate warnings
▪ Provide personalised financial advice based on spending patterns
▪ Handle edge cases gracefully
IS1110 Tutorial Portfolio Project 3/10
Hints:
▪ Use if statements:
if money_left < 0:
print("You're overspending!")
elif money_left > 50:
print("Good job saving!")
▪ Make sure to handle the case where money_left == 0
Sample Output:
Money Left: €-20
Status: OVERSPENDING! You need to cut expenses by €20
Submission: Python file (budget_tracker_v2.py)'''

print("\n-----BUDGET SUMMARY----- \n")

if money_left>0:
    print("You have enough money\nAdvice:\n1) Build an Emergency Fund\n2) Invest for Growth\n3) Pay Off High-Interest Debt\n4) Allocate with a Simple Rule (Example: 50/30/20)")
elif money_left==0:
    print("You have balanced spending\nAdvice:\n1) Maintain your current level.\n2) Automate payments to stay consistent.\n3) Review occasionally for efficiency.")
else: print("OVERSPENDING! You need to cut expenses by €",total_expenses-weekly_income,
            "\nAdvice:\n1) Reduce non-essential expenses (e.g., dining out, entertainment, subscriptions).\n2) Set limits or use budgeting tools.\n3) Redirect the excess to savings, debt repayment, or investments.\n4) Typical surplus categories:\n* Eating Out / Coffee Shops\n* Shopping / Lifestyle\n* Entertainment & Leisure\n* Convenience Transportation (taxis, ride-share)")

print("\n-----END-----")

