import pandas as pd
data = { 
    "Name": ['Ram','Syam','sita','gita','babita','omakar','Anshuman','Shukhi','Rahul'],
    "age": [20,21,22,23,54,34,26,46,45],
    "Salary": [10000,20000,30000,40000,50000,60000,70000,80000,90000],
    "Performance score":[86,87,88,89,90,91,92,93,94]
}
df = pd.DataFrame(data)
print(pd)
df["Salary"] = df["Salary"] * 0.1 + df["Salary"]
print("Salary After Incrmeenting 10 percent")
print(df)
print("Salary after updating the specicfic person i.e. Syam ")
df.loc[1,"Salary"] = 45000
print(df)
df.insert(0,"Employee_id",[1,2,3,4,5,6,7,8,9])
print(df)
print("data after removing coloumn")
df.drop(columns=["Employee_id","age"],inplace=True)
print(df)
