# 3. Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в
# рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def select_items(inventory, total_weight):
    selected_items = []

    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)

    current_weight = 0
    for inventory, weight in sorted_items:
        if current_weight + weight <= total_weight:
            selected_items.append(inventory)
            current_weight += weight

    return selected_items


items_for_hiking = {
    'карта': 1,
    'документы': 1,
    'горелка': 2,
    'еда': 5,
    'компас': 2,
    'палатка': 7,
    'спальник': 4
}

weight_backpack = 20

selected_items = select_items(items_for_hiking, weight_backpack)

print("Выбранные вещи для рюкзака:", selected_items)
