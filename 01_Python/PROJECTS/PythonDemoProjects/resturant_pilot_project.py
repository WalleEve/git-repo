# This is Restaurant management System Pilot Program
"""

# Section Need to be Developed
Step1: Billing Section
  @ Input Values
  Table No:      Number Of Person:         attendant no:
  srno          items         Quantity      unit price   total price
  -----     -------------     --------     ------------  -----------



  --------------------------------------------------------------------
  Tax
  Grand Total

Step2: Staff Section
@ Input Values
Name of the Employee:
Dob:
sex:
Address:
Phone:
Language:
Date of join:
Designation:
salary:

"""
import datetime
import sqlite3 as db 
import os 


class PilotRestaurant():
    """ This is a pilot restaurant project"""
    # Imports


    def __init__(self, name, cauisene):
        self.name = name
        self. cauisene = cauisene
        self.time = datetime.datetime.now()
    def billing(self):
        nid = 1
        wstring = ''
        new_t = ''
        space = ' '
        stotal = 0
        tax = 0
        for i in str(self.time):
            if i.isdigit():
                new_t+=str(i)
        table_no = int(input("Please Enter Table no: "))
        number_of_person = int(input("Number Of Person: "))
        attendant_no = int(input("Attendant no: "))
        file_name = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\PythonDemoProjects\\"+self.name+'_'+str(table_no)+'_'+str(number_of_person)+'_'+str(attendant_no)+'.txt'
        with open (file_name, 'w') as f:
            f.write(self.name)
            f.write('\n'+ self.cauisene)
            f.write('\n'+ str(self.time))
            f.write('\n'+'-'*63)
            wstring = f"Table No: {table_no}  Number Of Person: {number_of_person} Attendant no: {attendant_no}"
            f.write('\n'+wstring)
            f.write('\n'+'-'*63)
            wstring = "srno   | items            | Quantity | unit price | total price"
            f.write("\n"+wstring)
            f.write("\n"+'-'*len(wstring))
            while True:
                item = input("Item: ")
                quentity = int(input("Quantity:" ))
                uprice  = int(input("Price per unit: "))
                wstring = str(nid) + ' '*(7-len(str(nid))) +'| ' + item.title() + ' '*(18-len(item)-1) + '| ' + str(quentity) + ' '*(10-len(str(quentity))-1) + '| ' + str(format(uprice, '.2f')) + ' '*(12-len(str(uprice))-4)+ '| '  + str(format(quentity * uprice, '.2f'))
                nid +=1
                stotal += quentity * uprice
                tax += (stotal/100) * 18
                print(wstring)
                f.write('\n'+wstring)
                print("Do you want to insert more (Y/N)")
                flag = input("> ")
                if flag == 'N' or flag == 'n':
                    for i in range(0, 20-nid):
                        f.write("\n"+' '*7 +'|'+' '*18+'|'+' '*10+'|'+' '*12+'|')
                    f.write('\n'+'-'*63)
                    f.write('\nTax'+' '*(54-len(str(tax)))+ str(format(tax, '.2f')))
                    f.write('\nSub Total'+' '*(46-len(str(stotal)))+ str(format(stotal, '.2f')))
                    f.write('\nGrand Total'+' '*(44-len(str(stotal)))+ str(format(tax+stotal, '.2f')))
                    break

    def dbSetup(self):
        pass


    def new_employers(self):
        # For New Employer
        file_name = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\PythonDemoProjects\\"+self.name+'_'+'employers.txt'
        nid = 1
        with open(file_name, 'w') as ef:
            ef.write(self.name)
            ef.write("\nEmployers Details")
            ef.write('\n'+'-'*63)
            ef.write('\nName of the Employee'.upper() + ' '+
             'Dob'.upper() + ' ' +
             'Sex'.upper() +' ' +
             'Address'.upper() + ' ' +
             'Phone'.upper() +' ' +
             'Language'.upper() +' ' +
             'Date of join'.upper() +' ' +
             'Designation'.upper() + ' ' +
             'salary'.upper()
            )













my_rest = PilotRestaurant("Taz Restaurant", "Indian")

#my_rest.billing()
my_rest.new_employers()
