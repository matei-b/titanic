import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def check_values_title(df):
	cnt = {}
	for i in df['Name']:
		aux = i.split(',')
		new_row = aux[1].split()[0]
		if (new_row in cnt) == False:
			cnt[new_row] = 0
		else:
			cnt[new_row] += 1
	return cnt

def create_title_list(df):
	name_list = []
	for i in df['Name']:
		name_list.append(i.split(',')[1].split()[0])
	return name_list

gender_of_titles = {
	'the Countess': 'female',
    'Miss' : 'female',
	'Capt' : 'male',
	'Mr' : 'male',
	'Jonkheer' : 'male',
	'Col' : 'male',
	'Master' : 'male',
	'Major' : 'male',
	'Sir': 'male',
	'Don' : 'male',
	'Rev' : 'male',
	'Mme' : 'female',
	'Mlle' : 'female',
	'Lady' : 'female',
	'Mrs' : 'male',
	'Dr' : 'female',
	'Ms' : 'female'
}

def what_gender(title):
	return gender_of_titles[title]

def cerinta9(df):
	df['Title'] = df.apply(lambda x: x['Name'].split(',')[1].split('.')[0].strip(), axis = 1)
	df['Title gender'] = df.apply(lambda x: gender_of_titles[x['Title']], axis = 1)
	titles = df['Title'].value_counts()
	plt.bar(titles.index, titles.values, color ='maroon', width = 0.4)
	plt.xticks(rotation = 90)
	plt.ylabel("Number of passengers")
	plt.savefig('bar_3.png')
	plt.close()
pass