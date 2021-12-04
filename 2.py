import pandas

filename = "input_2"

data = pandas.read_csv(filename, delimiter=" ", header=None)

forward = data.where(data[0]=="forward")[1].sum()
up = data.where(data[0]=="up")[1].sum()
down = data.where(data[0]=="down")[1].sum()

depth = down - up
print(int(forward * depth))


aim = 0
pos_x = 0 
depth = 0
for index, row in data.iterrows():
    if row[0] == "forward":
        pos_x += row[1]
        depth += row[1] * aim
    elif row[0] == "up":
        aim -= row[1]
    elif row[0] == "down":
        aim += row[1]

print(int(depth * pos_x))