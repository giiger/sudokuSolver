board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
def printBoard (puzzle):
    for i in range(len(puzzle)):
        if i % 3 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print(" | ")
            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ")

printBoard(board)