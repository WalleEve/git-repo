# Plot the Pie Chart,
# Pie charts plot the data as slices of a cercle with 
# each slice representing the percentage of the whole.
# Slices are plotted in a clockwise direction with 0deg being at the top of the cercle.
# Pie charts can only take a single series of data.
# For plotting the piechart on an excel sheet
# use PieChart class from openpyxl.chart submodule.

import openpyxl 

# import PieChart, Reference class

from openpyxl.chart import PieChart, Reference 

# create a new blank Workbook object 

wb = openpyxl.Workbook()

# get workbook active sheet 
sheet = wb.active 

datas = [	
	['Apple', 50],
	['Cherry', 30],
	['Pumpkin', 10],
	['Beans', 5],	
	['Tomato', 20]
]

# write contents of each row in 1st and 2nd
# column of the active sheet 

for row in datas:
	sheet.append(row)

# create object of PiChart class 
chart = PieChart()

# create data for plotting 

labels = Reference(sheet, min_col=1, min_row=1, max_row=5)
data = Reference(sheet, min_col=2, min_row=1, max_row=5)

# adding data to the Pie Chart object 

chart.add_data(data, titles_from_data=True)

# set lables in the chart object 

chart.set_categories(labels)

# set the title of the chart 
chart.title = "PIE-CHART"

# add chart to the sheet 

sheet.add_chart(chart, "E2")

# save the file 

wb.save('C:\\Users\\Sayed\\Desktop\\RoadMap\\Python\\23_OpenPyExcel\\plotting_pie_chart.xlsx')

