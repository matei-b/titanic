import pandas as pd

def cerinta1(df):
	print(f"The number of columns is: {len(df.columns)}")
	print(f"The number of rows is: {len(df)}")
	print("The data types of the columns are:")
	print(df.dtypes)
	print("The number of null values in each column is:")
	print(df.isnull().sum())
	print(f"The number of duplicated rows is: {df.duplicated().sum()}")
pass