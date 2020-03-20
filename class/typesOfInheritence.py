class A:
    def display(self):
        print("I'm A class")


class B:
    def display(self):
        print("I'm B class")


class C( A, B ):
    pass
    # def display(self):
    #     print("I'm C class")
    #

obj1 = C()
obj1.display()