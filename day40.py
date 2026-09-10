#(how to merge)

import pandas as pd 
students= pd.DataFrame({
    "name":["Talha","Abdullah","ali"],
    "Class":["10th","9th","11th"]
})

marks=pd.DataFrame({
    "name":["Talha","Abdullah","ali"],
    "marks":[90,80,70]
})
merged=pd.merge(students,marks,on="name")
print(merged)