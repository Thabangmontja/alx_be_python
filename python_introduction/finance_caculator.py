#Prompt user input
monthly_income = float(input("Enter your monthly: "))
monthly_expense = float(input("Enter your total monthly expenses: "))

#Caculation of monthly savings formaluar
monthly_savings = monthly_income - monthly_expense

#caculate projected savings after one year, assuming a 5% INTEREST RATE
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

#results
print(f"Your monthly saavings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")