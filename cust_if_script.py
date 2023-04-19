#!/usr/bin/env python3
"""Alta3 Research | PhantumFury68
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Lookup the Letter grade for a given score '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your Numeric Score?"))

# if input value was higher or equal to 90
if connection >= 90:
    message = message + 'Your grade is an A.'
elif connection >= 80:
    message = message + 'Your grade is an B.'
elif connection >= 70:
    message = message + 'Your grade is an C.'
elif connection >= 60:
    message = message + 'Your grade is an D.'
else:
    message = message + 'Your grade is an F.'
print(message)
