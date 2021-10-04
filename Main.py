#Doug Lowe
#10-4-2021
#Code lets the user play connect 4 on the terminal, creates files for formating into a gif through jgraph
import numpy as np
import os

#creates folder for Moves
CURRPATH = os.getcwd()
if os.path.exists(CURRPATH + "/Moves"):
    multi = os.listdir(CURRPATH + "/Moves")
    for m in multi:
        os.remove(CURRPATH + "/Moves/" + m)
    os.rmdir(CURRPATH + "/Moves")
os.makedirs(CURRPATH + "/Moves")

#gets example board for formating ease
f = open("GRIDEXAMPLE.txt")
STARTINGBOARD = f.read()
f.close()
print(STARTINGBOARD)
 
#makes the empty board
def makeBoard():
    board = np.zeros((7,7))
    return board

#checks if location is valid
def validLoc(board, col):
    return board[6][col] == 0

#looks for next useable row
def nextRow(board, col):
    for r in range(7):
        if board[r][col] == 0:
            return r

#places piece onto board
def placePiece(board, row, col, piece):
    board[row][col] = piece
 
#used to print the board to the terminal
def termPrint(board):
    print(np.flip(board, 0))
 
#checks win conditions
def winMove(board, piece):
    for c in range(4):
        for r in range(7):
            if board[r][c] == piece:
                if board[r][c+1] == piece: 
                    if board[r][c+2] == piece: 
                        if board[r][c+3] == piece:
                            return True
 
    for c in range(7):
        for r in range(4):
            if board[r][c] == piece: 
                if board[r+1][c] == piece: 
                    if board[r+2][c] == piece: 
                        if board[r+3][c] == piece:
                            return True
 
    for c in range(4):
        for r in range(4):
            if board[r][c] == piece :
                if board[r+1][c+1] == piece : 
                    if board[r+2][c+2] == piece :
                        if board[r+3][c+3] == piece:
                            return True
 
    for c in range(4):
        for r in range(3, 7):
            if board[r][c] == piece: 
                if board[r-1][c+1] == piece: 
                        if board[r-2][c+2] == piece: 
                            if board[r-3][c+3] == piece:
                                return True
 
#makes the graph files
def makeGraph(board, move):
    name = "Moves/Move" + str(move) + ".txt"
    file = open(name, 'a')
    file.write(STARTINGBOARD)
    for c in range(7):
        for r in range(7):
            if board[r][c] != 0:
                if(board[r][c] == 1):
                    file.write("\n newline poly pcfill 1 0 0 color 1 0 0\n pts " + str(.5+c) + " " + str(.5+r) + " " + str(1.5+c) + " " + str(.5+r) + " " + str(1.5+c) + " " + str(1.5+r) + " " + str(.5+c) + " " + str(1.5+r) + "\n")
                else:
                    file.write("\n newline poly pcfill 0 0 1 color 0 0 1\n pts " + str(.5+c) + " " + str(.5+r) + " " + str(1.5+c) + " " + str(.5+r) + " " + str(1.5+c) + " " + str(1.5+r) + " " + str(.5+c) + " " + str(1.5+r) + "\n")
    file.close()

#starting declarations 
board = makeBoard()
termPrint(board)
game_over = False
currturn = 0
move = 0

#main while loop that runs the game until an illeagal move is made or a player wins
while not game_over:
    move += 1
    print("TURN " + str(move))
    if currturn == 0:
        number = input("Player 1 what is your move: ")
    else:
        number = input("Player 2 what is your move: ")
    number = int(number)
    if not validLoc(board, number):
        print("Impossible move")
        break
    row = nextRow(board, number)
    if currturn == 0:
        placePiece(board, row, number, 1)
        if winMove(board, 1):
            print("PLAYER 1 WINS")
            makeGraph(board, move)
            break
    else:
        placePiece(board, row, number, 2)
        if winMove(board, 2):
            print("PLAYER 2 WINS")
            makeGraph(board, move)
            break
    makeGraph(board, move)
    termPrint(board)
    if currturn == 0:
        currturn = 1
    else:
        currturn = 0
    