import random

playing_answer = input('Do you Do you wanna PLAY :D ? (y/n)').lower()
if playing_answer != 'y':
    quit()

options = ['rock', 'paper', 'scissors']
time_play_user = int(input('how many times do you wanna play? '))
time_play = 0
user_wins = 0
computer_wins = 0

while time_play < time_play_user:
    time_play += 1
    user_move = input('rock, paper or scissors?  ').lower()
    random_number = random.randint(0,2)
    computer_move = options[random_number]
    print(f'computer chose {computer_move}')
    if user_move == computer_move:
        print('same chosen :( , again ', end='')
        time_play -= 1
        continue
    elif user_move == 'rock' and computer_move == 'scissors':
        print('you won :D')
        user_wins += 1
    elif user_move == 'paper' and computer_move == 'rock':
        print('you won :D')
        user_wins += 1
    elif user_move == 'scissors' and computer_move == 'paper':
        print('you won :D')
        user_wins += 1
    else:
        print('you lost :(')
        computer_wins += 1
print('----------------------------------------')
print(f"you wins '{user_wins}' times and computer wins '{computer_wins}' times")
if user_wins > computer_wins:
    print('congratulations!!! YOU are the winner')
elif user_wins < computer_wins:
    print('sorry :(')
else:
    print('you are got equal score')
