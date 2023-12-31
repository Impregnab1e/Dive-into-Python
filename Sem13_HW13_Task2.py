from typing import Union


class InvalidTextError(Exception):
    """Исключение, возникающее при некорректных текстовых записях."""

    def __init__(self, text):
        self.text = text
        super().__init__(
            f"Invalid text: {text}. Text should be a non-empty string.")


class InvalidNumberError(Exception):
    """Исключение, возникающее при некорректных числовых записях."""

    def __init__(self, number):
        self.number = number
        super().__init__(
            f"Invalid number: {number}. Number should be a positive integer or float.")


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            if cls._instance.text:
                cls._instance.archive_text.append(cls._instance.text)
            if cls._instance.number:
                cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or not text:
            raise InvalidTextError(text)
        if not (isinstance(number, int) and number > 0) and not (isinstance(number, float) and number > 0):
            raise InvalidNumberError(number)
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'