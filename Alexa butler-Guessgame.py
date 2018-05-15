import random
num = random.randint(1, 50)
print(num)
guesses_left = 5

number = 0
while number != str(num) and guesses_left > 0:
    number = input("Guess a number")
    guesses_left -= 1

    # print(number == str(num))

    if number == str(num):
        print("You win")
    elif number >= str(num):
        print("Guess lower")
    elif number <= str(num):
        print("Guess higher")
