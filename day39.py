#groupby functions
import pandas as pd
data={
    "city":["Lahore","Karachi","Islamabad"],
    "sales":[50000,90000,60000]
}
df=pd.DataFrame(data)
result=df.groupby("city")["sales"].sum()
print(result)


import pandas as pd

data = {
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Product": ["Laptop", "Mobile", "Headphones", "Smartwatch", "Tablet"],
    "Price": [75000, 35000, 3000, 8000, 20000]
}
df = pd.DataFrame(data)

result = df.groupby("Category")["Price"].sum()
print(result)