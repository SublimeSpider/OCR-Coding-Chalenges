import random

winnings = 0
credit = 1

def fruitMachine(winnings):
    scores = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    fruits = []
    for i in range(0,len(scores)):
        if scores[i] == 1:
            fruits.append("Cherry")
        elif scores[i] == 2:
            fruits.append("Bell")
        elif scores[i] == 3:
            fruits.append("Lemon")
        elif scores[i] == 4:
            fruits.append("Orange")
        elif scores[i] == 5:
            fruits.append("Star")
        else:
            fruits.append("Skull")
    print(fruits)
    a = scores[0]
    b = scores[1]
    c = scores[2]
    if (a == b == c) and (a == 2):
        winnings = winnings + 5
    elif (a == b == c) and (a != 6):
        winnings = winnings + 1
    elif ((a == b) and (a != 6)) or ((b == c) and (b != 6)) or ((a == c) and (a != 6)):
        winnings = winnings + 0.5
    elif a == b == c == 6:
        winnings = 0
    elif (a == b) or (b == c) or (a == c):
        winnings = winnings - 1
    print("£"+str(winnings)+" earned")
    cont = input("Continue? True/False : ")
    print()
    return cont,winnings

while credit > 0:
    cont = fruitMachine(winnings)
    credit = credit - 0.2
    if cont[0] == 'False':
        credit = 0

print("Your total winnings are : £"+str(cont[1]))
