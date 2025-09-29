def calculate_square_root_exponent(number):
  """
  Calculates the square root of a number using the exponentiation operator.
  Args:
    number: The non-negative number for which to calculate the square root.
  Returns:
    The square root of the number.
  """
  if number < 0:
    return "Error: Cannot calculate square root of a negative number."
  return number ** 0.5

# Example usage
num = float(input("Enter a number: "))
result = calculate_square_root_exponent(num)
print(f"The square root of {num} is: {result}")