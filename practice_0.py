import pandas as pd

mydataset = {
  'cars': ["BMW", "tata", "Volvo", "Ford"],
  'passings': [3, 7, 2, 5]
}

myvar = pd.DataFrame(mydataset)

print(pd.__version__)
print(myvar)
