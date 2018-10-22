'''
Here , I defined the fucntions for make game (Tic Tac Toe)
'''

from random import randint


# Step =====> 1 :
def display_board(board):

	''' First Tab design the board:'''

    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Step ======> 2 :
def player_input():
	'''
	input X show player1 ==> X and player2 ==> O
	input O show player1 ==> O and player2 ==> X

	'''
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Step ========> 3:
def place_marker(board, marker, position):
	
	''' put marker in position of board '''

    board[position] = marker


# Step =========> 4:
def win_check(board, mark):

	''' check all posibility in board '''

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  
            (board[4] == mark and board[5] == mark and board[6] == mark) or  
            (board[1] == mark and board[2] == mark and board[3] == mark) or  
            (board[7] == mark and board[4] == mark and board[1] == mark) or  
            (board[8] == mark and board[5] == mark and board[2] == mark) or  
            (board[9] == mark and board[6] == mark and board[3] == mark) or  
            (board[7] == mark and board[5] == mark and board[3] == mark) or  
            (board[9] == mark and board[5] == mark and board[1] == mark))



# Step ======> 5 :
def choose_first():

	''' this function choose who first player '''

    if randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'



# Step ======> 6 :
def space_check(board, position):
	
	''' check space in board '''
    
    return board[position] == ' '




# Step ======> 7 :
def full_board_check(board):
	
	''' check board if found space in any position '''
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True



# Step ======> 8:
def player_choice(board):
	
	''' input position '''
    
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position



# Step ======> 9:
def replay():
	
	''' replay the game '''
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')