"""
This is to read data from json file and stored into df
"""
import pandas as pd

# make df from json file
dfj = pd.read_json("data/data.json")
print(dfj.shape)

# print top lines in dfj
# print(dfj.head(10))

# print bottom lines in dfj
# print(f"Tail information\n{dfj.tail(10)}")

# print
# print(dfj.to_string())

# The DataFrames object has a method called info(), that gives you more information about the data set.
print(dfj.info())
"""
(169, 4)
<class 'pandas.core.frame.DataFrame'>
Index: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 6.6 KB
None
it seems like there are 164 of 169 Non-Null values in the "Calories" column.
Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values.
"""
