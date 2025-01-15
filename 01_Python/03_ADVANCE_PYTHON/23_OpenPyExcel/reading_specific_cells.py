# reading_specific_cells.py
xlFile = "D:\\RoadMap\\Python\\PythonDemoProjects\\billings\\items.xlsx"
from openpyxl import load_workbook
def get_cell_info(path):
    workbook = load_workbook(filename=path)
    sheet = workbook.active
    print(sheet)
    print(f'The title of the Worksheet is: {sheet.title}')
    print(f'The value of A2 is {sheet["A2"].value}')
    print(f'The value of A3 is {sheet["A3"].value}')
    cell_pointer = 'F4'
    cell = sheet[cell_pointer]
    print(f'The variable "cell" is {cell.value}')
    return cell.value
if __name__ == '__main__':
    value = get_cell_info(xlFile)
    print(f"Value: {value}")
   