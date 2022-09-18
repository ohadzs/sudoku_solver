import copy
# import time

sudoku = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]


def check(y, x, z):
    while z[y][x] != 10:
        moner = 0
        monel = 0
        mone = 0

        for num in z[y]:
            if z[y][x] == num:
                moner += 1
        for h in range(0, 9):
            if z[y][x] == z[h][x]:
                monel += 1

        if y in [0, 1, 2] and x in [0, 1, 2]:
            for a in [0, 1, 2]:
                for b in [0, 1, 2]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [3, 4, 5] and x in [3, 4, 5]:
            for a in [3, 4, 5]:
                for b in [3, 4, 5]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [6, 7, 8] and x in [6, 7, 8]:
            for a in [6, 7, 8]:
                for b in [6, 7, 8]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [3, 4, 5] and x in [0, 1, 2]:
            for a in [3, 4, 5]:
                for b in [0, 1, 2]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [6, 7, 8] and x in [0, 1, 2]:
            for a in [6, 7, 8]:
                for b in [0, 1, 2]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [0, 1, 2] and x in [3, 4, 5]:
            for a in [0, 1, 2]:
                for b in [3, 4, 5]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [6, 7, 8] and x in [3, 4, 5]:
            for a in [6, 7, 8]:
                for b in [3, 4, 5]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [0, 1, 2] and x in [6, 7, 8]:
            for a in [0, 1, 2]:
                for b in [6, 7, 8]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        elif y in [3, 4, 5] and x in [6, 7, 8]:
            for a in [3, 4, 5]:
                for b in [6, 7, 8]:
                    if z[y][x] == z[a][b]:
                        mone += 1

        if moner == 1 and monel == 1 and mone == 1:
            return z[y][x]

        z[y][x] += 1
    return z[y][x]


def print_board(board):
    for a in range(len(board)):
        if a % 3 == 0 and a != 0:
            print("- - - - - - - - - - - - ")
        for b in range(len(board[0])):
            if b % 3 == 0 and b != 0:
                print(" | ", end="")
            if b == 8:
                print(board[a][b])
            else:
                print(str(board[a][b]) + " ", end="")


def enter_board(bo):
    print("Enter your board:")
    for a in range(len(bo)):
        b = input("Enter line " + str(a+1) + " : ")
        while len(b) != 9:
            b = input("Something went wrong\nEnter line: ")
        b = int(b)
        c = 8
        while c != -1:
            bo[a][c] = int(b % 10)
            b = (b - bo[a][c]) / 10
            c -= 1


ans = input("Wanna enter board? (y/n) ")
if ans == "y":
    enter_board(sudoku)
print("\nYour board:\n")
print_board(sudoku)
print("\nSolving...\n")
# start = time.time()
clone = copy.deepcopy(sudoku)
row = 0
line = 0
la = "add"
while row != 9:
    if sudoku[row][line] == 0:
        clone[row][line] += 1
        clone[row][line] = check(row, line, clone)
        if clone[row][line] == 10:
            la = "sub"
            clone[row][line] = 0
            line -= 1
            if line == -1:
                row -= 1
                line = 8
        else:
            la = "add"
            line += 1
            if line == 9:
                row += 1
                line = 0
    else:
        if la == "add":
            line += 1
            if line == 9:
                row += 1
                line = 0
        else:
            line -= 1
            if line == -1:
                row -= 1
                line = 8

# end = time.time()
print_board(clone)
# print("\ntook me only " + str(int(end - start)) + " seconds")
