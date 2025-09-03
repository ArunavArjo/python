class IOString:
    def __init__(self):
        self.str1 = ""
    
    def get_string(self):
        self.str1 = input("Enter a string:")

    def print_string(self):
        self.str1 = print("The result is",self.str1.upper)

s1 = IOString()
s1.get_string()
s1.print_string()