import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)
print(df.to_string())



x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())


x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

