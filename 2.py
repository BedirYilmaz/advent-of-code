import pandas

filename = "input_2"

data = pandas.read_csv(filename, delimiter=" ", header=None)

forward = data.where(data[0]=="forward")[1].sum()
up = data.where(data[0]=="up")[1].sum()
down = data.where(data[0]=="down")[1].sum()

depth = down - up
print(int(forward * depth))