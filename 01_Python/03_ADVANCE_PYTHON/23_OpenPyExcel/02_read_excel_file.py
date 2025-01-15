# Program to read an excel file

import openpyxl

xlFile = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\Country Capital.xlsx"

# To Open the workbook
# workbook object is created

wb_obj = openpyxl.load_workbook(xlFile)

# Get workbook active sheet object
# from the active attribute

sheet_obj = wb_obj.active

# Cell objects alo have a row, column
# and coordinate attributes that provides
# location information for the cell.

# cell object is created by using sheet object's cell() method

cell_obj = sheet_obj.cell(row=1, column=1)

# print value of cell object
# using the value attribute

print(cell_obj.value)
