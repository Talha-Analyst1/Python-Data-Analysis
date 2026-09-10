#filtering through pandas

import pandas as pd
df=pd.read_csv("sales_data.csv")
best_sellers= df[df["Units_Sold"]>20]
print(best_sellers)