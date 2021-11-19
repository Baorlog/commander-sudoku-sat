from pysat.solvers import Glucose3
import time
from sudoku import read_sudoku, show_sudoku


def current_milli_time():
    return int(round(time.time() * 1000))


g = Glucose3()
sum1 = 0

# Only 1 number in one cell, each number exists once in a row, column
for i in range(9):
    for j in range(9):
        # i -> row, j -> col, k -> num
        g.add_clause([i*81+j*9+1, i*81+j*9+2, i*81+j*9+3, i*81+j*9+4, i*81+j*9+5, i*81+j*9+6, i*81+j*9+7, i*81+j*9+8, i*81+j*9+9])
        # i -> row, k -> col, j -> num
        g.add_clause([i*81+0*9+j+1, i*81+1*9+j+1, i*81+2*9+j+1, i*81+3*9+j+1, i*81+4*9+j+1, i*81+5*9+j+1, i*81+6*9+j+1, i*81+7*9+j+1, i*81+8*9+j+1])
        # k -> row, j -> col, i -> num
        g.add_clause([0*81+j*9+i+1, 1*81+j*9+i+1, 2*81+j*9+i+1, 3*81+j*9+i+1, 4*81+j*9+i+1, 5*81+j*9+i+1, 6*81+j*9+i+1, 7*81+j*9+i+1, 8*81+j*9+i+1])
        sum1 += 3
        for k in range(1, 9):
            for l in range(k+1, 10):
                # k, l -> num
                g.add_clause([-(i*81+j*9+k), -(i*81+j*9+l)])
                # k, l -> col
                g.add_clause([-(i*81+(k-1)*9+j+1), -(i*81+(l-1)*9+j+1)])
                # k, l -> row
                g.add_clause([-((k-1)*81+j*9+i+1), -((l-1)*81+j*9+i+1)])
                sum1 += 3

#Box
for k in range(1, 10):
    # clause = []
    for a in range(3):
        for b in range(3):
            clause = []
            for i in range(3):
                for j in range(3):
                    clause.append((a*3+i)*81+(b*3+j)*9+k)
            g.add_clause(clause)
            sum1 += 1
            for i in range(len(clause) - 1):
                for j in range(i + 1, len(clause)):
                    g.add_clause([-(clause[i]), -(clause[j])])
                    sum1 += 1

sudoku = [
        "5,3,0,0,7,0,0,0,0",
        "6,0,0,1,9,5,0,0,0",
        "0,9,8,0,0,0,0,6,0",
        "8,0,0,0,6,0,0,0,3",
        "4,0,0,8,0,3,0,0,1",
        "7,0,0,0,2,0,0,0,6",
        "0,6,0,0,0,0,2,8,0",
        "0,0,0,4,1,9,0,0,5",
        "0,0,0,0,8,0,0,7,9"
    ]

read_sudoku(sudoku, 9, g)

start = current_milli_time()
print(g.solve())
result = g.get_model()
print(result)
end = current_milli_time()
print("Time to solve: " + str(end-start) + " (ms)")
print("Number of clause: " + str(sum1))

show_sudoku(result, 9)
