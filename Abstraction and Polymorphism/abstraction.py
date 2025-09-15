from abc import ABC, abstractmethod

class ABClass(ABC):
    def print(self,x):
        print("Passed value:",x)

    @abstractmethod
    def task(self):
        print("We are inside ABClass method")

class testClass(ABClass):
    def task(self):
        print("We are inside a class task method")

test_obj = testClass()
test_obj.task
test_obj.print(100)