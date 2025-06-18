units = int(input())
if units < 50:
    amounts = units*5
    surchange = 25
elif units<= 100:
    amounts = units*7.5
    surchange = 35
elif units<= 200:
    amounts = units*9.5
    surchange = 50
else:
    amounts = units*10
    surchange = 70
    total = amounts+surchange
    print("Total electricity bill is",total)