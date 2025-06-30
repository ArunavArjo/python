num = int(input("Enter a number:"))

sum = 0
orgNum = num
while orgNum > 0:
    digit = orgNum % 10
    sum = sum + digit**3
    orgNum //= 10

if num == sum:
    print("The number is armstrong number")
else:
    print("The number is not a armstrong number")
