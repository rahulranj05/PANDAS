import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 29],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 75000]
}

df = pd.DataFrame(data)

deptIT = df.query('Department == "IT"')
print(deptIT)

age30_fin = df.query('Age > 30 and Department == "Finance"')
print(age30_fin)

deptIThr = df.query('Department == "IT" or Department == "HR"')
print(deptIThr)


dept = 'HR'
deptHR = df.query('Department == @dept')
print(deptHR)
