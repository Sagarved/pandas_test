"""
This is to read and write csv file using pandas
"""
import pandas as pd

df = pd.read_csv('data/powerball_python.csv')
# Show top rows from a df
# print(df.head())
print(df.shape)

# # use to_string() to print the entire DataFrame.
# print(df.to_string())
#
# # If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows.
# print(df)

# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(f"Maximum Rows set to: {pd.options.display.max_rows}")

# You can change the maximum rows number with the same statement options.display.max_rows
pd.options.display.max_rows = 100000
df2 = pd.read_csv('data/powerball_python.csv')

print(df2)

