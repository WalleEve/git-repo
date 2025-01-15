# Plot the 3D Bar Chart for plotting the 3D bar chart on an excel sheet,
# use BarChart3D class from openpyxl.chart submodule.

import openpyxl 

# import BarChart3D class from openpyxl.chart sub module 
from openpyxl.chart import BarChart3D, Reference

# write 0 to 9 in 1st column of the active sheet 
wb = openpyxl.Workbook()

sheet = wb.active

for i in range(10):
    sheet.append([i])


values = Reference(sheet, min_col = 1, min_row = 1, 
                        max_col = 1, max_row = 10)


# Create object of BarChart3D class 

chart = BarChart3D()

chart.add_data(values)

# set the title of the chart 
chart.title = "BAR-CHART"

# set the title of the x-axis 
chart.x_axis.title = "X AXIS"

# set the title of the y-axix 
chart.y_axis.title = "Y AXIX"

# Add chart to the sheet 
# the top-left cornor of a chart
# is anchored to cell E2 

sheet.add_chart(chart, "E2")

# Save the file 
wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_3D_bar_chart.xlsx')