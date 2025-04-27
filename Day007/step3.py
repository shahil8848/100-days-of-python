import random
word_list =['aardvark','baboon','camel']

chosen_word = random.choice(word_list)

placeholder=''
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)
game_over= False
correct_letter=[]

while not game_over:
    guess=input("Guess a letter:").lower()
    print(f"Your guessed letter is : {guess}")

    display=""

    for letter in chosen_word:
        if letter== guess:
            display+=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+= letter
        else:
            display+="_"

    print(display)


    if"_" not in display:
        game_over= True
        print("You win")
