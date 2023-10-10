import random


def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


def generate_boards():
    board_list = []
    while len(board_list) < 4:
        queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if check_queens(queens):
            board_list.append(queens)
    return board_list


for board in generate_boards():
    print(board)
