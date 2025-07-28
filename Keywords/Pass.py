for i in range(21):
    if i % 15 == 0:
        pass
    elif i % 10 ==0:
        print("Buzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 3 == 0:
        print("Slash")
    else:
        print(i)