import random
def play():
    number = random.randint(1,100)
    name = input("Enter your name:")
    print(f"{name},Im thinking a number between 1 to 100")


    Hint = "Even" if number%2 == 0 else "odd"
    print(f"The number is {Hint}")

    for tries in range(6):
        guess = int(input("Take a guess:"))

        if guess < 1 or guess > 100:
            print("Take a number between 1 to 100")
            continue
        if guess < number:
            print("Too low")

        
        elif guess > number:
            print("Too high")

        else:
            print(f"Good job,{name}")
            return
        
while True:
    play()

    again = input("Play again? Yes/No:")
    if again == "No":
        break
