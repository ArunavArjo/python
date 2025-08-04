import random
playing = True
num = str(random.randint(10,20))
print("It will genarate numbers between 10 to 20 now give your guess : ")

while playing:
    guess = input("Now give your best guess: ")
    if num == guess :
        print("You won!")
        print("The number was", num)
        break
    else:
        print("Incorret guess! Please try again.")