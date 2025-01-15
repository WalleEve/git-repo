# Variable length keyword argument 
""""
def dmat(dperc=2, **args): # dictionary
    total = 0 
    for key, value in args.items():
        print(f'Item: {key}  Item: Price: {value} Discount: {(value/100)*dperc} Item total Price: {value - (value/100)*dperc}')
        total +=value

    print(f"Total Paid: {total - (total/100)*dperc}")



    
   


dmat(10, rice=50, sugar=30)





item      price      disc      total
rice      50         5          45
sugar     30         3          27


grand total: 72 



school = 
student= sudent name:subject 
teacher= teac_name: subject  
admin= admin_name:dept 

"""

school = {
    'student':{'student_name': 'uma', 'subject': 'Java'},
    'teacher': {'teacher_name': 'Sadhana', 'subject': 'Java'},
    'admin': {'admin_name': 'sanker', 'dept': 'front desk'}
}


print(school)


st = school['student']
print(st['student_name'])


#print(f'{school[]}')









