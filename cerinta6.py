import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def cerinta6(df):
	print("****Cerinta VI****")
	no_20_s = len(df[(df['Age'] < 21) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_40_s = len(df[(20 < df['Age']) & (df['Age'] < 41) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_60_s = len(df[(40 < df['Age']) & (df['Age'] < 61) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_max_s = len(df[(60 < df['Age']) & (df['Survived'] == 1) & (df['Sex'] == 'male')])
	no_males = len(df[(df['Sex'] == 'male')])
	print(f"Under 20: {no_20_s} survived, {len(df) - no_20_s} dead")
	print(f"21 - 40: {no_40_s} survived, {len(df) - no_40_s} dead")
	print(f"41 - 60: {no_60_s} survived, {len(df) - no_60_s} dead")
	print(f"60+: {no_max_s} survived, {len(df) - no_max_s} dead")
	p_20 = (no_20_s / no_males) * 100
	p_40 = (no_40_s / no_males) * 100
	p_60 = (no_60_s / no_males) * 100
	p_max = (no_max_s / no_males) * 100
	percentages = [p_20, p_40, p_60, p_max]
	age_groups = ['Under 20', '21 - 40', '41 - 60', '60+']
	plt.bar(age_groups, percentages, color ='maroon', width = 0.4)
	plt.xlabel("Age Groups")
	plt.ylabel("Survival Rate")
	plt.title("Survival rate among different age groups for males")
	plt.savefig('bar.png')
	plt.close()
	print("***************")
	print("")
pass