import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def cerinta6(df):
	no_20_s = len(df[(df['Age'] < 21) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_40_s = len(df[(20 < df['Age']) & (df['Age'] < 41) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_60_s = len(df[(40 < df['Age']) & (df['Age'] < 61) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_max_s = len(df[(60 < df['Age']) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_20 = len(df[(df['Age'] < 21)])
	no_40 = len(df[(20 < df['Age']) & (df['Age'] < 41)])
	no_60 = len(df[(40 < df['Age']) & (df['Age'] < 61)])
	no_max = len(df[(60 < df['Age'])])
	p_20 = (no_20_s / no_20) * 100
	p_40 = (no_40_s / no_40) * 100
	p_60 = (no_60_s / no_60) * 100
	p_max = (no_max_s / no_max) * 100
	percentages = [p_20, p_40, p_60, p_max]
	age_groups = ['Under 20', '21 - 40', '41 - 60', '60+']
	plt.bar(age_groups, percentages, color ='maroon', width = 0.4)
	plt.xlabel("Age Groups")
	plt.ylabel("Survival Rate")
	plt.title("Survival rate among different age groups for males")
	plt.savefig('bar.png')
pass