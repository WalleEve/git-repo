# Taz Kirana Store

"""
# Section 1:

@ Billing

srno    item    unit   unit_type  unit_price  total





----------------------------------------------------
tax
sub total
grand total



@ Employees

    @ Add New Employee
    id      name    gen    date_of_birth     phone      address       date_of_join      designation     salary



    @ View Employees
    id      name    gen    date_of_birth     phone      address       date_of_join      designation     salary




@ In House Stock

cod     item    brand       unit      sale_price



@ WareHouse Stock

cod     item    brand       unit        unit_price      order_Qty       cur_Qty



@ Reports

    @ shortage Stock Report
    item_code   item    brand   ordered_stock   current_stock   total_sale      prod_damage     total_purchages         total_sale      profit



    @ daily Sale Report
    date    item_code   item_name   total_sale  stock_price     sale_price      profit      tax_collected



"""
import openpyxl as pyxl
import datetime as dt    


class MyMart():
    """ This is Pilot Kirana Store Test Project"""
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.base_path = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\PythonDemoProjects\\ProjectKiranaStore\\"
        self.tDate = datetime.datetime.now()
        self.stock_house_XL = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\PythonDemoProjects\\ProjectKiranaStore\\STOCK_HOUSE_XL.xlsx"

    def stock_house:
        # user inputs 
        Flag = True 
        print("Do you want to insert new stock (Y/N)")
        uInput = input("> ")
        if uInput = 'Y' or uInput = 'y':
            while Flag:                  
                item    = input("Item Name: ")
                brand   = input("Item Brand: ")
                unit    = input("Item Unit: ")
                unit_price  = input("Unit Price $  ")

                # insert to the Excel

                print("\nDo you want to insert more: (Y/N)")
                uInput = input("n>")
                if uInput == 'n' or uInput == 'N':
                    break 


                
                



        else:
            return " Thank you!"







        
