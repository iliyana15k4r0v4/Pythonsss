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


weelkly_income=input("Enter the weekly income: ")
weelkly_income=float(weelkly_income)

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
money_left=weelkly_income-total_expenses

print("Weekly income= €"+str(weelkly_income)+"\nTotal expenses= €"+str(total_expenses)+"\nMoney left= €"+str(money_left))
