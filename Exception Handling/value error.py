try:
    number = int(input("enter a number:"))
    print("You have entered a number",number)

except ValueError as ex:
    print("Exception has occured",ex)