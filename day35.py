#(pandas library)

import pandas as pd
data={
      "product":["Laptop","Computer","Tablet"],
       "price":[80000, 7500 ,60000 ],
       "stock":[10,20,50]
}
df=pd.DataFrame(data)
print(df)


import pandas as pd
data={
    "Students":["Ahad","Ahmed","Uzair"],
    "fee":[8000,9000,8900],
    "Grade":["A","B","C"]
}
df=pd.DataFrame(data)
print(df)