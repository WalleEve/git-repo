# Plot the Scatter chart Scatter, or xy charts are similar to the some line charts.
# For plotting the Scatter chart on an excel sheet, use ScatterChart class
# from openpyxl.chart submodule

import openpyxl 

from openpyxl.chart import ScatterChart, Reference, Series 


# call a workbook function fo openpyxl 
# to create a new blank Workbook object 

wb = openpyxl.Workbook()

# Get worksheet active sheet
# from the active attribute 

sheet = wb.active 

rows = [
    (14, 12200, 15),
    (20, 60000, 33),
    (18, 24400, 10),
    (22, 32000, 42)
]

# write content of each row in 1st 2nd and 3rd 
# column fo the active sheet respectively 

for row in rows:
    sheet.append(row)

# Create Object of StatterChart class 
chart = ScatterChart()

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

# Save the file 

wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_scatter_chart.xlsx')
