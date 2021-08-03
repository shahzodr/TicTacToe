space = " "
xt = "X"
ot = "O"
min_coord = 1
max_coord = 3

empty_board = "         "

def display_board(board):
    print ("---------")
    for row in board:
        print ('|', end=' ')
        print (' '.join(row), end=' ')
        print ('|', end=' ')
        print()
    print ("---------")

def check_status():
    # For the horizontal X
    xh = False
    for row in board:
        if set(row)=={xt}:
            xh = True
    
    # For the vertical X
    xv = False
    for i in range(len(board)):
        column = [board[n][i] for n in range(len(board[0]))]
        if set(column)=={xt}:
            xv = True

    # For the diagonal X
    xd = False
    diag_down = [board[i][i] for i in range(len(board))]
    diag_up = [board[i][-(i+1)] for i in range(len(board))]
    if set(diag_down)=={xt}:
        xd = True
    if set(diag_up)=={xt}:
        xd = True
    
    # if|else for the X
    x = False
    if xh:
        x = True
    elif xv:
        x = True
    elif xd:
        x = True
        
    # For the horizontal O
    oh = False
    for row in board:
        if set(row)=={ot}:
            oh = True
    
    # For the vertical O
    ov = False
    for i in range(len(board)):
        column = [board[n][i] for n in range(len(board[0]))]
        if set(column)=={ot}:
            ov = True
    
    # For the diagonal O
    od = False
    diag_down = [board[i][i] for i in range(len(board))]
    diag_up = [board[i][-(i+1)] for i in range(len(board))]
    if set(diag_down)=={ot}:
        od = True
    if set(diag_up)=={ot}:
        od = True
    
    # if|else for the O
    o = False
    if oh:
        o = True
    elif ov:
        o = True
    elif od:
        o = True
    
    # if|else for the winning conditions
    if x and not o:
        return "X wins"
    elif o and not x:
        return "O wins"
    elif x and o:
        return "Impossible"
    elif not x and not o and not (any(space in i for i in board)):
        return "Draw"
    else:
        return "None"

board = [list(empty_board[i*3:i*3+3]) for i in range(3)]
display_board(board)

active = True
while active:
    x_input = input("Enter the coordinates: ")
    player_x = []
    
    if x_input[0].isnumeric() and x_input[2].isnumeric():
        player_x = [int(i) for i in x_input.split()][::-1]
        #player_x = [int(i) for i in x_input.split()]
    else:
        print("You should enter numbers!")
        continue
    
    if any(y > max_coord for y in player_x) or any(y < min_coord for y in player_x):
        print("Coordinates should be from 1 to 3!")
        continue
        
    player_x[0] -= 1
    player_x[1] -= 1
    
    if board[player_x[0]][player_x[1]] == space:
        board[player_x[0]][player_x[1]] = xt
        display_board(board)
        
        result = check_status()
        if result != "None":
            print(result)
            active = False
            break
        else:
            o_input = input("Enter the coordinates: ")
            player_o = []
            
            if o_input[0].isnumeric() and o_input[2].isnumeric():
                player_o = [int(i) for i in o_input.split()][::-1]
                #player_o = [int(i) for i in o_input.split()]
            else:
                print("You should enter numbers!")
                continue
            
            if any(y > max_coord for y in player_o) or any(y < min_coord for y in player_o):
                print("Coordinates should be from 1 to 3!")
                continue
                
            player_o[0] -= 1
            player_o[1] -= 1
            
            if board[player_o[0]][player_o[1]] == space:
                board[player_o[0]][player_o[1]] = ot
                display_board(board)
                
                result = check_status()
                if result != "None":
                    print(result)
                    active = False
                    break
                else:
                    continue
            else:
                print("This cell is occupied! Choose another one!")
    else:
        print("This cell is occupied! Choose another one!")
    