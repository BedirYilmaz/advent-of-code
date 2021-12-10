import numpy as np
import pandas as pd

filename = "input_5"

data = pd.read_csv(filename, sep="->|,", header=None).astype(int)

data_vert_horz = data[(data[0]==data[2]) | (data[1]==data[3])]

ventures = np.zeros((1000,1000))
for index, row in data_vert_horz.iterrows():
    if row[0]==row[2]:
        if row[3]>row[1]:
            ventures[row[0], row[1]:row[3]+1] += 1
        else:
            ventures[row[0], row[3]:row[1]+1] += 1
    if row[1]==row[3]:
        if row[2]>row[0]:
            ventures[row[0]:row[2]+1, row[1]] += 1
        else:
            ventures[row[2]:row[0]+1, row[1]] += 1

print(ventures[ventures>=2].shape)


