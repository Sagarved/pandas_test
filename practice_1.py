"""
Introduction to Series
Series is like column in table. It is one dimensional array holding data (any type).
"""
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

# If nothing else is specified, the values are labeled with their index number. First value has index 0.
print(myvar)

# Return the first value of the Series
print(myvar[0])

# # With the index argument, you can name your own labels.
myvar_with_index = pd.Series(a, index=["X", 0, "Z"])
print("Series with Index")
print(myvar_with_index)

# When you have created labels/Index, you can access an item by referring to the label.
print(f"Accessing element by index {myvar_with_index[0]}")
print(f"Accessing element by Label name {myvar_with_index['X']}") # This is a best practice to use call value by label

# Create a simple Pandas Series from a dictionary

weights = {'day1': 210, 'day2': 200, 'day3': 205}

myvar_from_dictionary = pd.Series(weights)

print(f"Series from a dictionary \n{myvar_from_dictionary}")
# Get value from a Series using a key/label
print(f"Series from a dictionary weight of day1: {myvar_from_dictionary['day1']}")

