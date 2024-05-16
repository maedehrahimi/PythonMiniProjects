import random
import time

max_num = 11
min_num = 2
operators = ['+', '*', '-']
total_problem = 5
wrong_guesses = 0


def q_generation():
    left_num = random.randint(min_num, max_num)
    right_num = random.randint(min_num, max_num)
    operate = random.choice(operators)
    question = f'{left_num} {operate} {right_num}'
    answer = eval(question)
    return question, answer


input('press to start : ')
print('-----------------------------------------------')
start_time = time.time()

for i in range(total_problem):
    q, correct_answer = q_generation()
    while True:
        guessed = input(f'question number {i + 1} : {q} = ')
        if int(guessed) == correct_answer:
            break
        wrong_guesses += 1

end_time = time.time()
print('-----------------------------------------------')
print(
    f'you are answerd all {total_problem} questions with {wrong_guesses} wrong guess, and you end in {round((end_time - start_time), 2)} ')
print('nice job, good bye!')
