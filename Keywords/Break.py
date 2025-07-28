word = input("Enter a word:")

for i in word:
    if i == "u":
        print("u is found loop exited")
        break
    else:
        print(i)