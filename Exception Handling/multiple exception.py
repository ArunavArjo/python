try:
    num1,num2 = eval(input("Enter a number:"))
    reasult = num1 / num2
    print("Reasult is:",reasult)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except SyntaxError:
    print("Put the input correctly")

except:
    print("An exception has occured")

else:
    print("No exception has occured")

finally:
    print("Finally done")
