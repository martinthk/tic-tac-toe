# Tic Tac Toe in Python (aka X’s and O’s game)
import json
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
# Human user will always be the 1st one to start and using 'x'
board = [' ' for x in range(10)]    # The blank board


# * Printing the board * #
def printBoard(board):
    print(" " + board[1] + "| " + board[2] + "| " + board[3])
    print("---------")
    print(" " + board[4] + "| " + board[5] + "| " + board[6])
    print("---------")
    print(" " + board[7] + "| " + board[8] + "| " + board[9])


# * Check if board is full * #
"""
Explain:
Check if the board is full to end the game
If the board is full then its a TIE. 
The board can lack to be full with no winner declared and hence a move can be made. 
This function will be called every time before a move is made.
"""


def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


# * Check if board is full * #
"""
Explain:
If the board isn’t full, we then check if there is a winner.
We declare a winner if 3 “x’s” or 3 “o’s” occur in 1 ROW or in COLUMN or DIAGONALLY.
"""


def isWinner(bo, le):
    # "bo" stands for the board.
    # "le" stands for the letter or symbol we're checking.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


# * Insert letter * #
""" 
Explain:
The user should insert a number position on the board in which 'x' will be planced.
Number position: 1 - 9 includsive
"""


def insertLetter(letter, pos):
    board[pos] = letter


# * Check if position is free * #
def spaceIsFree(pos):
    return board[pos] == " "


# * Allow player move * #
"""
Explain:
This function prompts the user to enter a position on the board in which an x is to be placed. 
1. It checks if the users input is valid. 
2. If the input is valid -> the position itself is checked for its status (occupied or empty). 
3. It saves the letter in that position if it checks out with the two cases. 
4. If it doesn’t pass one case, then an error is thrown back respectively 
5. This means that if it is occupied, the user is alerted and told to pick a different number. 
"""
def playMove():
    run = True
    while run:
        move = input("Please select position for 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("x", move)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Please type the number within the range")
        except:
            print("Please type a number.")


# Test
printBoard(board)
