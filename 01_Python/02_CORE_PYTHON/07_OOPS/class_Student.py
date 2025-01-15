class Student: # Class name should be in Camel Case 
    """ 
    This class is created by Sayed for the demo purposes
    """
    def __init__(self):  # __init__ is known as constructor It will executed automatically when ever we create an object 
        self.name = "Sayed"
        self.rollno = 101 
        self.marks = [60, 80, 94, 73]

    def talk(self):  # def talk() known as method of an object or class 
        print(f"My name is : {self.name}")
        print(f"My roll number is : {self.rollno}")
        print(f"My marks are : {self.marks}")
        



print(Student.__doc__) # Thsi is to view the class documentaon statements 
s = Student() # Object create for class student and reference s will hel us to access the functionality of Student object 
print(s.name)
print(s.rollno)
print(s.marks)
s.talk() 


s.name = "Mahfuze"
s.rollno = 102
s.marks = [56, 78, 80, 82]
s.add = "HYD" # It will not work 
print()
s.talk()

