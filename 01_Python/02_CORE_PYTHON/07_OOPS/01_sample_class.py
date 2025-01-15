class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_read = 0

    def descriptive_name(self):
        long_name = str(self.year)+ ' '+ self.make + ' '+ self.model
        return long_name

    def read_odometer(self):
        print("this car has " + str(self.odometer_read) + " miles on it")

    def update_odometer(self, miles):
        if miles >= self.odometer_read:
            self.odometer_read = miles
        else:
            print("Sorry can not rollback the Odometer.")
    def increase_odometer(self, miles):
        self.odometer_read += miles



class ElectricCar(Car):
    def __init__(selef, make, model, year):
        super().__init__(make, model, year)


my_car = ElectricCar("Tesla", "Model S", 2022)

my_car_model = my_car.descriptive_name()

print("I have purchesed {}".format(my_car_model))
