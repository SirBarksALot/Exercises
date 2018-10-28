change_dict = {'rock': 1, 'paper': 2, 'scissors': 3}

def check_battle(choice1, choice2):
    choice = choice1 - choice2
    winner = 0
    
    if choice == 0:
        print 'Overtime!'
    elif choice == -1:
        winner = 2
    elif choice == -2:
        winner = 1
    elif choice == 1:
        winner = 1
    elif choice == 2:
        winner = 1
    else:
        'Sth went wrong!'
    if winner != 0:
        print 'And the winner is player:  ', winner

while True:
    player_1 = raw_input('Choose your item player1 [rock/paper/scissors]:  ')
    player_2 = raw_input('Choose your item player2 [rock/paper/scissors]:  ')

    player_1_choice = change_dict.get(player_1)
    player_2_choice = change_dict.get(player_2)
        
    check_battle(player_1_choice, player_2_choice)
