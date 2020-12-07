# Tic Tac Toe in Python (aka X’s and O’s game)

"""
TODO: 
 - A function to check if there is a winner
 - The insert letter function
 - A function to check if position is free
 - A function for the player move
 - The AI function for the computer
 - Select random function
 - The main function
"""

board = [' ' for x in range(10)]    # The blank board

#* Function: printing the board 
def printBoard(board):
    print(" " + board[1] + "| " + board[2] + "| " + board[3])
    print("---------")
    print(" " + board[4] + "| " + board[5] + "| " + board[6])
    print("---------")
    print(" " + board[7] + "| " + board[8] + "| " + board[9])

#* Function: check if board is full
   """
   Explain:
   Check if the board is full to end the game
   If the board is full then its a tie. 
   The board can lack to be full with no winner declared and hence a move can be made. 
   This function will be called every time before a move is made.
   """
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True




printBoard(board)