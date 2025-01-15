file_name = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\PythonDemoProjects\\test_tile.txt"
with open (file_name, 'w') as f:
    f.write('Srno                name                Age')
    f.write("\n---------------   ------------------  -------")
    name = input("Enter Name: ")
    age = int(input("Age: "))
    wstring = str(1) + ' ' * (len('------------------') - len(str(1))+2) +name+' ' * (len('------------------') - len(name)+2) +str(age)
    f.write('\n'+wstring)
