import pandas as pd

data={
    "Name":["Talha","Ahad","Ahme","Talha","Qari"],
    "City":["Lahore","Karachi","Multan","Lahore","Fsd"]
}
df=pd.DataFrame(data)
print(df.duplicated().sum())
print(df.drop_duplicates())