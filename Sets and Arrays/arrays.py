import array as sigma
num_array = sigma.array("i",[1,2,3,4,5,6,7,6,5,4,3,2,1])

print("Occurence of 3 :",num_array.count(3))

num_array.reverse()
print("Reverse",num_array)

num_array.remove(4)
print(num_array)

num_array.insert(0,4)
print(num_array)
num_array.extend([1,2,3,3,34,5])
print(num_array)