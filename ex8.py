#!/usr/bin/env python3
# Script: Printing Printing
# Author: Zachary Derrick                    
# Date of latest revision:  2023-4-20    
# Purpose: Do a more complicated formatting of a string.

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))