import pandas as pd

df = pd.read_csv("sales_data.csv")

sorted_df = df.sort_values("Price", ascending=False)

sorted_df.to_csv("sorted_sales.csv", index=False)
print("File saved!")