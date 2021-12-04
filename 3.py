import pandas

filename = "input_3"

data = pandas.read_csv(filename, dtype=str, header=None)

data_code = pandas.DataFrame(data[0].apply(list).tolist())

gamma_rate_list = []
for column in data_code:
    gamma_rate_list.append(data_code[column].mode()[0])

gamma_rate = int("".join(gamma_rate_list), 2)


epsilon_rate_list = []
for column in data_code:
    epsilon_rate_list.append(data_code[column].value_counts().index[-1])

epsilon_rate = int("".join(epsilon_rate_list), 2)

print(epsilon_rate * gamma_rate)