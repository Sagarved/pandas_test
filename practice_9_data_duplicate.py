"""
Duplicate rows are rows that have been registered more than one time.

"""

import pandas as pd

dfdirty = pd.read_json("data/data.json")

# Create a duplicate of the row at index 1
duplicate_row = dfdirty.loc[[4]]  # Get the row at index 4
# print(duplicate_row.head())
print(dfdirty.shape, dfdirty.tail())
# Append the duplicate row to the DataFrame
dfdirty = pd.concat([dfdirty, duplicate_row], ignore_index=True) #dfdirty.concat(duplicate_row, ignore_index=True)

print("\nAfter duplicate and concat of the last row")
print(dfdirty.shape, dfdirty.tail()) # Shape shows total number 170 and tail show index as 169 as it starts from 0.
# This behavior is the same as length function on list. It will give total number on the list and index starts from 0.

# print(dfdirty.head())
# print(dfdirty.duplicated().to_string())

# check individual row and verify if duplicate is true
# Steps: .duplicated(False)[dfdirty_index] gives boolean if it is True it is duplicated
# There are more than one duplicates in the given data.json. So without concat of duplication in line 15 we can run this.
n = 0
for dfdirty_index in dfdirty.index:
    if dfdirty['Calories'].duplicated(False)[dfdirty_index] == True:
        if n == 0:
            print(dfdirty.loc[[dfdirty_index]]) # Show the header on every line
        print('       '.join(dfdirty.loc[[dfdirty_index]].to_string(header=False).split()))  # Show no header on every line

        n += 1
print(f"Total repeat {n}")

