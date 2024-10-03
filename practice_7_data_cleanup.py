"""
The mean is the average of all the values in a dataset.
It is calculated by summing up all the values and dividing by the number of values.
mean = average = sum[All values]/[No. of Values]

The median is the middle value in a sorted dataset.
If the dataset has an odd number of elements, it is the exact middle value.
If it has an even number of elements, it is the average of the two middle values.

The mode is the most frequent value in a dataset.
A dataset can have more than one mode if multiple values have the same highest frequency.
"""
import pandas as pd

dfdirty = pd.read_json("data/data.json")
# To find average or mean
average = dfdirty["Calories"].mean()
# make a copy of original datafreame
df_fill_calories = dfdirty.copy()
# fill average value in new dataframe of calories label
df_fill_calories["Calories"] = df_fill_calories["Calories"].fillna(average)
print(f"value of average calories {average:.10}")
print(df_fill_calories.info())


# Median is a central value
median_value = dfdirty["Calories"].median()
df_fill_calories_median = dfdirty.copy()
# df_fill_calories_median["Calories"] = df_fill_calories_median["Calories"].fillna(median_value)
# This would save in update in the same df
df_fill_calories_median["Calories"].fillna(median_value, inplace=True)
print(f"Average median value {median_value}")
print(df_fill_calories_median.info())

# Mode = the value that appears most frequently.
most_appeared = dfdirty["Calories"].mode()[0]
df_fill_calories_mode = dfdirty.copy()
df_fill_calories_mode["Calories"].fillna(most_appeared, inplace=True)
print(f"Mode value {most_appeared}")
print(df_fill_calories_mode.info())
