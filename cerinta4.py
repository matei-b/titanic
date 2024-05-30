import pandas as pd

def no_and_perc(df):
	NaN_columns = df.columns[df.isnull().any()]
	percentages = {}
	no_NaN_values = {}
	for i in NaN_columns:
		no_NaN_values[i] = df[i].isnull().sum()
		percentages[i] = (no_NaN_values[i] / len(df)) * 100
	return NaN_columns, percentages, no_NaN_values 

def cerinta4(df):
	print("****Cerinta IV****")
	NaN_columns, percentages, no_NaN_values = no_and_perc(df)
	NaN_columns.tolist()
	print("These are the columns containing null values and their number: ")
	for i in NaN_columns:
		print(f"{i}: {no_NaN_values[i]}")
	print()
	
	print("The percentages of null values:")
	for i in NaN_columns:
		print(f"{i}: {percentages[i]:.2f}%")
	print()

	survived_df = df[(df['Survived'] == 1)]
	NaN_columns, percentages, no_NaN_values = no_and_perc(survived_df)
	print("Percentages for survivors:")
	for i in NaN_columns:
		print(f"{i}: {percentages[i]:.2f}%")
	print()

	perished_df = df[(df['Survived'] == 0)]
	NaN_columns, percentages, no_NaN_values = no_and_perc(perished_df)
	print("Percentages for the perished:")
	for i in NaN_columns:
		print(f"{i}: {percentages[i]:.2f}%")
	print("***************")
	print("")
pass