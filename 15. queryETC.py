import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 29],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 75000]
}

df = pd.DataFrame(data)
print(df)

search = df.loc[df['Salary'] > 60000, ['Name', 'Salary']]
print(search)

find = df.iloc[1:4, 1:3]
print(find)


isinFn = df[df['Department'].isin(['HR', 'Finance'])]
print(isinFn)

isNotin = df[~df['Department'].isin(['IT'])]
print(isNotin)


betw = df[df['Age'].between(30, 40)]
print(betw)

nameA = df[df['Name'].str.startswith('A')]
print(nameA)

nameContainA = df[df['Name'].str.contains('a', case=False)]
print(nameContainA)

nLargest = df.nlargest(2, 'Salary')
print(nLargest)

nSmallest = df.nsmallest(3, 'Age')
print(nSmallest)