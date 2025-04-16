import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 29],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 75000]
}

df = pd.DataFrame(data)
#print(df)


#Using Boolean Indexing

df_ITdept = df[df['Department'] == 'IT']
print(df_ITdept)

df_Age30 = df[df['Age'] > 30]
print(df_Age30)

df[(df['Age'] > 30) & (df['Department'] == 'Finance')]
df[(df['Department'] == 'IT') | (df['Department'] == 'HR')]




