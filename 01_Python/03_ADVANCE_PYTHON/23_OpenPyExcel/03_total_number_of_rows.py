# Determine total number of rows

import openpyxl


xlFile = "C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\Country Capital.xlsx"


# to open the workbook
# workbook object is created

wb_obj = openpyxl.load_workbook(xlFile)

sheet_obj = wb_obj.active

# print the total number of rows
print(sheet_obj.max_row)
