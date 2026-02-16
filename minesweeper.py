import random

def print_board(board):
    # for roww in range(10):
    #     print(board[roww])
    for roww in range(10):
        print(*board[roww])
    print()
    # print('\n'.join(''.join(roww) for roww in board))
    # print('\n'.join(map(''.join, str(board))))


def count_neighbors(matrix, row, col):
    count = 0
    bomb = 9
    if (row == 0 and col ==0):
        if (matrix[row][col+1] == bomb):
            count+=1
        if (matrix[row+1][col+1] == bomb):
            count+=1
        if (matrix[row+1][col] == bomb):
            count+=1

    elif (row == 0 and col > 0 and col < 9):
        if (matrix[row][col-1] == bomb):
            count+=1
        if (matrix[row+1][col-1] == bomb):
            count+=1
        if (matrix[row+1][col] == bomb):
            count+=1
        if (matrix[row+1][col+1] == bomb):
            count+=1
        if (matrix[row][col+1] == bomb):
            count+=1

    elif (row == 0 and col ==9):
        if (matrix[row][col-1] == bomb):
            count+=1
        if (matrix[row+1][col-1] == bomb):
            count+=1
        if (matrix[row+1][col] == bomb):
            count+=1

    elif (row > 0 and row < 9 and col == 9):
        if (matrix[row-1][col] == bomb):
            count+=1
        if (matrix[row-1][col-1] == bomb):
            count+=1
        if (matrix[row][col-1] == bomb):
            count+=1
        if (matrix[row+1][col-1] == bomb):
            count+=1
        if (matrix[row+1][col] == bomb):
            count+=1

    elif (row == 9 and col ==9):
        if (matrix[row-1][col] == bomb):
            count+=1
        if (matrix[row-1][col-1] == bomb):
            count+=1
        if (matrix[row][col-1] == bomb):
            count+=1

    elif (row == 9 and col >0 and col <9):
        if (matrix[row][col+1] == bomb):
            count+=1
        if (matrix[row-1][col+1] == bomb):
            count+=1
        if (matrix[row-1][col] == bomb):
            count+=1
        if (matrix[row-1][col-1] == bomb):
            count+=1
        if (matrix[row][col-1] == bomb):
            count+=1

    elif (row == 9 and col ==0):
        if (matrix[row][col+1] == bomb):
            count+=1
        if (matrix[row-1][col+1] == bomb):
            count+=1
        if (matrix[row-1][col] == bomb):
            count+=1

    elif (row >0 and row < 9 and col ==0):
        if (matrix[row+1][col] == bomb):
            count+=1
        if (matrix[row+1][col+1] == bomb):
            count+=1
        if (matrix[row][col+1] == bomb):
            count+=1
        if (matrix[row-1][col+1] == bomb):
            count+=1
        if (matrix[row-1][col] == bomb):
            count+=1

    else:
        if (matrix[row-1][col-1] == bomb):
            count+=1
        if (matrix[row-1][col] == bomb):
            count+=1
        if (matrix[row-1][col+1] == bomb):
            count+=1
        if (matrix[row][col+1] == bomb):
            count+=1
        if (matrix[row+1][col+1] == bomb):
            count+=1
        if (matrix[row+1][col] == bomb):
            count+=1
        if (matrix[row+1][col-1] == bomb):
            count+=1
        if (matrix[row][col-1] == bomb):
            count+=1
    return count

