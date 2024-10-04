"""
A great aspect of the Pandas module is the corr() method.
The corr() method calculates the relationship between each column in your data set.
"""
import pandas as pd

dfdirty = pd.read_json("data/data.json")
print(dfdirty.corr())

"""
RESULT
Note: The corr() method ignores "not numeric" columns.
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922721
Pulse    -0.155408  1.000000  0.786535  0.025120
Maxpulse  0.009403  0.786535  1.000000  0.203814
Calories  0.922721  0.025120  0.203814  1.000000

* 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a 
value went up in the first column, the other one went up as well.
* 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
* -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
* 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
"""
print("This is for using different correlation method spearman")
print(dfdirty.corr(method="spearman"))
