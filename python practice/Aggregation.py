import pandas as pd
data = {
    "Name" : ["akash","anime","Tanjiro","chump"],
    "Age" : [22,4,66,6,],
    "Score" : [60,45,87,99]
}
df= pd.DataFrame(data)
print(df)
df.sort_values(by="Age",ascending=True,inplace=True)
print(df)