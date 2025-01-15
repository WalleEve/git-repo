class Student:
    """
    This class is created by sayed for demo purposes 
    """
    def __init__(self, name, rollno, marks):
        self.name = name 
        self.rollno = rollno 
        self.marks = marks 
        
    def talk(self):
        print("My name is: ", self.name) 
        print("My rollno is: ", self.rollno) 
        print("My marks are: ", self.marks)  

s = Student("sayed", 101, [60, 89, 90])
s.talk() 

s2 = Student("Mahfuze", 102, [80, 78, 89])
s2.talk() 

