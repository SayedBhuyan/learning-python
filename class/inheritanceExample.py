from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        print("I'm area method of shape")


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        return area


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        return area


t1 = Triangle(20, 30)
print(t1.area())

r1 = Rectangle(20, 30)
print(r1.area())
