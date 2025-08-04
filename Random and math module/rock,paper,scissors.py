import random
while True:
    user = input("Enter a choice: (Rock,paper,scissors )")
    computer = random.choice(['rock','paper','scissors'])
    print(f"You choose {user},Computer choose {computer}")

    if user == computer:
        print("Its a tie")
    elif user == 'rock' and computer == 'scissors':
        print("You won")
    elif user == 'rock' and computer == 'paper':
        print("You lost")
    elif user == 'paper' and computer == 'scissors':
        print("You lost")
    elif user == 'paper' and computer == 'rock':
        print("You won")
    elif user == 'scissors' and computer == 'paper':
        print("You won")
    elif user == 'scissors' and computer == 'paper':
        print("You won")

    Play_again = input("Do you want to play again ?(y/n)")
    if Play_again == 'n':
        break
    
    