amount = int(input("Enter the amount :")) #4660

note500 = amount // 500 #9
amount = amount % 500 #4660 % 500 = 160
note100 = amount // 100
amount = amount % 100 #160 % 60 = 100
note50 = amount // 50
amount = amount % 50 #60 % 50 = 10
note10 = amount // 10 #1
amount = amount % 10 #10 % 10 

print("Note of 500:",note500)
print("Note of 100:",note100)
print("Note of 50:",note50)
print("Note of 10:",note10)
print("Remaining amount:",amount)