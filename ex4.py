# Number of available cars
cars = 100
# Number of available seats in each car
space_in_a_car = 4
# Number of available car drivers
drivers = 30
# Number of passengers
passengers = 90
# Cars that can't be driven = number of cars - number of drivers
cars_not_driven = cars - drivers
# Cars that can be driven = number of drivers
cars_driven = drivers
# Total number of passengers that can be transported
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."