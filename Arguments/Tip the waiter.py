def calculate_total_bill(Bill_Amount,Total_perc):
    total = Bill_Amount + Bill_Amount *(Total_perc*0.01)
    total = round(total,2)
    print(f"Please pay,${total}")

calculate_total_bill(100,10)