income = {"rent":0, "laundry":0, "storage":0}
expense = {"tax":0, "insurance":0, "utilities":0, "HOA":0, "yard":0, "management":0, "repairs":0, "vacancy":0, "CapEx":0, "Mortgage":0}
util = {"water":0, "elec":0, "gas":0, "trash":0, "sewage":0}
investment = {"downpayment":0, "closingcost":0, "rehab":0}
#ledger = [{"income"}, {"expense"}, {"investment"}]


def int_input(prompt):#check for invalid string inputs
    while True:
        try:
            edgecase = int(input(prompt))
            return edgecase
        except ValueError as x:
            print("Please enter a valid number.")


mainmenu = int(int_input("""
==================
  ROI Calculator
    Main Menu
==================
 1. Income
 2. Expenses
 3. Investments
 4. Summary
 5. Exit
==================
  Enter a number
==================
"""))
#main flow chart
while mainmenu != 5:
#income menu 
    if mainmenu == 1:
        incomemenu = int(int_input("""
==================
  Income Sources
==================
 1. Rent
 2. Laundry
 3. Storage
 4. Misc
 5. View
 6. Main Menu      
==================
  Enter a number
==================
"""))
#each option exists in dictionary
#misc items can be added to dictionary
        if incomemenu == 1:
            cost = int_input("Enter the monthly amount per unit ")
            income["rent"] += cost
        elif incomemenu == 2:
            cost = int_input("Enter the monthly amount per unit ")
            income["laundry"] += cost
        elif incomemenu == 3:
            cost = int_input("Enter the monthly amount per unit ")
            income["storage"] += cost
        elif incomemenu == 4:
            incomeitem = input("What item would you like to add? ")
            if incomeitem in income:#if item exists add to quantity
                print("Item is already accounted for.")
            else:#add item to cart with quantity and cost - quack quack
                cost = int_input("Enter the monthly amount per unit ")
                income[incomeitem] = cost
                print(f"{income[incomeitem]} is now accounted for.")
        elif incomemenu == 5:
            print(income)
        elif incomemenu != {1,2,3,4,5,6}:
                print("Enter a valid number please. ")
                
else:
    print("Goodbye")
    exit