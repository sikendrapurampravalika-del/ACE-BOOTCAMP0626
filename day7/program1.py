import pandas as pd
student = {
    'name': ['pravalika', 'tapasi', 'indu', 'tejasri'],
    'Rollno': [12345, 12346, 12347, 12348],
    'Branch': ['csm', 'cse', 'iot', 'csd'],
    'City': ['c_abc', 'c_def', 'c_ghi', 'c_jkl'],
    'State': ['p_xyz', 'p_abc', 'p_def', 'p_ghi']
}
df = pd.DataFrame(student)
print(df)
print(df.shape)
print(df['Branch'])