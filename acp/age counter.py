while True:
    try:
        age = int(input("Enter your age : "))
        if 1 <= age <= 100:
            print("You have entered the age:", age)
            break  
        else:
            print("Age must be between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")