import numpy as np

ROW_COUNT = 6 
COLUMN_COUNT = 7 

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0
    #checking to see if the space is filled or not 

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))
    #This is a command in numpy which will flip. Zero is for the access. 

board = create_board()
print_board(board)
game_over = False;
turn = 0 

while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your col (0-6):"))
        #int makes sure it's an int and not a string 
        #print(col)#printing out the 
        #print(type(col))#used to check if it is string or int

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    #Ask for player 2 input
    else:
        col = int(input("Player 2 make your col (0-6):"))
    
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_board(board)


    turn += 1
    turn = turn % 2


