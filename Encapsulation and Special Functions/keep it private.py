class MyClass:
    __Privatevar = 27

    def __privatemethod(self):
        print("Iam a private number:")

    def hello(self):
        print("Printing the private method:",self.__privatemethod)

m1 = MyClass()
m1.hello()