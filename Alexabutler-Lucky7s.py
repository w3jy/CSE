import random
print("Welcome to Lucky7s")
money = 15
Round = 1
Highscore = 0
while money > 0:
    money -= 1
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)

    Round += 1

    if num1+num2 == 7:
        print("You win ")
        money += 5
        print(money)
        print(Round)
        if Highscore < money:
            print("Highscore")
            Highscore = money
    else:
        print("Roll again")
        print(money)
        print(Round)

    if money == 0:
        print("You Lose")
        print(money)
        print("You played %d rounds." % Round)
        print ("Your Highscore was %d dollars." % Highscore)
