l = (3, 5, 7, 2, 3, 4, 8)
sl = []

for i in range(0, len(l)):
    if len(sl) == 0:
        sl.append(l[i])
    else:
        for j in range(0, len(sl)):
            if l[i] <= sl[j]:
                sl.insert(j, l[i])
                break 
            else:
                if len(sl)-1 == j:
                    sl.append(l[i])
                else:
                    continue

print(tuple(sl))   # Sorted List

print(sl[::-1]) # Reverse Order


l = [4, 5, 2, 3]



def sort_list(l):
    sorted_list = []
    for i in range(0, len(l)):
        if len(sorted_list) == 0:
            sorted_list.append(l[i])
        else:
            print(l[i])
            for j in range(0, len(sorted_list)):
                if l[i]<=sorted_list[j]:
                    sorted_list.insert(j, l[i]) 
                    print(l[i], sorted_list[j])
                    break 
                else:
                    if j == len(sorted_list)-1:                        
                        sorted_list.append(l[i])
                        print(l[i])
                    else:
                        continue
    return sorted_list

sl = sort_list(l)
print(sl)



class A:
    def __init__(self):
        print("This is an object of the  class A")
    
    @staticmethod    
    def setter():
        name = 'sayed'
        phone = 9692392243
        return name, phone

class B(A):
    def __init__(self):
        print("This is an object of the class B")
        self.setter = super().setter

    def getter(self):
        print("This is the getter method from class B")
        #self.name, self.phone = super().setter()
        self.name, self.phone = self.setter()
        
        print(f"Name: {self.name} Phone: {self.phone}")


obj_b = B()
obj_b.getter()


a = 10 
b = 20.4 

if (a == int):
    print("int")

if (b == float):
    print("float")