income = float(input("Enter your monthly income"))
expenses = float(input("Enter your monthly expenses"))
monthly_savings = income - expenses
print(f"Your monthly savings is: {monthly_savings:.2f}")

annual_savings = monthly_savings * 12
annual_savings += annual_savings * 0.05
print(f"Your annual savings is :{annual_savings:.2f}")


