# Plot a Line Chart. For plotting the Line chart on an excel sheet,
# use LineChart class from openpyxl.chart submodule 

import openpyxl 

from openpyxl.chart import LineChart, Reference
import random 

# create a new work book 

wb = openpyxl.Workbook()

# select the active sheet to work 

sheet = wb.active 

# imsert some sample data 

for i in range(10):
    sheet.append([random.randint(1, 10)])

# set values for chart 

values = Reference(sheet, min_row=1, min_col=1, max_row=10, max_col=1)

# create a chart object 

chart = LineChart()

# add data to the chart 

chart.add_data(values)

# set chart title 
chart.title = "LINE-CHART"

# set x-axix title 
chart.x_axis.title = "X-AXIS"

# set u-axis title 
chart.y_axis.title = "Y-AXIS"

# please chart in sheet 

sheet.add_chart(chart, "E2")

# save the workbook 
wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_line_chart.xlsx')