class Archive:
    _instance = None

    def __new__(cls, text, number):
        if cls._instance is None:
            cls._instance = super(Archive, cls).__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
            cls._instance.text = text
            cls._instance.number = number
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
            cls._instance.text = text
            cls._instance.number = number
        return cls._instance

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"

archive1 = Archive("First Text", 1)
archive2 = Archive("Second Text", 2)
archive3 = Archive("Third Text", 3)
print(archive1.archive_text)  # Выведет: ['First Text', 'Third Text']
print(archive1.archive_number)  # Выведет: [1, 3]
print(archive2.archive_text)  # Выведет: ['First Text', 'Second Text']
print(archive2.archive_number)
