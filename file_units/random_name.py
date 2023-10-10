from random import randint
VOWELS = "AEYUIOaeuioy"


def generate_random_name():
    name_len = randint(4, 7)
    while True:
        name = ""
        for i in range(name_len):
            name += chr(randint(65, 90))
        for i in name:
            if i in VOWELS:
                return name.capitalize()