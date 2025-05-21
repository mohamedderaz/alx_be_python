monthly_income = int (input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
Monthly_Savings =  monthly_income - monthly_expenses
project_saving = (Monthly_Savings *12) + ((Monthly_Savings*12)*.05)                       
print("Your monthly savings are " +str(Monthly_Savings) + " $")
print("Projected savings after one year, with interest, is: " +str(project_saving) +" $")
