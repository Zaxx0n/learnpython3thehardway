#!/usr/bin/env python3
# Script: Variables and Names
# Author: Zachary Derrick                    
# Date of latest revision:  2023-4-4    
# Purpose: We will now type in a whole bunch of strings, variables, and formats, and print them. You will also
# practice using short abbreviated variable names. Programmers love saving time at your expense by
# using annoyingly short and cryptic variable names, so let’s get you started reading and writing them
# early on.

# defines the variable 'types_of_people' to being 10
types_of_people = 10
# creates a variable of an f-string that calls on the variable 'types_of_people'
x = f"There are {types_of_people} types of people."

# creates the variable 'binary'
binary = "binary"
# creates the variable 'do_not'
do_not = "don't"
# this is a variable that connects the previous two variables with an f-string
y = f"Those who know {binary} and those who {do_not}."

# prints the variable 'x'
print(x)
# prints the variable 'y'
print(y)
# prints an f-string that contains the variable 'x'
print(f"I said: {x}")
# prints an f-string that contains the variable 'y'
print(f"I also said: '{y}'")
# sets the variable 'hilarious' to 'False'
hilarious = False
# a variable that creates a string that contains curly brackets at the end
joke_evaluation = "Isn't that joke so funny?! {}"
# prints the variable 'joke_evaluation' and adds formatting to the end with the 'hilarious' variable
print(joke_evaluation.format(hilarious))
# sets variable 'w'
w = "This is the left side of..."
# sets variable 'e'
e = "a string with a right side."
# adds two variable/strings with the '+' symbol
print(w + e)