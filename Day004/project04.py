# #rock,paper,scissors
#
# import random
#
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# print("Lets play the game of 'Rock', 'Paper' and 'Scissors'")
# user_choice= int(input("What do you Choose?\n"
#                          "Type'0' for Rock\n"
#                          "Type '1' for Paper\n"
#                         "Type '2' for Scissors  : "))
# number=[1,2,3]
# computer_choice= random.choice(number)
#
# if user_choice==0 and computer_choice==1:
#     print(f"You chose rock {rock}")
#     print(f"Computer chose paper {paper}")
#     print("You lose. Computer Won")
# elif user_choice==1 and computer_choice==1:
#     print(f"You chose paper {paper}")
#     print(f"Computer chose paper {paper}")
#     print("Its Draw")
# elif user_choice==2 and computer_choice==1:
#     print(f"You chose scissor {scissors}")
#     print(f"Computer chose paper {paper}")
#     print("You won congratulations")

import random

# ASCII art for each choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices
game_images = [rock, paper, scissors]

# Player input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print("\nYou chose:")
    print(game_images[user_choice])

    # Computer input
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")
