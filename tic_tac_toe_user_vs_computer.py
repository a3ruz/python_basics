from IPython.display import clear_output

def display_board(board):
    clear_output()
    print (board[1]+'|'+board[2]+'|'+board[3])
    print (board[4]+'|'+board[5]+'|'+board[6])
    print (board[7]+'|'+board[8]+'|'+board[9])

def player_input():
    marker=''
    while not (marker=='X' or marker=='O'):
        marker=input('USER want to be X or O?').upper()
    if marker=='X':
        return ('X','O')
    if marker=="O":
        return ('O','X')
    
    
def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board,mark):
    return ( board[1]==board[2]==board[3]==mark or
             board[4]==board[5]==board[6]==mark  or
             board[7]==board[8]==board[9]==mark  or
             board[1]==board[4]==board[7]==mark  or
             board[2]==board[5]==board[8]==mark  or
             board[3]==board[6]==board[9]==mark  or
             board[1]==board[5]==board[9]==mark  or 
             board[3]==board[5]==board[7]==mark )

import random 
def choose_first():
    flip=random.randint(0,1)
    
    if flip==1:
        return 'USER'
    else: 
        return 'COMPUTER'

def space_check(board,position):
    if(board[position]!=' '):
        print('Selected Position not empty')
    return board[position]==' '

def full_boardcheck(board):
    for i in range (1,10):
        if space_check(board,i):
            return False
    return True 

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
         position=int(input('Please choose a position from 1-9 '))
    return position

def computer_choice(board): 
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
         position=random.randint(1,9)
    
    return position
    
def replay():
    return input('Restart the Game ? Yes or No: ').lower().startswith('y')
# GAME 
print('Welcome to TIK TAC TOE')
while True:
    #Play the game 
    #setup
    the_board=[' ']*10
    display_board(the_board)
    user_marker,computer_marker=player_input()
    turn=choose_first()
    print(turn+ ' will go first')
    game_on=input('Ready to PLAY ? Enter Yes or No: ').lower().startswith('y')
    

    
 ## GAME PLAY 
    while game_on:
        ## Player 1 turn 
        if turn=='USER':
            display_board(the_board)
        #choose position
            position=player_choice(the_board)
            place_marker(the_board,user_marker,position)

            if win_check(the_board,user_marker):
                display_board(the_board)
                print ('USER WON')
                game_on=False
            else:
                if(full_boardcheck(the_board)):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on=False
                else:
                    turn='COMPUTER'





        ## COMPUTER TURN 
        else:
            position=computer_choice(the_board)

            place_marker(the_board,computer_marker, position)

            if win_check(the_board,computer_marker):
                display_board(the_board)
                print ('COMPUTER WON')
                game_on=False
            else:
                if(full_boardcheck(the_board)):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on=False

                else:
                        turn='USER'



    if not replay():
        break

#Break out the while loopbre