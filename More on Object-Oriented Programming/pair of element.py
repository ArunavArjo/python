class pair_elements:
    def twosum(self,nums,target):
        
        for i, num1 in enumerate(nums):
            for i, num2 in enumerate(nums):
                if num1+num2 == target:
                        return(num1,num2)
                
value = int(input("Enter your value:"))

nums = [10,20,30,40,50,60,70,80,90]
result = pair_elements().twosum(nums,value)

if result:
     print(f"Value1={result[0]},Value2={result[1]}")

else:
    print("Pair not found")