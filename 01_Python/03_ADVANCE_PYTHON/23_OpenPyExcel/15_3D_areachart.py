# PLot the 3D Area Chart for plotting the 3D Area chart on an excel 
# sheet, use the AreaChart3D class from openpyxl.chart submodule 

import openpyxl 

# importing AreaChart3D module from openpyxl.chart submodule 

from openpyxl.chart import AreaChart3D, Reference

wb = openpyxl.Workbook ()

sheet = wb.active 

# insert some sample data 
import random 

for i in range(10):
    sheet.append([random.randint(1, 10)])

# set up data for chart 
values = Reference(sheet, min_row=1, min_col=1, max_col=1, max_row=10)

# create an object for chart 

chart = AreaChart3D()

# adding data to the chart 

chart.add_data(values)

# set the chart title 
chart.title = "3D AREA-CHART"

# set the x-axis title 
chart.x_axis.title = "X-AXIS"

# set the y-axis title
chart.y_axis.title = "Y-AXIS"

# Add chart to the sheet 
# the top-left corner of a chart is anchored to cell E2 
sheet.add_chart(chart, "E2")


# save the workbook 
wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_3D_area_chart.xlsx')