# Determine Total Number of Columns

# importing openpyxl module

import openpyxl


xlFile = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\Country Capital.xlsx"


# workbook object

wb_obj = openpyxl.load_workbook(xlFile)

# sheet Object

sheet_obj = wb_obj.active

# print total number of columns

print(sheet_obj.max_column)
