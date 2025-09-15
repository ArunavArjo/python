from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move (self):
        pass

class Human(Animal):
    def move(self):
        print(" I can walk on two legs")

class Snake(Animal):
    def move(self):
        print(" I can crawl")

class Dog(Animal):
    def move(self):
        print(" I can walk on four legs")

class Bird(Animal):
    def move(self):
        print(" I can fly")

R = Human()
R.move()

K = Snake()
K.move

M = Dog()
M.move

I = Bird()
I. move