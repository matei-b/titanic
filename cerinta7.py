import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def cerinta7(df):
	print("****Cerinta VII****")
	no_passengers = len(df)
	no_u18 = len(df[(df['Age'] < 18)])
	no_o18 = len(df[(df['Age'] >= 18)])
	no_u18_s = len(df[(df['Age'] < 18) & (df['Survived'] == 1)])
	no_o18_s = len(df[(df['Age'] >= 18) & (df['Survived'] == 1)])
	p_u18 = (no_u18 / no_passengers) * 100
	print(f"This is the percentage of children on board: {p_u18:.2f}%")
	p_u18_s = (no_u18_s / no_u18) * 100
	p_o18_s = (no_o18_s / no_o18) * 100
	percentages = [p_u18_s, p_o18_s]
	age_groups = ['Under 18', 'Over 18']
	plt.bar(age_groups, percentages, color ='maroon', width = 0.4)
	plt.xlabel("Age Groups")
	plt.ylabel("Survival Rate")
	plt.title("Survival rate disparity between children and adults")
	plt.savefig('bar_2.png')
	plt.close()
	print("***************")
	print("")
pass