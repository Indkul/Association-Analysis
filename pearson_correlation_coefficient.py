import pandas as pd
import scipy.stats

def pearson_correlation_coefficient(col1, col2):

	# col1 and col2 are numeric variables

	correlation_value = round(scipy.stats.pearsonr(col1, col2)[0], 2)

	print('\n Pearson\'s Correlation Coefficient =', correlation_value)


"""Reading data"""

data = pd.read_csv("Sample 1.csv")

col1 = data['PetalLength']
col2 = data['SepalLength']

"""Applying Pearson's Correlation Coefficient"""

pearson_correlation_coefficient(col1,col2)







