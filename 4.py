import pandas as pd

filename = "input_4"

import csv


def check_bingo(pd):

    # check if any row has only non-na values
    for i in range(len(pd)):
        if pd.iloc[i].isna().sum() == 0:
            return True
    # check if any column has only non-na values
    for i in range(len(pd.columns)):
        if pd.iloc[:, i].isna().sum() == 0:
            return True

    return False


numbers_to_draw = []
with open(filename) as csvFile:
    reader = csv.reader(csvFile)
    numbers_to_draw = next(reader)

boards = pd.read_csv(
    filename, dtype=int, delim_whitespace=True, header=None, skiprows=1
)
boards_marked = pd.DataFrame().reindex_like(boards)

for i, number in enumerate(numbers_to_draw):
    print(i, number)

    number = int(number)

    for j in range(100):

        board = boards[(j % 100) * 5 : ((j + 1) % 100) * 5]

        if board.isin([number]).any().any():
            boards_marked.update(board[board.isin([number])], overwrite=False)

            is_bingo = check_bingo(boards_marked[(j % 100) * 5 : ((j + 1) % 100) * 5])

            if is_bingo:
                print("Bingo!")

                board_marked = boards_marked[(j % 100) * 5 : ((j + 1) % 100) * 5]

                print(board)
                print(board_marked)

                board_non_marked = board[(~board_marked.notna())]
                sum_non_marked = board_non_marked.sum().sum()

                print(int(sum_non_marked * number))
                exit()
