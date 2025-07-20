# Updated Student Management

import json

# --- Base Class ---

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# --- Student Class ---

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id
        self.courses = {}    # Course name: grade

        def enroll(self, course):
            if course not in self.courses:
                self.course[course] = None
                print(f"{self.name} enrolled in {course}")
            else:
                print(f"{self.name} is already enrolled in {course}")

        def add_grade(self, course, grade):
            if course in self.courses:
                self.courses[course] = grade
                print(f"Grade added for {self.name} in {course}: {grade}")
            else:
                print(f"{self.name} is not enrolled in {ourse}")

        def show_info(self):
            super().show_info()
            print(f"Student ID: {self.__student_id}")
            if self.courses:
                for course, grade in self.courses.items():
                    grade_ste = grade if grade is not None else "Not graded"
                    print(f"  Course: {course}, Grade: {grade_str}")

            else:
                print("No courses enrolled")

        def get_id(self):
            return self.__student_id

        def to_dict(self):
            return {
                "name": self.name,
                "age": self.age,
                "student_id": self.__student_id,
                "cources": self.cources
            }


        @staticmethod
        def from_dict(data):
            s = Student(data["name"], data["age"], data["student_id"])
            s.cources = data["cources"]
            return s

# --- Teacher Class ---

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Subject Taught: {self.subject}")


# --- School Class ---

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student: {student.name}")

    def remove_student(self, student_id):
        for s ini self.students:
            if s.get_id() == student_id:
                self.students.remove(s)
                print(f"Removed Student ID {student_id}")
                return
        print(f"Student ID {student_id} not found.")

    def show_all_students(self):
        print("\n--- Student List ---")
        for student in self.students:
            student.show_info()
            print()

    def save_to_file(self, filename):
        data = [s.to_dict() for s in self.students]
        with open(filename, "w") as f:
            json.dump(data, f)
        print(f"Student data saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") asa f:
                data = json.load(f)
            self.student = [Student.from_dict(d) for d in data]
            print(f"Student data loaded from {filename}")
        except FileNotFoundError:
            print(f"No File found: {filename}")


# Create a school instance
school = School()

# Pre-defined admin and teacher login info
admin_username = "admin"
admin_password = "1234"

teachers = {
    "smith": {"password": "math123", "subject": "Math"},
    "lee": {"password": "science123", "subject": "Science"}
}

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. Save Data")
        print("5. Load Data")
        print("0. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            sid = input("Enter student ID: ")
            student = Student(name, age, sid)
            school.add_student(student)

        elif choice == "2":
            sid = input("Enter student ID to remove: ")
            school.remove_student(sid)

        elif choice == "3":
            school.show_all_students()

        elif choice == "4":
            school.save_to_file("students.json")

        elif choice == "5":
            school.load_from_file("students.json")

        elif choice == "0":
            break
        else:
            print("Invalid choice")

def teacher_menu(teacher_name, subject):
    while True:
        print(f"\n--- Teacher Menu ({teacher_name.title()} - {subject}) ---")
        print("1. Assign Grade")
        print("2. View All Students")
        print("0. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter student ID: ")
            course = subject
            grade = input(f"Enter grade for {course}: ")

            found = False
            for student in school.students:
                if student.get_id() == sid:
                    student.enroll(course)
                    student.add_grade(course, grade)
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == "2":
            school.show_all_students()

        elif choice == "0":
            break
        else:
            print("Invalid choice")

# --- Main Login Menu ---
def main_menu():
    while True:
        print("\n📚 Welcome to Student Management System")
        print("1. Admin Login")
        print("2. Teacher Login")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Admin Username: ")
            password = input("Admin Password: ")
            if username == admin_username and password == admin_password:
                admin_menu()
            else:
                print("Invalid admin credentials!")

        elif choice == "2":
            username = input("Teacher Username: ")
            password = input("Password: ")
            if username in teachers and teachers[username]["password"] == password:
                teacher_menu(username, teachers[username]["subject"])
            else:
                print("Invalid teacher credentials!")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run the program
main_menu()
