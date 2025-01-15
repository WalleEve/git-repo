# PLOT THE BUBBLE CHART.
# Bubble charts are similar to scatter charts but use a third dimension to deretmine
# the size of the bubbles. 
# Charts can include multiple series.
# For plotting the bubble chart on an excel sheet, 
# use BubbleChart class from openpyxl.chart submodule 

import openpyxl 

# import BubbleChart, Referece, Series class from openpyxl.chart sub-module 
from openpyxl.chart import BubbleChart, Reference, Series

# call a Workbook() function of openpyxl
# to create a new blank Workbook object 
wb = openpyxl.Workbook()

# get the workbook active sheet from the active attribute.

sheet = wb.active 

rows = [
    (14, 12200, 10),
    (20, 60000, 10),
    (18, 24400, 10),
    (22, 32000, 10)
]

# write content of each row in 1st 2nd and 3rd 
# column fo the active sheet respectively 

for row in rows:
    sheet.append(row)

# Create Object of StatterChart class 
chart = BubbleChart()

# create data for plotting 

xValues = Reference(sheet, min_col=1, min_row=1, max_row=5)
yValues = Reference(sheet, min_col=2, min_row=1, max_row=5)
size = Reference(sheet, min_col=3, min_row=1, max_row=5)

print(xValues, yValues, size)


# create a 1st series of data 

series = Series(values = yValues, xvalues = xValues, zvalues = size, title="2023")

# add series data to the chart object 
chart.series.append(series)

# set the title of the chart 
chart.title = "SCATTER-CHART"

# set the title of the x-axis 
chart.x_axis.title = "X-AXIS"

# set the title of the y-axis 
chart.y_axis.title = "Y-AXIS"

# add chart to the sheet 

sheet.add_chart(chart, "E2")


# save the file 
wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_Bubble_chart.xlsx')