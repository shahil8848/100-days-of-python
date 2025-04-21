print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to Treasure Island 🏴‍☠️")
print("Your mission is to find the treasure 💰")

choice1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake.\n"
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There are three doors with different colors.\n"
                        "Type 'yellow' to choose the yellow door,\n"
                        "Type 'green' to choose the green door,\n"
                        "Type 'red' to choose the red door: ").lower()
        if choice3 == "yellow":
            print("🎉 Congratulations! You obtained the holy sword and found the treasure!")
        elif choice3 == "red":
            print("🔥 Game Over. A red dragon burned you to ashes.")
        else:
            print("👹 Game Over. A gang of green goblins ambushed you. Better luck next time!")
    else:
        print("🐟 Game Over. You got attacked by an angry trout.")
else:
    print("🕳️ Game Over. You fell into a hole.")

