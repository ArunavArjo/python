lst = [1,2,7,5,4,5]

sum = 0
for i in lst:
    sum+= i
print("Sum",sum)

avg = sum / len(lst)
print("Average:",avg)

lst.sort()
print("Sort",lst)
print("Smallest",min(lst))