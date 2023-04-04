#!/usr/bin/env python3
# Script: Variables and Names
# Author: Zachary Derrick                    
# Date of latest revision:  2023-4-3    
# Purpose: Now we’ll do even more typing of variables and printing them out. This time we’ll use something called
# a ”format string.” Every time you put " (double-quotes) around a piece of text you have been making a
# string. A string is how you make something that your program might give to a human. You print strings,
# save strings to files, send strings to web servers, and many other things.
# Strings are really handy, so in this exercise you will learn how to make strings that have variables em-
# bedded in them. You embed variables inside a string by using a special {} sequence and then put the
# variable you want inside the {} characters. You also must start the string with the letter f for ”format”,
# as in f"Hello {somevar}". This little f before the " (double-quote) and the {} characters tell Python
# 3, ”Hey, this string needs to be formatted. Put these variables in there.”
# As usual, just type this in even if you do not understand it, and make it exactly the same.

my_name = "Zak S. Derrick"
my_age = 43
my_height = 73 # inches
my_weight = 177 # pounds
my_eyes = "Hazel"
my_teeth = "White"
my_hair = "Brown"

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")