string = input("Enter a string")
string2 =''
for char in string:
    string2 = char + string2

print("Orignal string:",string)
print("Reversed string",string2)