s1 = {1,2,3}
s2 = {'a','c','l'}

s3 = list(zip(s1,s2))
print(s3)

List_1 = [12,30,46]
List_2 = [200,500,900]

for x, y in zip(List_1,List_2[::-1]):
    print(x,y)

Stocks = ['Target','Mexica','24/7']
Prices = [1200,7000,8901]

dict = {Stocks: Prices for Stocks,Prices in zip(Stocks,Prices)}
print(dict)