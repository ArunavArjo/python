def calculate_due_amount(total_bill, amount_paid):
  """
  Calculates the remaining due amount after a payment.

  Args:
    total_bill: The total amount of the bill.
    amount_paid: The amount paid by the customer.

  Returns:
    The remaining due amount.
  """
  due_amount = total_bill - amount_paid
  return due_amount

# Get input from the user
try:
  bill_amount = float(input("Enter the total bill amount: "))
  paid_amount = float(input("Enter the amount paid by the customer: "))

  # Calculate the due amount
  remaining_due = calculate_due_amount(bill_amount, paid_amount)

  # Display the result
  if remaining_due > 0:
    print(f"The customer still owes: ${remaining_due:.2f}")
  elif remaining_due < 0:
    print(f"Change to be returned to the customer: ${abs(remaining_due):.2f}")
  else:
    print("The bill has been fully paid.")

except ValueError:
  print("Invalid input. Please enter numerical values for amounts.")