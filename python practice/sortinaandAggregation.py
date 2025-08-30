import pandas as pd
#sorting
data =  {
       'Name' : ["Aru","Varun","sesgy"],
       'Age'  : [23,45,42],
       'salary' : [10000,2000,200000]
}
df = pd.DataFrame(data)
print("without sorting")
print(df)
print("after sorting")
df.sort_values(by="salary",ascending=True, inplace=True)
print(df)
df.sort_values(by=="age",ascending=False, inplace=True)
print(df)