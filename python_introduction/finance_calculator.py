monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings is: {monthly_savings:.2f}")


#calculate annual savings by multiplying monthly savings by we and adding the total interest for the 12 months

annual_savings = monthly_savings * 12 + (monthly_savings *12 *0.05)
#annual_savings += annual_savings * 0.05
print(f"Your annual savings is :{annual_savings:.2f}")


