# Available cars integer
cars = 100
# Available cars floating point
space_in_a_car = 4.0
# Available drivers
drivers = 30 
# Available passengers
passengers = 90
# Available cars
cars_not_driven = cars - drivers
# Unavailable cars
cars_driven = drivers
# Available capacity in carpool
carpool_capacity = cars_driven * space_in_a_car
# The average number of passengers needed to fill capacity
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")