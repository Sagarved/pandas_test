"""
This is continue of dataframe practice
"""
import pandas as pd

data = {
    "weights": [210, 200, 205],
    "duration": ["day1", "day2", "day3"]
}
# Add a list of names to give each row a name:
myvar = pd.DataFrame(data, index=["Sanjay", "Raman", "Nita"])
print(myvar)

# Use the named index in the loc attribute to return the specified row(s).
print(f"Returning row 0 \n{myvar.loc['Sanjay']}") # this retuns a pandas Series?
print(f"Returning row 0 as DF \n{myvar.loc[['Sanjay']]}") # When using [], the result is a Pandas DataFrame.e

