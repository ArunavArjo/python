total_cost = int(input("Total_cost is:"))
sale_amount = int(input("Sale_amount is:"))

if sale_amount > total_cost:
    profit = sale_amount - total_cost
    print("Profit",profit)

else:
    loss = total_cost - sale_amount
    print("Loss",loss)
