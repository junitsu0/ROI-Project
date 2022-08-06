#import any?

#====== LISTS n stuff ========
income = {}
expense = {}
investment = {}
#ledger = [{"income"}, {"expense"}, {"investment"}]
cashflow = sum(income[x][1]) - sum(expense[y][1]) 
ROI = cashflow / sum(investment[a][1])

print("""
Welcome to the ROI Calculator.
Please input whole numbers only.
""")

print("""
=======================
Please Choose an Option
=======================
1. Income
2. Expenses
3. Investments
4. Exit
""")





#Income
input("Rental Income per unit")
input("Laundry")
input("Storage/Garage")
input("Misc")

#Expenses
input("Tax")
input("Insurance")
input("Utilities")
input("HOA")
input("Yard/Snow")
input("Management")
input("Repairs")
input("Vacancy")
input("CapEx")
input("Mortgage")

#Investments
input("down payment")
input("closing costs")
input("rehab")
input("misc")






#? create a dictionary of inputs to store each topic and answer ?
#? equations pull from that dictionary the required matching information/key ?

#====================
#Inputs and Equations
#====================
#ROI = AnnualCashFlow / Total Investment

#Incomes
#-rent
#-laundry
#-storage
#-misc

#Expenses
#-Tax
#-Insurance
#-Utilities
#-water
#-gas
#-electric
#-sewage
#-trash
#-HOA
#-Yard/Snow
#-Management
#-Repairs
#-Vacancy
#-CapEx
#-Mortgage

#Monthly Cash Flow = Income - Expense

#Investments
#-down payment
#-closing costs
#-rehab
#-misc