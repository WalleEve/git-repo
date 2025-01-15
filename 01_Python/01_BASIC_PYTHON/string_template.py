# 1.1.2: Templates

from string import Template

t = Template("Sayed is $x")
marks={'x':'100'}
print(t.substitute(marks))


t = Template("x is $x")
print(t.substitute({'x':100}))

Students = [('Sayed', 90), ('Sabeeha', 78), ('Eva', 99)]

t = Template("Hi $name, You have got $marks Marks")

for i in Students :
	print(t.substitute(name=i[0], marks=i[1]))

