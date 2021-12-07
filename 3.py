import pandas

filename = "input_3"
# filename = "sample_input_3"

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

data_code_for_oxy = pandas.DataFrame(data[0].apply(list).tolist())

for column in data_code_for_oxy:
    most_common_bit = data_code_for_oxy[column].mode()[0]
    selected_rows = data_code_for_oxy.where(
        data_code_for_oxy[column] == most_common_bit
    ).dropna()

    rows_with_1 = data_code_for_oxy.where(data_code_for_oxy[column] == "1").dropna()

    rows_with_0 = data_code_for_oxy.where(data_code_for_oxy[column] == "0").dropna()

    print(len(rows_with_1), len(rows_with_0))

    if len(rows_with_1) == len(rows_with_0):
        selected_rows = rows_with_1

    if len(selected_rows) == 1:
        the_row = selected_rows
        oxygen_generator_rating = int(
            "".join(the_row.apply(lambda x: "".join(x)).tolist()), 2
        )
        break
    else:
        data_code_for_oxy = selected_rows

column = None
the_row = None

data_code_for_co2 = pandas.DataFrame(data[0].apply(list).tolist())

for column in data_code_for_co2:
    least_common_bit = data_code_for_co2[column].value_counts().index[-1]
    selected_rows = data_code_for_co2.where(
        data_code_for_co2[column] == least_common_bit
    ).dropna()

    rows_with_1 = data_code_for_co2.where(data_code_for_co2[column] == "1").dropna()

    rows_with_0 = data_code_for_co2.where(data_code_for_co2[column] == "0").dropna()

    print(len(rows_with_1), len(rows_with_0))

    if len(rows_with_1) == len(rows_with_0):
        selected_rows = rows_with_0

    if len(selected_rows) == 1:
        the_row = selected_rows
        co2_scrubber_rating = int(
            "".join(the_row.apply(lambda x: "".join(x)).tolist()), 2
        )
        break
    else:
        data_code_for_co2 = selected_rows

print(oxygen_generator_rating * co2_scrubber_rating)
