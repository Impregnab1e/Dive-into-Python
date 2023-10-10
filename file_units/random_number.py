from random import randint, uniform


def generate_random_numbers(count, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        for i in range(count):
            f.write(f'{randint(-1000, 1000)} /{uniform(-1000,1000)} \n')

def random_name_in_file(count, file_name):
    with open(file_name, "a") as f:
        for i in range(count):
            f.write(generate_random_numbers()+"\n")