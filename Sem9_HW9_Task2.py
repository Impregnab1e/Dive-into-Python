# Создаем файл с функциями
with open("__init__.py", "w") as init_file:
    init_file.write("""
def save_to_json():
    pass

def find_roots():
    pass

def generate_csv_file():
    pass
""")

# Загружаем код из файла __init__.py
with open("__init__.py", "r") as init_file:
    code = init_file.read()

# Проверяем наличие функций в файле
function_names = [
    "def save_to_json",
    "def find_roots",
    "def generate_csv_file"
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")
