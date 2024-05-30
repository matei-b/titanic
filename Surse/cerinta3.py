import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
def cerinta3(df):
	data_survived = df['Survived']
	data_pclass = df['Pclass']
	data_age = df['Age']
	data_sibsp = df['SibSp']
	data_parch = df['Parch']
	data_fare = df['Fare']

	plt.hist(data_survived, bins=10, color='skyblue', edgecolor='black')
	plt.xlabel('Survivors')
	plt.ylabel('Number of passengers')
	plt.title('Histogram of Survivors')
	plt.savefig("survivors.png")
	plt.close()

	plt.hist(data_pclass, bins=10, color='skyblue', edgecolor='black')
	plt.xlabel('Class')
	plt.ylabel('Number of passengers')
	plt.title('Histogram of Class')
	plt.savefig("class_hist.png")
	plt.close()

	plt.hist(data_age, bins=100, color='skyblue', edgecolor='black')
	plt.xlabel('Age')
	plt.ylabel('Number of passengers')
	plt.title('Histogram of Age')
	plt.savefig("age.png")
	plt.close()

	plt.hist(data_sibsp, bins=10, color='skyblue', edgecolor='black')
	plt.xlabel('SibSp')
	plt.ylabel('Number of passengers')
	plt.title('Histogram of SibSp')
	plt.savefig("sibsp.png")
	plt.close()

	plt.hist(data_parch, bins=10, color='skyblue', edgecolor='black')
	plt.xlabel('Parch')
	plt.ylabel('Number of passengers')
	plt.title('Histogram of Parch')
	plt.savefig("parch.png")
	plt.close()

	plt.hist(data_fare, bins=60, color='skyblue', edgecolor='black')
	plt.xlabel('Fare')
	plt.ylabel('Number of passengers')
	plt.title('Histogram of Fare')
	plt.savefig("fare.png")
	plt.close()
pass