# main.py

import random
from hangman_art import stages,logo
from hangman_words import word_list



print(logo)
# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize game variables
lives = 6
game_over = False
display = ["_"] * word_length
guessed_letters = []  # Store all guessed letters
wrong_letters = []  # Store only wrong guesses

print("🎮 Welcome to Hangman!")
print(f"You have {lives} lives to complete the game.\n")
print("Word to guess: " + " ".join(display))
print(stages[0])

# Main game loop
while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Life lost!")
        lives -= 1
    else:
        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        else:
            print(f"Oops! '{guess}' is not in the word.life lost ")
            lives -= 1
            wrong_letters.append(guess)
            print(f"remaining lives {lives}")

    print("\nWord: " + " ".join(display))
    print(stages[6 - lives])

    if wrong_letters:
        print(f"Wrong guesses so far: {', '.join(wrong_letters)}")

    if "_" not in display:
        game_over = True
        print("\n🎉 Congratulations! You guessed the word correctly and won the game!")

    if lives == 0:
        game_over = True
        print("\n😢 You lost all your lives.")
        print(f"The word was: '{chosen_word}'.")

print("\nThanks for playing Hangman! 🪂")
