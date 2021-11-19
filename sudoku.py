import math


def read_sudoku(sudoku, size, g):
    for i in range(size):
        row = [int(x) for x in sudoku[i].split(",")]
        for j in range(size):
            number = row[j]
            if number:
                g.add_clause([i * int(math.pow(size, 2)) + j * size + number])


def show_sudoku(var_list, size):
    for i in range(size):
        for j in range(size):
            number_in_cell = ""
            for k in range(size):
                if var_list[i * int(math.pow(size, 2)) + j * size + k] > 0:
                    number_in_cell = k + 1

            print(number_in_cell, end="\t")
        print()


def check_sudoku(sudoku):
    size = len(sudoku)
    print("Row: " + str(size))
    invalid_row = -1
    for i in range(size):
        print("In row: " + str(i + 1))
        if len(sudoku[i].split(",")) != size:
            invalid_row = i + 1
            print(len(sudoku[i].split(",")))
            break
        else:
            valid_row = sudoku[i].split(",")
            for j in range(size):
                if int(valid_row[j]) > 36 or int(valid_row[j]) < 0:
                    print(valid_row[j])
    print(invalid_row)


