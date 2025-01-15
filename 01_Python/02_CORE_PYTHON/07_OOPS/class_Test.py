class Test:
    """
    This class is created by sayed for test the self  
    self is not a key word, we can use any name instead of self, but to use self is recommended 
    """

    def __init__(kelf):
        print("Constructor, id of kelf is: ", id(kelf))

t = Test() 
print(id(t))

print()
class Test2:
    def __init__(kelf, name, age):
        kelf.name = name     
        kelf.age = age 
        print("id of kelf: ", id(kelf))

    def talk(self):
        print("my name is: ", self.name)
        print("my age is: ", self.age)
        print("id of self: ", id(self))

t2 = Test2("sayed", 30)
t2.talk() 



class Test3:
    def __init__(self):
        print("Constructor:")

Test3() # We can create an object of a class without reference variable but we can not use that object or we can not access properties of that object.

# When even we create an object constructot will get executed automatically all variable in a constructor will initialized in memmory.

