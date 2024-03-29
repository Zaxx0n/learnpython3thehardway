#!/usr/bin/env python3
# Script: Variables and Names
# Author: Zachary Derrick                    
# Date of latest revision:  2023-4-3    
# Purpose: Now you can print things with print and you can do math. The next step is to learn about variables. In
# programming, a variable is nothing more than a name for something, similar to how my name ”Zed” is
# a name for, ”The human who wrote this book.” Programmers use these variable names to make their
# code read more like English and because they have lousy memories. If they didn’t use good names for
# things in their software, they’d get lost when they tried to read their code again.

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are ", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")