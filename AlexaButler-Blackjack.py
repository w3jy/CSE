import random




money = 10
while money > 0:
    money -= 1
card1 = random.randint(1, 11)
card2 = random.randint(1, 11)
print(card1 + card2)

if card1 + card2 == 21:
    print("You win ")
    money += 5
    print(money)


