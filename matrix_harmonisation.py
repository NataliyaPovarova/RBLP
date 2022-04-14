import os
import pandas as pd

os.chdir('/Users/nataliapovarova/Desktop/Work/Python/harmonization')

matrix = pd.read_excel(io='sample_matrix.xlsx', sheet_name='SHEET')
elements = (list(matrix))[11:]
element_fan_ids = matrix['Questel unique family ID (FAN)'].tolist()


def parents(x, list):
    parents = []
    for i in list:
        if i != x:
            if str(x).startswith(str(i)):
                parents.append(str(i))
    return parents


for element in elements:
    for pos in range(len(element_fan_ids)):
        if pd.isnull(matrix.loc[pos, element]):
            pos += 1
        else:
            for parent in parents(element, elements):
                matrix.loc[pos, parent] = 1
matrix.to_excel("harmonized_matrix.xlsx", sheet_name='result')
