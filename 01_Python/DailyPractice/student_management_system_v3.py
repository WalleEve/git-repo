from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMessageBox
)
import sys

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = {}

    def enroll(self, course):
        self.courses[course] = None

    def add_grade(self, course, grade):
        if course in self.courses:
            self.courses[course] = grade

    def __str__(self):
        info = f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}\n"
        for course, grade in self.courses.items():
            info += f"  Course: {course}, Grade: {grade if grade else 'Not assigned'}\n"
        return info

class SchoolSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.students = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Student Management System (PyQt5)")
        self.setGeometry(100, 60, 1000, 800)

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        self.id_label = QLabel("Student ID:")
        self.id_input = QLineEdit()


        self.course_label = QLabel("Course:")
        self.course_input = QLineEdit()

        self.grade_label = QLabel("Grade:")
        self.grade_input = QLineEdit()

        self.add_button = QPushButton("Add Student")
        self.view_button = QPushButton("View Students")
        self.grade_button = QPushButton("Assign Grade")

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(self.course_label)
        layout.addWidget(self.course_input)
        layout.addWidget(self.grade_label)
        layout.addWidget(self.grade_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.grade_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.output)
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_student)
        self.view_button.clicked.connect(self.view_students)
        self.grade_button.clicked.connect(self.assign_grade)

    def add_student(self):
        name = self.name_input.text()
        age = self.age_input.text()
        sid = self.id_input.text()
        if not (name and age and sid):
            QMessageBox.warning(self, "Input Error", "Please fill in all student fields.")
            return
        try:
            age = int(age)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Age must be a number.")
            return
        student = Student(name, age, sid)
        course = self.course_input.text()
        if course:
            student.enroll(course)
        self.students.append(student)
        QMessageBox.information(self, "Success", f"Added student {name}.")
        self.clear_inputs()

    def assign_grade(self):
        sid = self.id_input.text()
        course = self.course_input.text()
        grade = self.grade_input.text()
        found = False
        for student in self.students:
            if student.student_id == sid:
                student.enroll(course)
                student.add_grade(course, grade)
                found = True
                break
        if found:
            QMessageBox.information(self, "Success", f"Grade {grade} assigned in {course}.")
        else:
            QMessageBox.warning(self, "Not Found", "Student ID not found.")
        self.clear_inputs()

    def view_students(self):
        if not self.students:
            self.output.setText("No students added.")
            return
        text = "\n".join(str(student) for student in self.students)
        self.output.setText(text)

    def clear_inputs(self):
        self.name_input.clear()
        self.age_input.clear()
        self.id_input.clear()
        self.course_input.clear()
        self.grade_input.clear()

def run_app():
    app = QApplication(sys.argv)
    window = SchoolSystem()
    window.show()
    sys.exit(app.exec_())

run_app()
