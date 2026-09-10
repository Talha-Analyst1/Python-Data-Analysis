#(pivot table)


import pandas as pd

data = {
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Product": ["Laptop", "Mobile", "Headphones", "Smartwatch", "Tablet"],
    "Price": [75000, 35000, 3000, 8000, 20000]
}
df = pd.DataFrame(data)

pivot = df.pivot_table(values="Price", index="Category", aggfunc="mean")
print(pivot)