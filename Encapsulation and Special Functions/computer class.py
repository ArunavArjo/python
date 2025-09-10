class Computer:
    def __init__(self):
        self.__maxprice =900

    def sell(self):
        print(f"selling__price:{self.__maxprice}")

    def setmaxprice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()

c.setmaxprice(800)
c.sell()