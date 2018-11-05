import pandas as pd

csv = pd.read_csv("test.csv")
print(csv.head())

# data = csv.head()
# data.to_excel("excel.xlsx")

read = pd.read_excel('excel.xlsx', 0, index_col='c')
print(read.dtypes)
print(read.head())
