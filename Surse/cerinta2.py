import pandas as pd
import matplotlib.pyplot as plt
import seaborn

def cerinta2(df):
	total_passengers = len(df)
	no_survivors = df['Survived'].sum()
	no_Iclass = len(df[(df['Pclass'] == 1)])
	no_IIclass = len(df[(df['Pclass'] == 2)])
	no_IIIclass = len(df[(df['Pclass'] == 3)])
	no_males = len(df[(df['Sex'] == 'male')])

	percentage_survivors = (no_survivors / total_passengers) * 100
	percentage_deaths = 100 - percentage_survivors
	percentage_Iclass = (no_Iclass / total_passengers) * 100
	percentage_IIclass = (no_IIclass / total_passengers) * 100
	percentage_IIIclass = 100 - percentage_Iclass - percentage_IIclass
	percentage_males = (no_males / total_passengers) * 100
	percentage_females = 100 - percentage_males
	
	data = [percentage_survivors, percentage_deaths]
	keys = ['Survivors', 'Perished']
	palette_color = seaborn.color_palette('bright') 
	plt.pie(data, labels=keys, colors=palette_color) 
	plt.savefig("suv.png")
	plt.close()

	data = [percentage_Iclass, percentage_IIclass, percentage_IIIclass]
	keys = ['First class', 'Second class', 'Third class']
	palette_color = seaborn.color_palette('bright') 
	plt.pie(data, labels=keys, colors=palette_color) 
	plt.savefig("class.png")
	plt.close()

	data = [percentage_males, percentage_females]
	keys = ['Males', 'Females']
	palette_color = seaborn.color_palette('bright') 
	plt.pie(data, labels=keys, colors=palette_color) 
	plt.savefig("sex.png")
	plt.close()
pass