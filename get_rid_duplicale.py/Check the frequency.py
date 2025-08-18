fruits = {
    'Apple':6,
    'Bananna':7,
    'Watermelon':3,
    'Kiwi':7,
    'Strawberry':9,
    'Lotkon':5
}
res = 0
k = 6
for key in fruits:
    if fruits[key] == k:
        res +=1
print("The frequencys are",k ,"=", res)