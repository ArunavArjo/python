word = input("Enter a word")
char = input("Enter a charecter")

i = 0
count = 0
for i in word:
    if i == char:
        count += 1
    
print (f"{char} occurs {count} times in the words{word}.")