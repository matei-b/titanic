import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def cerinta10(df):
	df_sib = df[(df['SibSp'] == 0) & (df['Parch'] == 0)]
	plt.hist(df_sib['Survived'], bins=10, color='skyblue', edgecolor='black')
	plt.xlabel('Survivors')
	plt.ylabel('Number of passengers')
	plt.title('Histogram of Survivors')
	plt.savefig("survivors.png")
	plt.close()

	df = df.head(100)
	sns.catplot(data=df, x = 'Pclass', y = 'Fare', hue = 'Survived', kind = 'swarm', size = 3)
	plt.savefig("CFS.png")
	plt.close()
pass