import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()  # Remove Rows

print(new_df.to_string())

df.dropna(inplace = True) # Remove Rows but same dataframe

print(df.to_string())

replace = df.fillna(130, inplace = True) # Fill missing values with 130
print(replace.to_string())

specificCol = df.fillna({"Calories": 130}, inplace=True)
print(specificCol.to_string())