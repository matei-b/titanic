import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def age_group(age):
	if age < 21:
		return 'Under 20'
	elif (20 < age) & (age < 41):
		return '21 - 40'
	elif (40 < age) & (age < 61):
		return '41 - 60'
	elif 60 < age:
		return '60+'

def cerinta5(df):
	no_20 = len(df[(df['Age'] < 21)])
	no_40 = len(df[(20 < df['Age']) & (df['Age'] < 41)])
	no_60 = len(df[(40 < df['Age']) & (df['Age'] < 61)])
	no_max = len(df[(60 < df['Age'])])
	df_aux = df
	df_aux['Age Group'] = df_aux['Age'].apply(age_group)
	data = [no_20, no_40, no_60, no_max]
	keys = ['Under 20', '21 - 40', '41 - 60', '60+']
	palette_color = seaborn.color_palette('bright') 
	plt.pie(data, labels=keys, colors=palette_color, autopct='%.2f%%') 
	plt.savefig("ages_g.png")
	plt.close()
	print(df)
pass