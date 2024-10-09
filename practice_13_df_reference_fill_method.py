"""
This file is for filling value in dataframe methods.
fillna

"""
import pandas as pd


# bfill Replace NULL values with the values from the next row:
dfdirty = pd.read_json("data/data.json")
print(f"shows dfdirty properties\n {dfdirty.describe()}")
print(f"shows top rows\n {dfdirty.head(20)}")

# In Calories column index 17 has a NaN we can use fillna with specific value as constant, mean, median or use bfill
# when use bfill, the bfill() method replaces the NULL values with the values from the next row.
dfdirty.bfill(inplace=True)
print(f"shows top rows after bfill\n {dfdirty.head(20)}") # One can see that row 17 has the same Calories as row 18


