#(Missing Data(drop)(fill))

import pandas as pd
df=pd.read_csv("sales_data_missing.csv")
print(df)
print(df.isnull())
print(df.dropna())
print(df.fillna(0))