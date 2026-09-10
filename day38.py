#practice pandas of .iloc and .loc

import pandas as pd
df=pd.read_csv("sales_data.csv")
print(df.iloc[0])
print(df.iloc[2])

print(df.loc[2, "Price"])