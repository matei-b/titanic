import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def cerinta8(df):
	df_filled = df.groupby(['Survived', 'Age'])
	print(df_filled.count())
pass