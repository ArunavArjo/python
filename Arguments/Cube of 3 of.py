def cube(number):
    return number*number*number

def divide_by_three (number):
    if number % 3 == 0:
        return cube(number)
    
    else:
        return False
    
print(divide_by_three(5))