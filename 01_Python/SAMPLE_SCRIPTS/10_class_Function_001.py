# VARIBALE LENGTH KEYWORD ARGUMENT 
# Variable Length keyword argument represent as ** 
# It should be the last argument in function
# Variable length key word argument will be store all the paramter values in a dictionary as KEy-VALYE pair

# Store 
# item name 
# price 
# discount perc 
import os 

os.system('cls')

def my_store( dict_p=2, **args): 
	total_paid = 0
	for key, value in args.items():
		print(f"Teem: {key}   Base Price: {value} DIcsount: {(value/100)*dict_p}  total: {value - ((value/100)*dict_p)}")
		total_paid += value - ((value/100)*dict_p)
	print(f"Total Amount to be paid: {total_paid}")




my_store(5, ac=40000, microwave=7000, iron=1700, washingmachine=15000, fridge=20000 )
#m y_store( ac=40000, microwave=7000, iron=1700, washingmachine=15000, fridge=20000 )
#my_store(dict_p=7, ac=40000, microwave=7000, iron=1700, washingmachine=15000, fridge=20000 )


def emi_cal(item_price, ten, roi):
