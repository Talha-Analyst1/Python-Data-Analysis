import pandas as pd
df=pd.read_csv("sales_data.csv")
df=df.rename(columns={"Units_Sold":"Sold_Quantity"})
print(df)