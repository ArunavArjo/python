medical_cause = input("Did you have any medical issue(y/n)")


if medical_cause == 'y':
    print("allowed")
else:
    attendance = int(input("Enter your attandance percantage"))
    if attendance < 75:
        print("Not allowed")
    else:
        print("allowed")