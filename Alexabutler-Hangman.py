import random
import string

print("Welcome to Hangman")

guesses_left = 10
letters_guessed = []
# Word_bank
word_bank = ["cool", "fun", "happy", "school","class","nice","crazy","edison","dance", "test"]

# Random Choice
random_word = random.choice(word_bank)

correct_guess = False

while guesses_left > 0 and correct_guess is False:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))
    print(guesses_left)

    if output == list(random_word):
        print("You Win")
        exit(0)
    print(output)

    guess = input("Guess a letter A though Z")
    letters_guessed.append(guess)
    print(letters_guessed)
    guesses_left -= 1

    if guesses_left == 0:
        print("You Lose")
        print("Your random word was")
        print(random_word)
