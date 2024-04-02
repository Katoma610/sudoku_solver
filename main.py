def checkBoard(board, num, row, col):
    # Check if num is in current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if num is in current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if num is in current 3x3 square
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False

    return True


def solveBoard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if checkBoard(board, n, i, j):
                        board[i][j] = n
                        if solveBoard(board):
                            return True
                        board[i][j] = 0
                return False
    return True


def printBoard(board):
    count1 = 1
    count2 = 1
    s = ""
    for i in range(9):
        for j in range(9):
            if count1 == 3:
                s += str(board[i][j]) + ' '
                count1 = 1
            else:
                s += str(board[i][j])
                count1 += 1
        print(s)
        s = ''
        if count2 == 3:
            print("\n", end='')
            count2 = 0
        count1 = 1
        count2 += 1
    return

def main():
    board = [
        [0,6,0,0,0,0,9,0,0],
        [0,0,0,0,0,5,6,8,0],
        [0,0,0,0,8,3,2,5,0],
        [0,0,0,0,3,2,0,7,0],
        [4,0,7,5,0,0,0,6,0],
        [0,0,2,7,0,0,0,0,0],
        [0,0,0,2,0,0,8,0,1],
        [0,5,0,0,0,0,0,0,0],
        [0,0,9,0,0,1,3,0,0]
    ]
    solveBoard(board)
    printBoard(board)



if __name__ == '__main__':
    main()
