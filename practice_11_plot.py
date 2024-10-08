"""
This is for plotting various value from pandas dataframe.
Pandas uses the plot() method to create diagrams.
We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
"""

import pandas as pd
import matplotlib.pyplot as plt

dfdirty = pd.read_json("data/data.json")
# To find average or mean
average = dfdirty["Calories"].mean()

# To plot and show
dfdirty.plot() # Creates plot and storec it in the memory
plt.show() # show the stored plot
print(average)

# Plot with kind, and x, y axis
dfdirty.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

# Histogram chart, A histogram needs only one column.
# A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
dfdirty["Duration"].plot(kind='hist')
plt.show()
