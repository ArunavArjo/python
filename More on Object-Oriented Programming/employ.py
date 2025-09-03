class employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Employ destructed")

    def hello_ali(self):
        print("Hello Ali")

obj = employee()
obj.hello_ali()