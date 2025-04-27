import random

stages = [
    r'''
     +---+
     |   |
         |
         |
         |
         |
    =========
    ''',
    r'''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    r'''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    r'''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    r'''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''',
    r'''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''',
    r'''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    '''
]

word_list = ['aardvark', 'baboon', 'camel']
lives = 6

chosen_word = random.choice(word_list)
print(f"You have {lives} lives to complete this game.")
word_length = len(chosen_word)

placeholder = ''
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"Your guessed letter is: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    print(stages[6 - lives])

    # if "_" not in display:
    #     game_over = True
    #     print("You win! 🎉")
