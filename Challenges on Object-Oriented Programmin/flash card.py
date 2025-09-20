class Flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word}--->{self.meaning} "
    


flashcards = []
print("Welcome to flashcard aplication")


while True:
    word = input("Enter the name you want to add:")
    meaning = input("Enter the meaning you want to add:")

    flashcards.append(Flashcard(word,meaning))

    option = int(input("Enter 0 if you Want to add else press 1 to exit"))
    if (option == 1):
        break
print("<---Your flashcards are--->")
for i in flashcards:
    print(">",i)
