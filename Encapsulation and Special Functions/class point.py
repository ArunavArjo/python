class point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def  show(self):
        return(f"{self.x},{self.y}")
    
    def move(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point move to{self.show()}")

    def add(self,other_point):
        new_x= self.x+other_point
        new_y = self.y+other_point
        return point(new_x,new_y)
    
p1 = point(3,7)
print(p1.show())
p1.move(8,8)
p2 = p1.add(3)
print(p2.show())

        