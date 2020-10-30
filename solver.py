import sys

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def printboard(puzzle):
    for i in range(len(puzzle)):

        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                sys.stdout.write(" | ")
            if j == 8:
                print(puzzle[i][j])
            else:
                sys.stdout.write(str(puzzle[i][j]) + " ")
        if i % 3 == 2 and i != 8:
            print("- - - - - - - - - - - - ")


printboard(board)
