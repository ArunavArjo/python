lst = [1,2,3,4,5,6,7,8,12,33,87,45,88,10,47]
even_list = [num for num in lst if num%2 ==0]
print(even_list)

Number_1  = [1,2,3,4,5]
Number_2 = [6,7,8,9,10]
result = map(lambda x,y: x+y ,Number_1,Number_2)
print(list(result))

nums = [1,8,9,4,6]

def square (n):
    return n*n

squared = map(square,nums)
print("Squared : ",list(squared) )
