import random

number1 = random.randint(1,100)
i = 0

while True:
    number2 = input("Enter number or q if you want to finish: ")
    if number2 == "q" or number2 == "Q":
        print("The end")
        break
    elif number1 == int(number2):
        print("You win")
        break
    else:
        print("You lost")
        print(number1)
    i +=1