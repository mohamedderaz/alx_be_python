mon_incom = int (input("Enter your monthly income: "))
mon_exp = int(input("Enter your total monthly expenses: "))
mon_sav =  mon_incom - mon_exp
project_saving = (mon_sav *12) + ((mon_sav*12)*.05)                       
print("Your monthly savings are " +str(mon_sav) + " $")
print("Projected savings after one year, with interest, is: " +str(project_saving) +" $")
