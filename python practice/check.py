import pandas as pd
#read data from csv file
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print("dispalay inf0rmation about data frame")
print(df.info())