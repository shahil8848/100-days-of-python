#Tip calculator and bill seperator  project
print("WELCOME TO THE TIP CALCULATOR!\n")
bill= float(input("What is the total bill amount? $"))
tip=float(input("How much percentages tip would you like to give? %"))
tip_in_number= tip/100
total_bill=((bill*tip_in_number)+bill)
print(f"Your net total bill amount including tip is ${round(total_bill,3)}")
no_of_people= int(input("How many people to split the bills?"))
pay=total_bill/no_of_people
print(f"Each person should pay: ${round(pay,3)}")
print("Thank You")
