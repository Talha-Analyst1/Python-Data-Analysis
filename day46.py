import pandas as pd
df=pd.read_csv("shop_data.csv")
print(df["Price"].value_counts)