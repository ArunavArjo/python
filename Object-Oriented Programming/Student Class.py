class Student:
    isStudent = True

    def __init__(self,name,role):
        self.name = name
        self.role = role

s1 = Student('Lila Mozunder',20)
print(f"Hello my name is:{s1.name},and my role is:{s1.role},isStudent:{s1.isStudent}")

s2 = Student('mafus',29)
print(f"Hello my name is:{s2.name},and my role is:{s2.role},isStudent:{s1.isStudent}")