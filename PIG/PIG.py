import random


def roll():
    max_value = 6
    min_value = 1
    value = random.randint(min_value, max_value)
    return value


while True:
    players = input('enter number of players : ( 2 - 4 ) ? ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('must be between 2 - 4')
    else:
        print('invalid !')

players_score = [0 for player in range(players)]
win_score = 30
while max(players_score) < win_score:
    for player_index in range(players):
        print(f"\nit's player {player_index + 1} turn")
        print(f'your total score is {players_score[player_index]} \n')
        current_score = 0
        while True:
            wanna_roll = input('\nDo you Do you :D wanna roll ? ( y/n )').lower()
            if wanna_roll != 'y':
                break
            value = roll()
            if value == 1:
                print("You rolled a 1!!!")
                print('------------------------------------------')
                current_score = total_value = 0

                break
            else:
                current_score += value
                total_score = current_score + players_score[player_index]
                print(f'you rolled {value} value')
            print(f'your total score is {total_score}')
            print('------------------------------------------')
            if total_score >= win_score:
                break
        players_score[player_index] += current_score
        print(f'player {player_index + 1} your total score is {players_score[player_index]}')
        if players_score[player_index] >= win_score:
            break
max_score = max(players_score)
max_player_idx = players_score.index(max_score)
print(f'the player {max_player_idx + 1} is winner with score :{max_score}')
