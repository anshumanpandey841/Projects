import pandas as pd
data = { 
    "Name": ['Ram','Syam','sita','gita','babita','omakar','Anshuman','Shukhi','Rahul'],
    "age": [20,21,22,23,54,34,26,46,45],
    "Salary": [10000,20000,30000,40000,50000,60000,70000,80000,90000],
    "Performance score":[86,87,88,89,90,91,92,93,94]
}
df = pd.DataFrame(data)
print(df)
print("name in single cloumn series")
print(df['Name'])
#selecting multiple coloumns
print("name and salary in multiple cloumn data frame")
subset = df[['Name','Salary']]
print(subset)