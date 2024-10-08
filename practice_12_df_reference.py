"""
This is for properties of df
"""
import pandas as pd

df = pd.read_json('data/data.json')
print(df.axes)  # The axes property returns a list with the row axis labels, and the column axis labels, in that order.

"""
[Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
       ...
       159, 160, 161, 162, 163, 164, 165, 166, 167, 168],
      dtype='int64', length=169), Index(['Duration', 'Pulse', 'Maxpulse', 'Calories'], dtype='object')]
"""

"""
The all() method returns one value for each column, True if ALL values in that column are True, otherwise False.
By specifying the column axis (axis='columns'), the all() method returns True if ALL values in that axis are True.
"""
print(df.all())  # Provides information about each column True or False.

# specific column
print(df["Duration"].all())

# One can change axis. It means instead of column all can treat each row as column
print(df.all(axis=1))


# aggregate of columns value
data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}

dfd = pd.DataFrame(data)
x_data = dfd.agg(["sum"])
print(x_data)

xrow_data = dfd.agg(["sum"], axis=1) # This will sum the value of row
print(xrow_data)
