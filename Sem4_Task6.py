# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# Если нижняя граница меньше нуля, суммируем от начала.
# Если верхняя граница больше длины списка, до конца.

def nums(numbers: list[int], start: int, stop: int) -> int:
    if start > stop:
        start, stop = stop, start
    if start < 0 or start > len(numbers):
        start = 0
    if stop > len(numbers) or stop < 0:
        stop = len(numbers)
    return sum(numbers[start:stop])


numbers = [4, 6, 1, 2, 5, 0, 3]
print(nums(numbers, 10, 20))
