import random

def main():
    board, firstPlayer, secondPlayer = startGame()
    print("First player is: " + firstPlayer)
    print("Second player is: " + secondPlayer)
    printBoard(board)
    for i in range(9):
        if i % 2 == 0:
            empty = True
            while empty:
                print("First player's turn")
                row = input("Enter row: ")
                col = input("Enter column: ")
                if not row.isdigit() or not col.isdigit():
                    print("Invalid input")
                else: 
                    row, col = int(row), int(col)
                    if row > 2 or col > 2:
                        print("Invalid input")
                    elif board[row][col] == '-':
                        board[row][col] = firstPlayer
                        empty = False
                    else:
                        print("This cell is already filled")
                printBoard(board)
                if isWinner(board, firstPlayer):
                    print("First player wins")
                    playAgain()
                if isDraw(board):
                    print("It's a draw")
                    playAgain()
        else:
            empty = True
            while empty:
                print("Second player's turn")
                row = input("Enter row: ")
                col = input("Enter column: ")
                if not row.isdigit() or not col.isdigit():
                    print("Invalid input")
                else:
                    row, col = int(row), int(col)
                    if row > 2 or col > 2:
                        print("Invalid input")
                    elif board[row][col] == '-':
                        board[row][col] = secondPlayer
                        empty = False
                    else:
                        print("This cell is already filled")
                printBoard(board)
                if isWinner(board, secondPlayer):
                    print("Second player wins")
                    playAgain()
                if isDraw(board):
                    print("It's a draw")
                    playAgain()

def playAgain():
    playAgain = input("Do you want to play again? (yes/no): ")
    if playAgain == "yes":
        main()
    else:
        print("Goodbye")
        exit()

def initializeBoard(board):
    for i in range (3):
        for j in range(3):
            board[i][j] = '-'

def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()

def isFilled(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

def isWinner(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def isDraw(board):
    return isFilled(board) and not isWinner(board, 'X') and not isWinner(board, 'O')

def startGame():
    board = [["-" for i in range(3)] for j in range(3)]
    initializeBoard(board)
    firstPlayer = random.choice(['X', 'O'])
    if firstPlayer == 'X':
        secondPlayer = 'O'
    else:
        secondPlayer = 'X'
    return board, firstPlayer, secondPlayer

if __name__ == "__main__":
    main()