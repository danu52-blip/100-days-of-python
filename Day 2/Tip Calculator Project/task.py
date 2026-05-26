print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (bill*(tip/100))+ bill
bill_for_each_one = bill_with_tip/people
bill_total = round(bill_for_each_one, 2)
print(f"Each one should be pay: $ {bill_total}")



