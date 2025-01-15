from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass 

    def gun(self):
        print("This is AK-47")



class Army(DefenceForce):
    def area(self):
        print("This is operating from land!")


ay = Army()

ay.area()
ay.gun()
