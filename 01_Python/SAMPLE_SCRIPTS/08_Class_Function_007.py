# keyword argument
"""
def address(street, city, state,  pin, country='INDIA'):
    my_address = street + ' ' + city + ' '+ state + ' ' + country + ' '+str(pin)
    return my_address

my_address = address(street = "BBS", city="KHD", state = "ODISHA", pin=750001)

print(f" Key word Based Argument: {my_address}")

my_address = address("bbs", 'khorda', state = "ODISHA", pin=750001)
print(f" Mix arguments: {my_address}")

my_address = address("bbs", 'khorda', pin=750001, state = "ODISHA", )
print(f" Mix arguments: {my_address}")


# DEFAULT ARGUMENT

def full_name(first_name, middle_name, last_name, honor='Mr'):
    print(honor)


full_name('uma', 'sanker', 'palai')

"""
# 



# VARIBALE LENGTH ARGUMENT: *
#it will be store as tuple (1, 2, 3, 4, 5) []
"""
def address(*args):
    
    Fitsr_argument_value = args[0]
    Send_argument_value = args[1]
    Third_argument_value = args[2]
    Fourth_argument_value = args[3]
    Fifth_argument_value = args[4]
    
    return Fitsr_argument_value + ', '+Send_argument_value+', '+Third_argument_value+', '+Fourth_argument_value+', '+str(Fifth_argument_value)


fa_value = address("bbs", "khorda", "odisha", "india", 750001, "IN")
print(fa_value)


def address(*args):
    my_address = ''
    for i in args:
        my_address = my_address + str(i) + ' ,'

    return my_address
    


myAddress = address("bbs", "khorda", "odisha", "india", 750001, "IN")
print(f"My Address: {myAddress}")


def cal (*args):
    nResult = 0
    cResult = ''
    for i in args:
        i = str(i)
        if i.isdecimal():
            nResult = int(nResult) + int(i)
        else:
            cResult = cResult + i + ' '
    return nResult, cResult

nresult, cresult = cal('2', '3', 5, 6, 7, 89, '67', 'uma', "sanker", "palai")
print(f"Name: {cresult}  total: {nresult}")
"""
"""
# POSITIONAL ARGUMET
def f1(num1, num2):
    return num1 - num2
result = f1(30, 29) 
print(result) # 0 1 

# KEY WORD ARGUMENT
def f1(num1, num2):
    return num1 / num2

result = f1(num2 = 2, num1= 3)
print(result)


# DEFAULT ARGUMENT
def add(lane, city, dist, state, pin, contry = 'INDIA'):
    print(f"Lane: {type(lane)}")
    print(f"City: {type(city)}")
    print(f"Dist: {type(dist)}")
    print(f"State: {type(state)}")
    print(f"Country: {type(contry)}")
    print(f"Pin: {type(pin)}")
     
#myaddress = add('Bapuji Nagar', 'bhubaneswar', 'khorda', 'odisha', 750001)
#print(myaddress) #
myaddress = add(['Bapuji Nagar'], ('Bhubaneswar',), 'khorda', 'Odisha', 755022)
print(myaddress)

# VATIABLE LENGTH ARGUMENT
# *
# store as tuple


def add(*args):
    print(f"ARGS: {type(args)}")
    print(f"Lane: {type(args[0])}")
    print(f"City: {type(args[1])}")
    print(f"Dist: {type(args[2])}")
    print(f"State: {type(args[3])}")
    print(f"Country: {type(args[4])}")
    print(f"Pin: {type(args[5])}")
     
#myaddress = add('Bapuji Nagar', 'bhubaneswar', 'khorda', 'odisha', 750001)
#print(myaddress) #
myaddress = add(['Bapuji Nagar'], ('Bhubaneswar',), 'khorda', 'Odisha',755022)
print(myaddress)
"""
def add(*args):
    for i in args:
        print(type(i))

add(['Bapuji Nagar'])
        






# VARIABLE LENGTH KEY WORD ARGUMENT





















