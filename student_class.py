class Student:
    def __init__(self, roll_number, name, branch, marks):
        self.roll_number = roll_number
        self.name = name
        self.branch = branch
        self.marks = marks
    def calculate_grade(self):
        if self.marks>=90:
            return 'A'
        elif self.marks>=75:
            return 'B'
        elif self.marks>=60:
            return 'C'
        else:
            return 'D'
    def display_details(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
roll_number = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
branch = input("Enter Branch: ")
marks = int(input("Enter Marks: "))
student = Student(roll_number, name, branch, marks)
print("\nStudent Details:")
student.display_details()