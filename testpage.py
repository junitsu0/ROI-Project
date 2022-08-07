income = {"rent":0, "laundry":0, "storage":0}
expense = {"tax":0, "insurance":0, "utilities":0, "HOA":0, "yard":0, "management":0, "repairs":0, "vacancy":0, "CapEx":0, "mortgage":0}
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

#main flow
mainmenu = int_input("""
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
""")

while mainmenu != 5:
#income menu 
    if mainmenu == 1:
        incomemenu = int_input("""
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
""")
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
            mainmenu
    #expense menu
    elif mainmenu == 2:
        expmenu = int_input("""
    ==================
     Expense Sources
    ==================
     1. Tax
     2. Insurance
     3. Utilities
     4. HOA
     5. Yard
     6. Management
     7. Repairs
     8. Vacancy
     9. CapEx
    10. Mortgage
    11. Misc
    12. View
    13. Main Menu      
    ==================
      Enter a number
    ==================
""")
        if expmenu == 1:
            cost = int_input("Enter the monthly amount per unit ")
            expense["tax"] += cost
        elif expmenu == 2:
            cost = int_input("Enter the monthly amount per unit ")
            expense["insurance"] += cost
        elif expmenu == 3:
            cost = int_input("Enter the monthly amount per unit ")
            expense["utilities"] += cost
        elif expmenu == 4:
            cost = int_input("Enter the monthly amount per unit ")
            expense["HOA"] += cost
        elif expmenu == 5:
            cost = int_input("Enter the monthly amount per unit ")
            expense["yard"] += cost
        elif expmenu == 6:
            cost = int_input("Enter the monthly amount per unit ")
            expense["management"] += cost
        elif expmenu == 7:
            cost = int_input("Enter the monthly amount per unit ")
            expense["repairs"] += cost
        elif expmenu == 8:
            cost = int_input("Enter the monthly amount per unit ")
            expense["vacancy"] += cost
        elif expmenu == 9:
            cost = int_input("Enter the monthly amount per unit ")
            expense["CapEx"] += cost
        elif expmenu == 10:
            cost = int_input("Enter the monthly amount per unit ")
            expense["mortgage"] += cost
        elif expmenu == 11:
            expenseitem = input("What item would you like to add? ")
            if expenseitem in expense:#if item exists add to quantity
                print("Item is already accounted for.")
            else:#add item to cart with quantity and cost - quack quack
                cost = int_input("Enter the monthly amount per unit ")
                expense[expenseitem] = cost
                print(f"{expense[expenseitem]} is now accounted for.")
        elif incomemenu == 12:
            print(expense)
        elif incomemenu != {1,2,3,4,5,6,7,8,9,10,11,12}:
                print("Enter a valid number please. ")
        else:
            continue
    elif mainmenu == 3:
        invmenu = int_input("""
    ==================
       Investments
    ==================
    1. Down Payment
    2. Closing Costs
    3. Rehab Budget
    4. Misc
    5. View
    6. Main Menu      
    ==================
      Enter a number
    ==================
""")
        if invmenu == 1:
            cost = int_input("Enter the monthly amount per unit ")
            investment["downpayment"] += cost
        elif invmenu == 2:
            cost = int_input("Enter the monthly amount per unit ")
            investment["closingcost"] += cost
        elif invmenu == 3:
            cost = int_input("Enter the monthly amount per unit ")
            investment["rehab"] += cost
        elif invmenu == 4:
            investitem = input("What item would you like to add? ")
            if investitem in investment:#if item exists add to quantity
                print("Item is already accounted for.")
            else:#add item to cart with quantity and cost - quack quack
                cost = int_input("Enter the monthly amount per unit ")
                investment[investitem] = cost
                print(f"{investment[investitem]} is now accounted for.")
        elif invmenu == 5:
            print(investment)
        elif invmenu != {1,2,3,4,5}:
                print("Enter a valid number please. ")
        else:
            continue


else:
    print("Goodbye")
    exit