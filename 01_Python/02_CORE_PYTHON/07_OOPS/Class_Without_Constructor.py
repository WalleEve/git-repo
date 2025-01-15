class Test:
    def m1(self, name, add, roll):
        self.name = name 
        self.add = add 
        self.roll = roll     
        print(f"dtls: {self.name}, {self.add}, {self.roll}")

r1 = Test() 

r1.m1("sayed", "hyd", 101) 


class Test2:
    def m1(self, name, add, roll):     
        print(f"dtls: {name}, {add}, {roll}")

    def m2(self, name):
        print(f"My name is: {name}")

r2 = Test2() 

r2.m1("sayed", "hyd", 101)
r2.m2("sayed") 



class Test3:
    def __init__(self, name):
        self.name = name 

    def m1(self):
        print("my name is ", self.name) 
        
t = Test3("Eva") 
print(t.name)

t.__init__("sayed") # Re-initialization of the constructor instance variable 
print(t.name)

t.m1()


    