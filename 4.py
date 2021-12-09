import numpy as np
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


def get_the_last_bingo(boards):

    board_count = 100
    board_size = 5

    boards_marked = pd.DataFrame().reindex_like(boards)

    finished_boards = np.array([[False, None]] * board_count)
    is_bingo = False
    for i, number in enumerate(numbers_to_draw):

        number = int(number)

        for j in range(board_count):

            board = boards[
                (j % board_count) * board_size : ((j + 1) % board_count) * board_size
            ]

            if board.isin([number]).any().any():
                boards_marked.update(board[board.isin([number])], overwrite=False)

                if (not finished_boards[j,0]) and check_bingo(
                    boards_marked[
                        (j % board_count)
                        * board_size : ((j + 1) % board_count)
                        * board_size
                    ]
                ):
                    finished_boards[j,0] = True

                    board_marked = boards_marked[
                        (j % board_count)
                        * board_size : ((j + 1) % board_count)
                        * board_size
                    ]

                    board_non_marked = board[(~board_marked.notna())]
                    sum_non_marked = board_non_marked.sum().sum()

                    finished_boards[j,1] = int(sum_non_marked * number)

                    last_score = finished_boards[j,1]
    
    return last_score


def get_the_first_bingo(boards):

    boards_marked = pd.DataFrame().reindex_like(boards)

    for i, number in enumerate(numbers_to_draw):
        number = int(number)

        for j in range(100):

            board = boards[(j % 100) * 5 : ((j + 1) % 100) * 5]

            if board.isin([number]).any().any():
                boards_marked.update(board[board.isin([number])], overwrite=False)

                is_bingo = check_bingo(
                    boards_marked[(j % 100) * 5 : ((j + 1) % 100) * 5]
                )

                if is_bingo:
                    board_marked = boards_marked[(j % 100) * 5 : ((j + 1) % 100) * 5]
                    board_non_marked = board[(~board_marked.notna())]
                    sum_non_marked = board_non_marked.sum().sum()

                    return int(sum_non_marked * number)


numbers_to_draw = []
with open(filename) as csvFile:
    reader = csv.reader(csvFile)
    numbers_to_draw = next(reader)

boards = pd.read_csv(
    filename, dtype=int, delim_whitespace=True, header=None, skiprows=1
)

print(get_the_first_bingo(boards))
print(get_the_last_bingo(boards))
