import pandas as pd
import math

def phi_coefficient(col1, col2):

	# col1, col2 should be dichotomous variables

	table = pd.crosstab(col1, col2, margins=True)

	a = table.iloc[0, 0]
	b = table.iloc[0, 1]
	c = table.iloc[1, 0]
	d = table.iloc[1, 1]
	r_1 = table.iloc[0, 2]
	r_2 = table.iloc[1, 2]
	c_1 = table.iloc[2, 0]
	c_2 = table.iloc[2, 1]

	phi_coefficient = (a * d - b * c) / math.sqrt(r_1 * r_2 * c_1 * c_2)

	print('\n Phi Coefficient =', round(phi_coefficient, 2))


"""Reading data"""

data = pd.read_csv("Sample 2.csv")

col1 = data['Gender']
col2 = data['Having diabetes']

"""Applying Phi Coefficient"""

phi_coefficient(col1, col2)

