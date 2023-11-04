import warnings
import csv
import json
import random


def generate_csv_file(file_name, rows):
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['Value1', 'Value2', 'Value3']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(rows):
            value1 = random.randint(1, 1000)
            value2 = random.randint(1, 1000)
            value3 = random.randint(1, 1000)
            writer.writerow(
                {'Value1': value1, 'Value2': value2, 'Value3': value3})


def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return root1
    else:
        return None


def save_to_json(func):
    def wrapper(file_name):
        data = []

        with open(file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                a = int(row['Value1'])
                b = int(row['Value2'])
                c = int(row['Value3'])
                roots = func(a, b, c)
                data.append({'a': a, 'b': b, 'c': c, 'roots': roots})

        with open('results.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

    return wrapper


generate_csv_file("input_data.csv", 999)


@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return root1
    else:
        return None


generate_csv_file("input_data.csv", 1500)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data) == 1500)
