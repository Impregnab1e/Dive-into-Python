from datetime import datetime

class MyStr(str):
    def __new__(cls, value, author):
        instance = super(MyStr, cls).__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    def __str__(self):
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"
    
    def __repr__(self):
        return f"MyStr({super().__repr__()}, '{self.author}')"

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))