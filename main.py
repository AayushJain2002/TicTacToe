'''
Created on Jan 5, 2022

@author: Aayush Jain

Challenges / Modifications
1. Make user choose either X or O to start with (account for when user tries to enter different values as tokens)
2. Use RegEx to account for positions on board
3. Add a player v computer component

'''

# global variables

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_is_still_going = True

# Who won or tie?
winner = None

current_player = "X"


def display_board():  # displays the empty board 
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():  # plays Tic_Tac_Toe
    
    display_board()
    #current_player = input("choose X or O: ")

    
    # continues while the game is still going
    while game_is_still_going:
        
        # handles the turn of the current player by updating the board
        handle_turn(current_player)
        
        # checks if the game is over via a win or tie
        check_if_game_over()
                
        # if the game isn't over switch to other player's turn
        flip_player()
        
    # Game is Over
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")
    
    
def handle_turn(player):
    # Display's whose turn it is
    print(player + "'s turn")
    
    # Allows player @ their turn to place piece on board
    position = input("Choose a position from 1 - 9: ")
    
    valid = False
    while not valid:
        # make's sure player can put piece on board at a spot
        while position not in ["1", "2", "3", "4",
                            "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 - 9: ")
        
        position = int(position) - 1
        
        # checks if position isn't occupied. Otherwise forces player to try elsewhere on board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Try again")
    
    board[position] = player
    display_board()    

    
def check_if_game_over():
    check_for_winner()
    check_if_tie()

    
def check_for_winner():
    
    global winner
    
    # check rows
    row_winner = check_rows()
    # check cols
    col_winner = check_cols()
    # check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    
    return 


def check_rows():
    # Set up global variable
    global game_is_still_going 
    
    # check if any of the rows have the same value across
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
     
    # if any row has a match flag that there's a win
    if row_1 or row_2 or row_3:
        game_is_still_going = False
        
    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return 


def check_cols():
    # Set up global variable
    global game_is_still_going 
    
    # check if any of the columns have the same value across
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
     
    # if any column has a match flag that there's a win
    if col_1 or col_2 or col_3:
        game_is_still_going = False
        
    # Return the winner (X or O)
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return 


def check_diagonals():
    # Set up global variable
    global game_is_still_going 
    
    # check if any of the diagonals have the same value across
    dgn_1 = board[0] == board[4] == board[8] != "-"
    dgn_2 = board[2] == board[4] == board[6] != "-"
     
    # if any diagonal has a match flag that there's a win
    if dgn_1 or dgn_2:
        game_is_still_going = False
        
    # Return the winner (X or O)
    if dgn_1:
        return board[0]
    elif dgn_2:
        return board[2]
    return 


def check_if_tie():
    # global variables
    global game_is_still_going 

    # check if tie
    if "-" not in board:
        game_is_still_going = False
    return

     
def flip_player(): 
    # global variables
    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return 

        
play_game()
