class Person(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print("Name:", self.name, "ID",self.id)
class Employ(Person):
    def __init__(self, name, id,salary,post):
        Person.__init__(self,name, id)
        self.salary = salary
        self.post = post
    
emp = Employ("Awer",6473,90000,"IT")
emp.display()
        