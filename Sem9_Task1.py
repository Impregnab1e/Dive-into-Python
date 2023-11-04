# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from random import randint


def ran_num(rnd_num, count_num):
    def guess():
        for i in range(count_num):
            input_num = int(input('введите число: '))
            if input_num > rnd_num:
                print('Меньше')
            elif input_num < rnd_num:
                print('Больше')
            else:
                print(rnd_num)
                return True
        return False

    return guess


# rnd = ran_num(4, 5)
print(ran_num(4, 5)())
