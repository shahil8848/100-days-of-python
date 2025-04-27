#start of day 7 Hangman project
import random
word_list =['aardvark','baboon','camel']

word=random.choice(word_list)
print(word)

guess=input("Guess a letter:").lower()
print(guess)

display= ""
for letter in word:
    if letter == guess:
        display+=letter
    else:
        display+="_"
print(display)
#explain range function