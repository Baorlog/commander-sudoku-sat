from pysat_sudoku_commander import pysat_sudoku_commander


if __name__ == "__main__":

    # SUDOKU 9X9

    # sudoku = [
    #     "0,0,0,0,0,0,2,0,0",
    #     "0,8,0,0,0,7,0,9,0",
    #     "6,0,2,0,0,0,5,0,0",
    #     "0,7,0,0,6,0,0,0,0",
    #     "0,0,0,9,0,1,0,0,0",
    #     "0,0,0,0,2,0,0,4,0",
    #     "0,0,5,0,0,0,6,0,3",
    #     "0,9,0,4,0,0,0,7,0",
    #     "0,0,6,0,0,0,0,0,0"
    # ]
    # sudoku = [
    #     "0,2,0,5,0,1,0,9,0",
    #     "8,0,0,2,0,3,0,0,6",
    #     "0,3,0,0,6,0,0,7,0",
    #     "0,0,1,0,0,0,6,0,0",
    #     "5,4,0,0,0,0,0,1,9",
    #     "0,0,2,0,0,0,7,0,0",
    #     "0,9,0,0,3,0,0,8,0",
    #     "2,0,0,8,0,4,0,0,7",
    #     "0,1,0,9,0,7,0,6,0"
    # ]
    #
    # sudoku = [
    #     "1,0,0,0,4,0,0,0,0",
    #     "4,0,0,0,8,0,0,3,6",
    #     "0,0,0,0,7,0,9,0,0",
    #     "2,0,7,0,0,8,0,6,0",
    #     "0,0,0,0,0,4,0,8,0",
    #     "0,0,1,0,0,5,0,2,4",
    #     "0,0,0,0,5,0,3,0,0",
    #     "0,6,3,1,0,0,0,0,0",
    #     "7,0,0,0,0,0,0,0,0"
    # ]
    #
    # sudoku = [
    #     "0,9,1,3,0,2,0,0,0",
    #     "0,0,0,0,0,0,0,0,0",
    #     "2,8,5,0,9,0,6,0,0",
    #     "0,0,9,0,0,0,0,0,8",
    #     "5,0,0,8,0,9,2,0,0",
    #     "0,0,0,0,6,0,4,0,0",
    #     "1,0,0,0,0,0,0,0,9",
    #     "0,3,0,0,0,7,0,5,0",
    #     "0,0,0,0,0,0,7,3,4"
    # ]
    # #
    # sudoku = [
    #     "0,0,8,0,2,4,0,6,0",
    #     "2,0,0,0,8,0,4,3,0",
    #     "0,0,0,1,0,0,0,0,0",
    #     "1,0,0,0,0,7,0,0,5",
    #     "7,3,0,5,0,1,0,9,6",
    #     "6,0,0,2,0,0,0,0,4",
    #     "0,0,0,0,0,6,0,0,0",
    #     "0,1,3,0,5,0,0,0,2",
    #     "0,5,0,7,9,0,1,0,0"
    # ]
    # #
    # sudoku = [
    #     "5,3,0,0,7,0,0,0,0",
    #     "6,0,0,1,9,5,0,0,0",
    #     "0,9,8,0,0,0,0,6,0",
    #     "8,0,0,0,6,0,0,0,3",
    #     "4,0,0,8,0,3,0,0,1",
    #     "7,0,0,0,2,0,0,0,6",
    #     "0,6,0,0,0,0,2,8,0",
    #     "0,0,0,4,1,9,0,0,5",
    #     "0,0,0,0,8,0,0,7,9"
    # ]

    # SUDOKU 16X16

    # sudoku = [
    #     "1,0,0,2,3,4,0,0,12,0,6,0,0,0,7,0",
    #     "0,0,8,0,0,0,7,0,0,3,0,0,9,10,6,11",
    #     "0,12,0,0,10,0,0,1,0,13,0,11,0,0,14,0",
    #     "3,0,0,15,2,0,0,14,0,0,0,9,0,0,12,0",
    #
    #     "13,0,0,0,8,0,0,10,0,12,2,0,1,15,0,0",
    #     "0,11,7,6,0,0,0,16,0,0,0,15,0,0,5,13",
    #     "0,0,0,10,0,5,15,0,0,4,0,8,0,0,11,0",
    #     "16,0,0,5,9,12,0,0,1,0,0,0,0,0,8,0",
    #
    #     "0,2,0,0,0,0,0,13,0,0,12,5,8,0,0,3",
    #     "0,13,0,0,15,0,3,0,0,14,8,0,16,0,0,0",
    #     "5,8,0,0,1,0,0,0,2,0,0,0,13,9,15,0",
    #     "0,0,12,4,0,6,16,0,13,0,0,7,0,0,0,5",
    #
    #     "0,3,0,0,12,0,0,0,6,0,0,4,11,0,0,16",
    #     "0,7,0,0,16,0,5,0,14,0,0,1,0,0,2,0",
    #     "11,1,15,9,0,0,13,0,0,2,0,0,0,14,0,0",
    #     "0,14,0,0,0,11,0,2,0,0,13,3,5,0,0,12"
    # ]

    # sudoku = [
    #     "0,0,0,16,3,4,7,0,0,10,8,0,0,15,9,0",
    #     "8,0,0,0,0,0,9,0,13,0,2,15,3,0,1,5",
    #     "0,10,9,2,11,0,6,15,0,3,7,0,12,8,0,13",
    #     "3,4,14,15,0,1,8,0,16,0,0,12,0,10,0,7",
    #
    #     "0,0,12,7,0,0,0,0,9,2,0,0,10,0,0,16",
    #     "0,9,4,0,0,0,0,0,5,0,0,6,0,0,0,0",
    #     "0,0,0,0,0,0,2,0,0,8,0,16,5,1,15,0",
    #     "0,2,0,1,16,8,0,11,15,0,0,3,6,9,7,0",
    #
    #     "0,15,7,13,6,0,0,4,10,0,3,8,16,0,5,0",
    #     "0,12,8,4,14,0,16,0,0,5,0,0,0,0,0,0",
    #     "0,0,0,0,7,0,0,10,0,0,0,0,0,3,4,0",
    #     "10,0,0,14,0,0,11,8,0,0,0,0,9,2,0,0",
    #
    #     "4,0,2,0,15,0,0,5,0,9,6,0,11,12,14,3",
    #     "9,0,11,3,0,16,13,0,2,15,0,1,7,5,8,0",
    #     "7,1,0,5,2,6,0,9,0,142,0,0,0,0,0,15",
    #     "0,14,15,0,0,11,4,0,0,16,5,10,1,0,0,0"
    # ]

    # SUDOKU 25X25

    # sudoku = [
    #     "0,18,15,9,0,21,0,0,0,0,0,0,22,1,0,0,5,0,14,0,12,0,0,13,7",
    #     "23,0,0,4,0,0,0,11,0,0,0,25,24,0,0,18,0,0,20,0,6,0,0,0,0",
    #     "0,0,24,13,0,3,0,2,9,0,7,20,19,0,0,0,0,0,0,10,5,0,1,14,0",
    #     "0,11,16,0,19,0,0,17,23,7,13,2,0,6,0,0,0,0,0,0,0,10,0,0,0",
    #     "17,12,0,0,0,14,0,1,0,8,3,10,0,0,9,0,2,0,0,0,24,0,18,0,19",
    #
    #     "0,0,0,20,0,9,0,21,3,0,22,0,18,12,19,14,0,0,0,6,0,0,0,2,0",
    #     "14,16,0,2,6,25,0,0,0,0,0,5,0,7,0,4,0,0,0,22,0,0,13,0,12",
    #     "0,0,21,0,0,11,0,0,15,10,0,23,0,0,0,0,13,19,2,16,9,22,5,0,0",
    #     "8,0,19,5,3,24,0,0,0,18,0,17,0,14,0,1,0,0,0,0,0,0,25,10,0",
    #     "0,0,0,23,0,0,13,8,12,0,24,0,0,0,0,0,18,0,0,9,0,0,11,0,21",
    #
    #     "4,0,14,0,0,8,0,7,20,0,2,6,13,0,0,24,3,0,1,0,15,0,0,5,0",
    #     "0,0,0,0,22,0,15,0,17,0,0,19,0,0,16,7,0,14,0,18,25,11,24,23,0",
    #     "0,25,0,3,0,23,0,0,0,1,0,0,0,20,0,0,6,9,12,15,0,18,19,17,0",
    #     "13,0,0,0,0,0,9,0,0,0,0,15,1,25,11,16,0,0,10,0,22,0,4,6,14",
    #     "21,0,0,24,23,0,0,0,0,0,4,0,0,17,0,0,0,0,0,0,13,0,0,16,20",
    #
    #     "0,0,0,1,2,0,0,10,0,0,18,14,0,15,25,0,0,0,0,0,0,21,0,0,6",
    #     "10,19,0,22,0,0,0,0,0,0,0,0,0,0,2,0,0,4,0,11,0,14,0,0,0",
    #     "25,0,0,0,21,0,0,0,18,0,0,0,0,0,1,9,16,6,13,8,20,0,15,0,22",
    #     "5,8,0,16,13,4,24,0,19,23,0,0,20,21,0,0,10,0,7,0,0,0,0,11,0",
    #     "0,9,0,0,0,0,20,0,22,0,12,0,0,11,0,0,0,0,0,23,0,0,7,0,0",
    #
    #     "0,6,0,0,0,0,0,0,5,22,0,1,0,19,3,0,11,7,0,21,0,24,14,8,0",
    #     "2,7,0,0,0,12,6,0,0,0,0,0,0,4,8,0,0,0,0,19,0,13,0,0,0",
    #     "0,21,0,10,0,0,0,19,25,24,9,13,0,18,0,0,0,3,0,2,0,5,0,7,0",
    #     "0,0,1,0,8,2,0,0,0,0,0,0,10,0,17,0,14,5,18,12,0,0,0,0,0",
    #     "0,5,18,25,24,20,23,3,0,21,0,0,0,0,0,8,0,0,0,0,0,16,22,1,0"
    # ]

    # SUDOKU 36X36

    sudoku = [
        "17,0,5,0,0,0,16,0,24,0,0,0,0,0,0,0,0,0,2,0,19,0,0,0,27,0,13,0,0,0,0,0,0,0,0,0",
        "0,22,0,0,18,0,0,0,0,32,0,9,4,0,21,3,0,12,0,10,0,0,28,0,0,0,0,8,0,15,6,0,23,25,0,31",
        "2,0,19,0,0,0,27,0,13,0,0,0,0,0,0,0,0,0,17,0,5,0,0,0,16,0,24,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,4,0,21,0,0,0,16,32,24,0,9,0,0,0,0,0,0,0,6,0,23,0,0,0,27,8,13,0,15,0",
        "0,10,0,0,28,0,0,0,0,8,0,15,6,0,23,25,0,31,0,22,0,0,18,0,0,0,0,32,0,9,4,0,21,3,0,12",
        "0,0,0,0,0,0,6,0,23,0,0,0,27,8,13,0,15,0,0,0,0,0,0,0,4,0,21,0,0,0,16,32,24,0,9,0",

        "32,0,9,0,0,0,0,0,0,16,0,24,0,0,0,17,0,5,8,0,15,0,0,0,0,0,0,27,0,13,0,0,0,2,0,19",
        "0,0,0,17,0,5,0,0,0,0,0,0,3,0,12,0,0,0,0,0,0,2,0,19,0,0,0,0,0,0,25,0,31,0,0,0",
        "8,0,15,0,0,0,0,0,0,27,0,13,0,0,0,2,0,19,32,0,9,0,0,0,0,0,0,16,0,24,0,0,0,17,0,5",
        "7,0,20,0,0,0,1,0,11,0,0,0,0,0,0,16,0,24,26,0,34,0,0,0,29,0,35,0,0,0,0,0,0,27,0,13",
        "0,0,0,2,0,19,0,0,0,0,0,0,25,0,31,0,0,0,0,0,0,17,0,5,0,0,0,0,0,0,3,0,12,0,0,0",
        "26,0,34,0,0,0,29,0,35,0,0,0,0,0,0,27,0,13,7,0,20,0,0,0,1,0,11,0,0,0,0,0,0,16,0,24",

        "0,17,0,22,5,18,0,0,0,36,0,14,0,0,0,0,0,0,0,2,0,10,19,28,0,0,0,30,0,33,0,0,0,0,0,0",
        "1,0,11,16,0,24,32,0,9,0,0,0,0,36,0,0,14,0,29,0,35,27,0,13,8,0,15,0,0,0,0,30,0,0,33,0",
        "0,2,0,10,19,28,0,0,0,30,0,33,0,0,0,0,0,0,0,17,0,22,5,18,0,0,0,36,0,14,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,4,0,21,0,0,0,1,0,11,0,0,0,0,0,0,0,0,0,6,0,23,0,0,0,29,0,35",
        "29,0,35,27,0,13,8,0,15,0,0,0,0,30,0,0,33,0,1,0,11,16,0,24,32,0,9,0,0,0,0,36,0,0,14,0",
        "0,0,0,0,0,0,0,0,0,6,0,23,0,0,0,29,0,35,0,0,0,0,0,0,0,0,0,4,0,21,0,0,0,1,0,11",

        "5,0,17,0,0,0,24,0,16,0,0,0,0,0,0,0,0,0,19,0,2,0,0,0,13,0,27,0,0,0,0,0,0,0,0,0",
        "0,18,0,0,22,0,0,0,0,9,0,32,21,0,4,12,0,3,0,28,0,0,10,0,0,0,0,15,0,8,23,0,6,31,0,25",
        "19,0,2,0,0,0,13,0,27,0,0,0,0,0,0,0,0,0,5,0,17,0,0,0,24,0,16,0,0,0,0,0,0,0,0,0",
        "0,0,0,0,0,0,21,0,4,0,0,0,24,9,16,0,32,0,0,0,0,0,0,0,23,0,6,0,0,0,13,15,27,0,8,0",
        "0,28,0,0,10,0,0,0,0,15,0,8,23,0,6,31,0,25,0,18,0,0,22,0,0,0,0,9,0,32,21,0,4,12,0,3",
        "0,0,0,0,0,0,23,0,6,0,0,0,13,15,27,0,8,0,0,0,0,0,0,0,21,0,4,0,0,0,24,9,16,0,32,0",

        "9,0,32,0,0,0,0,0,0,24,0,16,0,0,0,5,0,17,15,0,8,0,0,0,0,0,0,13,0,27,0,0,0,19,0,2",
        "0,0,0,5,0,17,0,0,0,0,0,0,12,0,3,0,0,0,0,0,0,19,0,2,0,0,0,0,0,0,31,0,25,0,0,0",
        "15,0,8,0,0,0,0,0,0,13,0,27,0,0,0,19,0,2,9,0,32,0,0,0,0,0,0,24,0,16,0,0,0,5,0,17",
        "20,0,7,0,0,0,11,0,1,0,0,0,0,0,0,24,0,16,34,0,26,0,0,0,35,0,29,0,0,0,0,0,0,13,0,27",
        "0,0,0,19,0,2,0,0,0,0,0,0,31,0,25,0,0,0,0,0,0,5,0,17,0,0,0,0,0,0,12,0,3,0,0,0",
        "34,0,26,0,0,0,35,0,29,0,0,0,0,0,0,13,0,27,20,0,7,0,0,0,11,0,1,0,0,0,0,0,0,24,0,16",

        "0,5,0,18,17,22,0,0,0,14,0,36,0,0,0,0,0,0,0,19,0,28,2,10,0,0,0,33,0,30,0,0,0,0,0,0",
        "11,0,1,24,0,16,9,0,32,0,0,0,0,14,0,0,36,0,35,0,29,13,0,27,15,0,8,0,0,0,0,33,0,0,30,0",
        "0,19,0,28,2,10,0,0,0,33,0,30,0,0,0,0,0,0,0,5,0,18,17,22,0,0,0,14,0,36,0,0,0,0,0,0",
        "0,0,0,0,0,0,0,0,0,21,0,4,0,0,0,11,0,1,0,0,0,0,0,0,0,0,0,23,0,6,0,0,0,35,0,29",
        "35,0,29,13,0,27,15,0,8,0,0,0,0,33,0,0,30,0,11,0,1,24,0,16,9,0,32,0,0,0,0,14,0,0,36,0",
        "0,0,0,0,0,0,0,0,0,23,0,6,0,0,0,35,0,29,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,11,0,1"
    ]

    # check_sudoku(sudoku)
    pysat_sudoku_commander(sudoku)
