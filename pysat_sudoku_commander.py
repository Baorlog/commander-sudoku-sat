from pysat.solvers import Glucose3
import time
from commander import commander_exact_one
from sudoku import show_sudoku, read_sudoku
import math


def current_milli_time():
    return int(round(time.time() * 1000))


def pysat_sudoku_commander(sudoku):
    # Glucose initialize
    g = Glucose3()

    sudoku_size = len(sudoku)
    box_size = int(math.sqrt(sudoku_size))
    group_quantity = int(math.sqrt(sudoku_size))

    read_sudoku(sudoku, sudoku_size, g)

    # Commander temporary group variables index
    current_c = int(math.pow(sudoku_size, 3)) + 1

    # Number of clause
    num_clause = 0

    # Implement basic rules of sudoku

    # Each cell contains only 1 number
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            var_list = []
            for k in range(1, sudoku_size + 1):
                var_list.append(i*int(math.pow(sudoku_size, 2)) + j*sudoku_size + k)

            group_list = []

            for k in range(group_quantity):
                group_list.append(current_c + k)

            num_clause += commander_exact_one(var_list, group_list, g)

            current_c += group_quantity

    # Each number exists once in a row
    for i in range(sudoku_size):
        for k in range(1, sudoku_size + 1):
            var_list = []
            for j in range(sudoku_size):
                var_list.append(i*int(math.pow(sudoku_size, 2)) + j*sudoku_size + k)

            group_list = []

            for j in range(group_quantity):
                group_list.append(current_c + j)

            num_clause += commander_exact_one(var_list, group_list, g)

            current_c += group_quantity

    # Each number exists once in a column
    for j in range(sudoku_size):
        for k in range(1, sudoku_size + 1):
            var_list = []
            for i in range(sudoku_size):
                var_list.append(i*int(math.pow(sudoku_size, 2)) + j*sudoku_size + k)

            group_list = []

            for i in range(group_quantity):
                group_list.append(current_c + i)

            num_clause += commander_exact_one(var_list, group_list, g)

            current_c += group_quantity

    # Each number exists once in a box
    for k in range(1, sudoku_size + 1):
        for a in range(box_size):
            for b in range(box_size):
                var_list = []
                for i in range(box_size):
                    for j in range(box_size):
                        var_list.append((a*box_size+i)*int(math.pow(sudoku_size, 2)) + (b*box_size+j)*sudoku_size + k)

                group_list = []

                for i in range(group_quantity):
                    group_list.append(current_c + i)

                num_clause += commander_exact_one(var_list, group_list, g)

                current_c += group_quantity

    start = current_milli_time()
    print(g.solve())
    result = g.get_model()
    print(result)
    end = current_milli_time()
    print("Time to solve: " + str(end-start) + " (ms)")
    print("Number of clause: " + str(num_clause))

    if result is not None:
        show_sudoku(result, sudoku_size)

