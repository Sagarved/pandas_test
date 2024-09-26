"""
This is a dataframe practice
Datasets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table.
"""
import pandas as pd

data = {
    "weights": [210, 200, 205],
    "duration": ["day1", "day2", "day3"]
}

myvar = pd.DataFrame(data)
# Each keys in the data is referred as column name and values can be as rows on a table.
print(myvar)

# Pandas use the loc attribute to return one or more specified row(s)
print(f"Returning row 0 \n{myvar.loc[0]}") # this retuns a pandas Series?
print(f"Returning row 0 and 1 \n{myvar.loc[[0,1]]}") # When using [], the result is a Pandas DataFrame.e
print(f"Returning row 0 as DF \n{myvar.loc[[0]]}") # When using [], the result is a Pandas DataFrame.e

