import pandas as pd
df=pd.read_csv("shop_data.csv")
print(df)
print(df.isna())
print(df.fillna(0))
value=df.sort_values("Price",ascending=False)
print(value)
expensive_values=df[df["Price"]>10000]
print(expensive_values)
df.to_csv("shop_data_clean.csv",index=False)
print("File_saved!")