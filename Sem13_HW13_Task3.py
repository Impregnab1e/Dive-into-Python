class InvalidNameError(Exception):
    """Исключение, возникающее при некорректных данных о человеке."""

    def __init__(self, name):
        self.name = name
        super().__init__(f'Invalid name: . Name should be a non-empty string.')

class InvalidAgeError(Exception):
    """Исключение, возникающее при некорректном возрасте человека."""

    def __init__(self, age):
        self.age = age
        super().__init__(f'Invalid age: {age}. Age should be a positive integer.')

class InvalidIdError(Exception):
    """Исключение, возникающее при некорректном ID сотрудника."""

    def __init__(self, id):
        self.id = id
        super().__init__(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')

class Person:
    def __init__(self, name, surname, patronymic, age):
        if not all(isinstance(s, str) and s for s in [name, surname, patronymic]):
            raise InvalidNameError((name, surname, patronymic))
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age

    def get_age(self):
        return self.age

    def birthday(self):
        self.age += 1

class Employee(Person):
    def __init__(self, name, surname, patronymic, age, id):
        super().__init__(name, surname, patronymic, age)
        if not isinstance(id, int) or id < 100000 or id > 999999:
            raise InvalidIdError(id)
        self.id = id

    def get_level(self):
        return sum(int(digit) for digit in str(self.id)) % 7

person = Person("", "John", "Doe", 30)




print()