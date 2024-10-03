"""
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
"""
import pandas as pd

dfdirty = pd.read_json("data/data.json")
print(dfdirty.head(20))#dfdirty["date"])

# Adding value in duration column and row 5, value 45
dfdirty.loc[4, "Duration"] = 10000000
print(dfdirty.head(20))#dfdirty["date"])


"""For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
To replace wrong data for larger data sets you can create some rules, e.g. set some
boundaries for legal values, and replace any values that are outside of the boundaries.
"""
# If the value is higher than 120, set it to 120

for boundry in dfdirty.index:
    if dfdirty.loc[boundry, "Duration"] > 120:
        dfdirty.loc[boundry,"Duration"] = 120

print(f"After removing outlier {dfdirty.head(20)}")

