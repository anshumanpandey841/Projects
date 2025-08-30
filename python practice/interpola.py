import pandas as pd
data = {
    "Time": [1,2,3,4,5,6,7],
    "Value": [5,None,30,None,50,55,None] 
}
df = pd.DataFrame(data)
print("before interpolation")
print(df)
print("after interpolation")
df["Value"] = df["Value"].interpolate(method="linear")
print(df)