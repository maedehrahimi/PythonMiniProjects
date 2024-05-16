import random

random_number = random.randint(0, 10)
guesses_time = 0
while True:
    input_number = input('enter a number that you guess: ')
    guesses_time += 1
    if input_number.isdigit():
        input_number = int(input_number)
    else:
        print('again ', end='')
        continue
    if input_number == random_number:
        print('congratulation!!!')
        break
    elif input_number > random_number:
        print("it's above the number")
    else:
        print("it's below the number")

print(f'you got in {guesses_time} guess')
