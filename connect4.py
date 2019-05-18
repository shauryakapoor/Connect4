import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass

def is_valid_location(board, col):
    pass

def get_next_open_row():
    pass



board = create_board()
print(board)
game_over = False;
turn = 0 

while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your col (0-6):"))
        #int makes sure it's an int and not a string 
        #print(col)#printing out the 
        #print(type(col))#used to check if it is string or int

    #Ask for player 2 input
    else:
        col = int(input("Player 2 make your col (0-6):"))

    turn += 1
    turn = turn % 2


