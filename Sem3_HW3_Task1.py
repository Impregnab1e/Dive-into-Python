# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

input_list = [1, 2, 3, 1, 2]
duplicates_list = []

unique_elements = set()

for item in input_list:
    if item in unique_elements:
        duplicates_list.append(item)
    unique_elements.add(item)

print(duplicates_list)