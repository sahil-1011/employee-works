import pandas as pd

data = pd.read_csv("C:/Users/HP/Desktop/EDA/Pandas/Employee works/sample.csv")
# read the data from csv file
df = pd.DataFrame(data)
# convert into data structure
print(df)

print(df.describe())

print(df.head())

# employee.ipynb  -- integrated python notebook >> jupyter notebook