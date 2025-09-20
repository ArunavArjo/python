import random
class Fruitquiz:
    def __init__(self):
        self.fruits = {
            'apple':'red',
            'orange':'orange',
            'lemon':'green',
             'pineapple':'yellow'
        }


    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print(f"What is the color of {fruit}")

            answer = input()
            if answer == color:
                print("Corrcet answer")
            else:
                print("Wrong answer")

            option = int(input("Enter 0 if you Want to add else press 1 to exit"))
            if (option == 1):
                break

print("Welcome to fruitquiz")
fq = Fruitquiz()
fq.quiz()