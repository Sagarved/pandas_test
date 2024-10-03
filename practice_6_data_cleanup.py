"""
Data cleaning means fixing bad data in your data set.
Bad data could be:

* Empty cells
* Data in wrong format
* Wrong data
* Duplicates
"""

# Empty cell can be providing wrong analysis.
# Empty row and Nan, NAN is the same. It means cell is empty.
# To avoid this pitfall one should remove rows with empty cell if it is OK

import pandas as pd

dfdirty = pd.read_json("data/data.json")
df_no_empty = dfdirty.dropna()
print(df_no_empty.info())

"""
Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
If you want to change the original DataFrame, use the inplace = True argument:
"""
dfdirty.dropna(inplace=True)
print("This is inplace information")
print(f"{dfdirty.info()}")

"""
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:
"""
dffill_value = pd.read_json("data/data.json")
dffill_value.fillna(1, inplace=True)
print(dffill_value.info())


"""
Replace Only For Specified Columns
The example above replaces all empty cells in the whole Data Frame.
To only replace empty values for one column, specify the column name for the DataFrame:
"""
# Replace NULL values in the "Calories" columns with the number 100:
df_clean_calories = dfdirty["Calories"].fillna(100)
print(df_clean_calories.info())
