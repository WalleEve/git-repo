# import openpyxl module
import openpyxl
 
# import PieChart, Reference class
# from openpyxl.chart sub_module
from openpyxl.chart import PieChart, Reference
 
# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
wb = openpyxl.Workbook()
 
# Get workbook active sheet
# from the active attribute.
sheet = wb.active
 
datas = [
    ['Pie', 'Sold'],
    ['Apple', 50],
    ['Cherry', 30],
    ['Pumpkin', 10],
    ['Chocolate', 40],
]
 
# write content of each row in 1st, 2nd and 3rd
# column of the active sheet respectively .
for row in datas:
    sheet.append(row)
 
# Create object of PieChart class
chart = PieChart()
 
# create data for plotting
labels = Reference(sheet, min_col = 1,
                   min_row = 2, max_row = 5)
                    
data = Reference(sheet, min_col = 2,
                   min_row = 1, max_row = 5)
 
# adding data to the Pie chart object
chart.add_data(data, titles_from_data = True)
 
# set labels in the chart object
chart.set_categories(labels)
 
# set the title of the chart
chart.title = " PIE-CHART "
 
# add chart to the sheet
# the top-left corner of a chart
# is anchored to cell E2 .
sheet.add_chart(chart, "E2")
 
# save the file
wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_pie_chart2.xlsx')