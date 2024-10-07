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
dfdirty.plot()
dfdirty.show()
print(average)