def borders_open(matrix, x_board, row, col):
    if (row == 0 and col ==0):
        x_board[row][col+1] = matrix[row][col+1]
        x_board[row+1][col+1] = matrix[row+1][col+1]
        x_board[row+1][col] = matrix[row+1][col]

    elif (row == 0 and col > 0 and col < 9):
        x_board[row][col-1] = matrix[row][col-1]
        x_board[row+1][col-1] = matrix[row+1][col-1]
        x_board[row+1][col] = matrix[row+1][col]
        x_board[row+1][col+1] = matrix[row+1][col+1]
        x_board[row][col+1] = matrix[row][col+1]

    elif (row == 0 and col ==9):
        x_board[row][col - 1] = matrix[row][col - 1]
        x_board[row+1][col - 1] = matrix[row+1][col - 1]
        x_board[row+1][col] = matrix[row+1][col]

    elif (row > 0 and row < 9 and col == 9):
        x_board[row-1][col] = matrix[row-1][col]
        x_board[row-1][col-1] = matrix[row-1][col-1]
        x_board[row][col-1] = matrix[row][col-1]
        x_board[row+1][col-1] = matrix[row+1][col-1]
        x_board[row+1][col] = matrix[row+1][col]

    elif (row == 9 and col ==9):
        x_board[row-1][col] = matrix[row-1][col]
        x_board[row-1][col-1] = matrix[row-1][col-1]
        x_board[row][col-1] = matrix[row][col-1]


    elif (row == 9 and col >0 and col <9):
        x_board[row][col+1] = matrix[row][col+1]
        x_board[row-1][col+1] = matrix[row-1][col+1]
        x_board[row-1][col] = matrix[row-1][col]
        x_board[row-1][col-1] = matrix[row-1][col-1]
        x_board[row][col-1] = matrix[row][col-1]

    elif (row == 9 and col ==0):
        x_board[row][col+1] = matrix[row][col+1]
        x_board[row-1][col+1] = matrix[row-1][col+1]
        x_board[row-1][col] = matrix[row-1][col]

    elif (row >0 and row < 9 and col ==0):
        x_board[row+1][col] = matrix[row+1][col]
        x_board[row+1][col+1] = matrix[row+1][col+1]
        x_board[row][col+1] = matrix[row][col+1]
        x_board[row-1][col+1] = matrix[row-1][col+1]
        x_board[row-1][col] = matrix[row-1][col]

    else:
        x_board[row-1][col-1] = matrix[row-1][col-1]
        x_board[row-1][col] = matrix[row-1][col]
        x_board[row-1][col+1] = matrix[row-1][col+1]
        x_board[row][col+1] = matrix[row][col+1]
        x_board[row+1][col+1] = matrix[row+1][col+1]
        x_board[row+1][col] = matrix[row+1][col]
        x_board[row+1][col-1] = matrix[row+1][col-1]
        x_board[row][col-1] = matrix[row][col-1]
    return x_board

def initiate_board():
    # creating a matrix with zeros
    matrix = []
    bomb = 9
    for row in range(10):
        row_add = []
        for col in range(10):
            row_add.append(0)
        matrix.append(row_add)
    # filling in the matrix with mines
    count = 1
    while (count<10):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if (matrix[row][col] == 0):
            matrix[row][col] = bomb
            count += 1
    # filling with numbers
    for row in range(10):
        for col in range(10): #########
            if (matrix[row][col] == 0):
                matrix[row][col] = count_neighbors(matrix,row,col)
    print_board(matrix)
    return matrix


def initiate_hidden_board():
    x_board = []
    for row in range(10):
        row_add = []
        for col in range(10):
           row_add.append('X')
        x_board.append(row_add)
    print_board(x_board)
    return x_board

def check(n):
    if (n.isnumeric()):
        if (int(n)>=0 and int(n)<=9):
            return n
        else:
            n = input("number should be between 0 and 9, plz try again:")
            return check(n)
    else:
        n = input("Not a number, plz try again: ")
        return check(n)

def game_over_board(matrix, x_board):
    for roww in range(10):
        for coll in range(10):
            if (matrix[roww][coll] == 9):
                x_board[roww][coll] = 'B'
    return x_board

def check_for_zero(matrix, x_board, row, col): # the recursion doesn't stop (never gets to else)
    # check if there are any zeros around matrix[row][col]
    # checking if boxes around exist
    if (row-1>=0 and matrix[row-1][col] == 0):
        # then this box exists
        # top
        x_board = borders_open(matrix,x_board, row-1, col)
        return check_for_zero(matrix,x_board, row-1, col)
    elif (col+1<=9 and matrix[row][col+1] == 0):
        # right
        x_board = borders_open(matrix,x_board, row, col+1)
        return check_for_zero(matrix,x_board, row, col+1)
    elif (row+1<=9 and matrix[row+1][col] == 0):
        # bottom
        x_board = borders_open(matrix,x_board, row+1, col)
        return check_for_zero(matrix,x_board, row+1, col)
    elif (col-1>=0 and matrix[row][col-1] == 0):
        # left
        x_board = borders_open(matrix,x_board, row, col-1)
        return check_for_zero(matrix,x_board, row, col-1)
    else:
        return x_board


def open(matrix, x_board, row, col):
    # matrix[row][col] = 0
    # open_neighbours
    x_board = borders_open(matrix, x_board, row, col)
    x_board = check_for_zero(matrix, x_board, row, col)
    print_board(x_board)


# game start:
matrix = initiate_board()
x_board = initiate_hidden_board()
bomb = 9
bombs_count = 0
while (bombs_count<10):
    row = input("Enter row: ")
    row = int(check(row))
    col = input("Enter col: ")
    col = int(check(col))
    act = input("If u want to open, enter 1, and if to put a flag - enter 2: ")
    while (act != '1' and act != '2'):
        act = input("Invalid command, try again:")
    if (act == '1'):
        # open
        if (matrix[row][col] == bomb):
            print("Game over, try again >:)")
            print_board(game_over_board(matrix, x_board))
            break
        else:
            x_board[row][col] = matrix[row][col] #open first
            if (matrix[row][col] == 0):
                open(matrix, x_board, row, col)
    else:
        # put a flag as 'f' in x_board
        pass