import pandas as pd
data = { 
    "Name": ['Ram',None,'sita','gita','babita','omakar','Anshuman','Shukhi','Rahul'],
    "age": [20,None,22,23,54,34,26,46,45],
    "Salary": [10000,None,30000,40000,50000,60000,70000,80000,90000],
    "Performance score":[86,None,88,89,90,91,92,93,94]
}
df = pd.DataFrame(data)
print(df.isnull().sum())
df['age'].fillna(df['age'].mean(),inplace=True)
print(df)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)