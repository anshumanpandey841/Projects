import pandas as pd
data_1 = {
        "Name":['Aksh','laksh',"naitik","lori","maka"],
        "rollno":[1,2,3,4,5],
        
}

data_2 = {
    "rollno" :[1,2,3,11,5,6,7,8,9],
    "totalmarks" : [93,23,45,35,35,45,45,65,87]
}
df1 = pd.DataFrame(data_1)
df2 = pd.DataFrame(data_2)
merged = pd.merge(df1,df2,on="rollno",how="inner")
print("inner join")
print(merged)
merged1 = pd.merge(df1,df2,on="rollno",how='outer')
print("OUT?ER JOIN")
print(merged1) 
merged2 = pd.merge(df1,df2,on="rollno",how='right')
print("right join")
print(merged2)
