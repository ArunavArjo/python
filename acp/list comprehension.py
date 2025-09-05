
n = int(input("Enter a number: "))
odd_numbers = [i for i in range(n) if i % 2 != 0]
odd_numbers_squared = [i*i for i in odd_numbers]
print("Odd numbers:", odd_numbers)
print("Odd numbers squared:", odd_numbers_squared)

fruits = ['apple', 'banana', 'mango', 'orange']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruit list:", capitalized_fruits)
