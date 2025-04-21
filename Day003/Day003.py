# if condition:
# do this
#else:
#do this
#conditional statements
# water_level=50
# if water_level> 80:
#     print("Drain water")
# else:
#     print("continue")
#
# print("Welcome to the rollercoaster!!!!!!")
# height= int(input('Enter the height in the cm?'))
#
# if height >= 120:
#     print("You can right the rollercoaster")
#     age= int(input("What is your age?"))
#     if age<=18:
#         print("Please pay 7$")
#     else:
#         print("Please pay 12 $")
# else:
#     print("Sorry you cannot ride the rollercoaster")


# number= int(input("Enter the number:"))
# if number%2 == 0:
#     print(f"{number} is even number")
# else:
#     print(f"{number} is odd number")
#
print("Welcome to the rollercoaster!!!!!!")
height= int(input('Enter the height in the cm?'))
bill=0
if height>=120:
    print("You can ride the rollercoaster")
    age= int(input("Enter your age? "))
    if age< 12:
        bill=5
        print("Child ticket are 5 $")
    elif  age <= 15:
        bill=7
        print("youth ticket are 7 $")
    elif 45<=age<=55:
    # elif age>= 45 and age<=55:
        print("This is on the house. Enjoy the ride")
    else:
        bill=12
        print("Adult ticket are 12 $")


    wants_photo= input("Do you want to have a photo take? type y for Yes and n for No  ")
    if wants_photo == "y":
        bill+=3

    print(f"Your bill is ${bill}. Thank you for taking ride with us ")

else:
    print("Sorry you have to grow taller before you can ride.")


#LOGICAL OPERATORS AND OR NOT
