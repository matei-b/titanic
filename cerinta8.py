import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def cerinta8(df):
	df_s = df[df['Survived'] == 1]
	df_p = df[df['Survived'] == 0]
	for i in df.columns:
		if (df_s[i].dtype.kind in 'biufc') == True :
			df_s[i].fillna(df_s[i].mean(), inplace = True)
		if (df_p[i].dtype.kind in 'biufc') == True :
			df_p[i].fillna(df_p[i].mean(), inplace = True)
		if (df_s[i].dtype.kind in 'biufc') == False :
			df_s[i].fillna(df_s[i].mode()[0], inplace = True)
		if (df_p[i].dtype.kind in 'biufc') == False :
			df_p[i].fillna(df_p[i].mode()[0], inplace = True)
	df.fillna(df_s, inplace = True)
	df.fillna(df_p, inplace = True)
	df.to_csv('df_filled.csv')
pass