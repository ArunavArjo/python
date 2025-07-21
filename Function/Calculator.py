def add(a,b):
    return(a+b)
def subtraction(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def division(a,b):
    if b == 0:
        return("division in not allowed")
    else:
        return(a/b)

print("welcome to calculator")
print("a.Add")
print("b.subtraction")
print("c.multiplication")
print("d.division")

choice = input("select one of a/b/c/d:")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
    
if choice == 'a':
    print("reasult",add(num1,num2))

elif choice == 'b':
    print("reasult",subtraction(num1,num2))

elif choice == 'c':
    print("reasult",multiply(num1,num2))

elif choice == 'd':
    print("reasult",division(num1,num2))