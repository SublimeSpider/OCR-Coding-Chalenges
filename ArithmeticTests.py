import random

name = input("Enter your name : ")
score = 0
total = 0

def question(score):
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)
    opp = random.randint(1,4)
    if opp == 1:
        ans = float(num1 + num2)
        symb = "+"
    elif opp == 2:
        ans = float(num1 - num2)
        symb = "-"
    elif opp == 3:
        ans = float(num1 * num2)
        symb = "X"
    elif opp == 4:
        ans = float(num1 / num2)
        symb = "÷"
    answer = float(input(f"What is {num1} {symb} {num2} : "))
    if ans == answer:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
    return score

for i in range(1,10):
    total = total + question(score)

print(f"Your total score was : {total}")

file = open("ArithmeticTest.csv","a")
file.write(str([name,total]))
file.close()
