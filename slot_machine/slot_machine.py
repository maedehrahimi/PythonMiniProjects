import random

max_lines = 3
min_bet = 1
max_bet = 100

rows = 3
cols = 3

symbols_count = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5
}

symbols_values = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_wining(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_spin(rows, cols, symbols_count):
    all_symbols = []
    for symbol, symbol_count in symbols_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row])


def deposit():
    while True:
        amount = input('what would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('amount must be greater that 0')
        else:
            print('please enter a valid number : ')
    return amount


def get_number_of_lines():
    while True:
        lines = input(f'enter the number of lines that you bet on: (1-{max_lines})')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print('pls enter a valid number of lines.')
        else:
            print('please enter a valid number : ')
    return lines


def get_bet():
    while True:
        amount = input('how much you like to bet on each lines? $')
        if amount.isdigit():
            amount = int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f'amount must be between ${min_bet} - ${max_bet}')
        else:
            print('please enter a valid number : ')
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'you do not have enough to bet, tour current balance is = ${balance}')
        else:
            break
    print(f'you are betting ${bet} on {lines} lines. total bet is = ${total_bet}')
    slots = get_spin(rows, cols, symbols_count)
    print(print_slot_machine(slots))
    winnings, winning_lines = check_wining(slots, lines, bet, symbols_values)
    print(f'you won {winnings}.')
    print('you won on lines:', *winning_lines)


main()
