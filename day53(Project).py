import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("shop_data.csv")
plt.bar(df["Product"], df["Price"])
plt.title("product")
plt.xlabel("product")
plt.ylabel("price")
plt.show()