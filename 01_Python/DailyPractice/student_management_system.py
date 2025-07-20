# Student Management System Using Object-Oriented Programming in Python.
# Class & Object
# Inheritance
# Encapsulation
# Polymorphism
# Constructor

# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class: Student (inherits from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id  # Encapsulation
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def show_info(self):
        super().show_info()
        print(f"Student ID: {self.__student_id}")
        print("Course Enrolled: ", ", ".join(self.courses) if self.courses else "None")


# Derived class: Teacher (inherits from Person)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Subject Taught: {self.subject}")


# Manager class: School (manages student and teachers)
class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_all_people(self):
        print("\n---- Students -----")
        for student in self.students:
            student.show_info()

        print("\n---- Teachers -----")
        for teacher in self.teachers:
            teacher.show_info()


# Test the system

s1 = Student("ALice", 20, "S101")
s2 = Student("Bob", 21, "S102")
t1 = Teacher("Mr. Smith", 40, "Mathematics")

s1.enroll("Math")
s2.enroll("Science")

school = School()
school.add_student(s1)
school.add_student(s2)
school.add_teacher(t1)


school.show_all_people()
