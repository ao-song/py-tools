import pandas as pd

df = pd.read_csv('data.csv')
print(df['column_name'].value_counts())
