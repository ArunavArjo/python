lower = int(input("Enter a lower bound"))
upper = int(input("Enter a upper bound"))

for i in range(lower,upper+1):
    if i > 0:
        for j in range(2,i):
                if (i %j) == 0:
                     break
        else:
            print(i, end=" ")