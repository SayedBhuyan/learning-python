class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim = Student(101, 4.5)
rahim.display()

karim = Student(102, 4.6)
karim.display()

