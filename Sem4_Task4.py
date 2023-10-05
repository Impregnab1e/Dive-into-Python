# Функция получает на вход список чисел. 
# Отсортируйте его элементы in place без использования 
# встроенных в язык сортировок. 
# Как вариант напишите сортировку пузырьком. 
# Её описание есть в википедии.

def sort_list(list_: list[int]):
    for i in range(len(list_)):
        for j in range(i, len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]


list_ = [12, 34, 345, 54, 23, 67, 532, 33, 4, 6]
sort_list(list_)
print(list_)
