import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

print(df.head(10))

print(df.tail()) 

print(df.tail(10)) 

print(df.info()) 