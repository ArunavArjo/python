valid = False
while not valid:

    try:
        n = int(input("Enter a number"))
        while n == 0:
            print("bye")
            valid = True
        
    except ValueError:
        print("Invalid value")