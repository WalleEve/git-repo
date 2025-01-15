# Plot the Area chart for plotting the area chart on an excel sheet,
# use AreaChart class from the openpyxl.chart submodule 

import openpyxl 

# import AreaChart class from openpyxl.chart sub_module 

from openpyxl.chart import AreaChart, Reference

wb = openpyxl.Workbook()

sheet = wb.active 

for i in range(10):
    sheet.append([i])

values = Reference(sheet, min_col = 1, min_row = 1, max_col = 1, max_row=10)

# create object of AreaChart class 

chart = AreaChart()

chart.add_data(values)

# set the title of the chart 
chart.title = "AREA-CHART"

# set the title of the x-axix 

chart.x_axis.title = "X-AXIS"

# set the title of the y-axis 
chart.y_axis.title = "Y-AXIS"


# Ass chart to the sheet 
# the top-left corner of a chart
# is anchored to cell E2 
sheet.add_chart(chart, "E2")

# save the file
wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_area_chart.xlsx')
