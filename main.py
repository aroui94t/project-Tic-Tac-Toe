import app

# Test Step 1:

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# Test Step 2:
player1 , player2 = player_input()
print("Player1 :"+player1,"Player 2 :"+player2)

# Test Step 3 : 
# I will put first character name of friends on any position in board 
place_marker(test_board,'T',8)
place_marker(test_board,'H',7)
place_marker(test_board,'A',5)
place_marker(test_board,'M',6)
place_marker(test_board,'N',2)
place_marker(test_board,'K',1)
display_board(test_board)


# Test Step 4 :
print(win_check(test_board,'O'))