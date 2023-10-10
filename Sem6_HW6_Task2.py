def is_attacking(q1, q2):
    x1, y1 = q1
    x2, y2 = q2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def check_queens(queens):

    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


if __name__ == "__main__":
    queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
    result = check_queens(queens)
    # print(result)

