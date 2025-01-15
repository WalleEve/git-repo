from openpyxl import Workbook 

path =  "D:\\Users\\MRaheman\\Desktop\\Practice\\"
file = "Products.xlsx"

destination_file = path + file 

wb = Workbook()

ws = wb.active 
ws.title = "Products"

column_headers = ["product_id", "product_name", "catagory", "brand", "measure_unit", "tax_catagory"]
mapping_letters = ['A', 'B', 'C', 'D', 'E', 'F']

if len(column_headers) != len(mapping_letters):
    print("Plese note that, mappping leeters should be same number as column_headers")
    print(list(zip(mapping_letters, column_headers )))
    
else:
    ndx = 1
    for i  in range(0, len(column_headers)):
        ws[mapping_letters[i]+str(ndx)] = column_headers[i]



wb.save(filename = destination_file)





