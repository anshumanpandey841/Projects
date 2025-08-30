import pandas as pd
data = { 
    "Name": ['Ram','Syam','sita','gita','babita','omakar','Anshuman','Shukhi','Rahul'],
    "age": [20,21,22,23,54,34,26,46,45],
    "Salary": [10000,20000,30000,40000,50000,60000,70000,80000,90000],
    "Performance score":[86,87,88,89,90,91,92,93,94]
}
df = pd.DataFrame(data)
high_salary = df[df['Salary'] > 10000]
print(high_salary)
print("filter age greater than 25 and salary greater than 30000")
filetered = df[(df['age'] > 25) & (df['Salary'] > 30000)]
print(filetered)
filter_or = df[(df['age'] > 30) | (df['peformance score'] > 90)]
print("filtered age of the people grester then 30 or performance score greater than 90")
print(filter_or)