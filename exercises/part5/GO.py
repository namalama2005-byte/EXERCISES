def who_won(game_board: list):
    player1_count = 0
    player2_count = 0
    
    for row in game_board:          
        for value in row:           
            if value == 1:
                player1_count += 1
            elif value == 2:
                player2_count += 1
    

    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    else:
        return 0
    

board = [
    [1, 2, 1],
    [0, 1, 2],
    [2, 1, 0]
]

print(who_won(board))