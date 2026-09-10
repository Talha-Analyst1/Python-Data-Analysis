#(sorting)
import pandas as pd
df=pd.read_csv("sales_data_missing.csv")
best_sellers=df.sort_values("Units_Sold")
print(best_sellers)

import pandas as pd
df=pd.read_csv("sales_data_missing.csv")
best_sellers=df.sort_values("Units_Sold", ascending=False)
print(best_sellers)