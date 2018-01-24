import random
"""
A general guide for Hangman
1. Make a word bank - 10 items 
2. Pick a random item from the list
3. Add a guess to the list to guess
4. Reveal letters already guessed
5. Create the win condition
"""


# Word_bank
word_bank = [" Cool , Fun , Happy , School , Class , Nice , Computer , Edison , Awesome , Project "]

# Random Choice


random.choice
guesses_left = 10
correct_guess = False

while guesses_left > 0 and correct_guess is False:
    guess = input("Guess a letter A though Z")

letters_gusses = []
guesses =
