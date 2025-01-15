cars = 100 # It contains total no of cars
space_in_a_car = 4 # Space for the seating capacity
drivers = 30 # Total no of drivers available 
passengers = 90 # Total no of passengers 
cars_not_driven = cars - drivers  # No of cars for that no driver is availabe to drive
cars_driven = drivers # No of cars have Drivers to Drive
carpool_capacity = cars_driven * space_in_a_car # Total no of seating capacity
average_passengers_per_car = passengers / cars_driven # 


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven,"empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have to put about", average_passengers_per_car, "in each car")
