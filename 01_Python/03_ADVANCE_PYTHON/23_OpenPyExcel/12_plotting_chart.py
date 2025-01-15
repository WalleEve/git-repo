# Plot the Bar Chart for plotting the bar char on an excel sheet, use BarChart
# class from openpyxl.chart submodule.

import openpyxl 
from openpyxl.chart import BarChart, Reference 

wb = openpyxl.Workbook()

sheet = wb.active 

#write 0 to 9 in 1st column fo the active sheet
for i in range(10):
    sheet.append([i])

# create data for plotting 
values = Reference(sheet, min_col = 1, min_row=1, max_col=1, max_row=10)

# create object of BarChar class 

chart = BarChart()

# adding data to the Bar chart object 
chart.add_data(values)

# set the title of the chart 
chart.title = "BAR-CHART"

# set the title of the x-axis 
chart.x_axis.title = "X_AXIS"

# set the title of the y-axis 
chart.y_axis.title = "Y_AXIS"

# Add chart to the sheet 
# the top-left corner of a chart
# is anchored to cell E2.

sheet.add_chart(chart, "E2")

# save the file 
wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_bar_chart.xlsx')