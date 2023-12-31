import re
from collections import Counter

text = """
Чебурашка — персонаж, придуманный писателем Эдуардом Успенским в 1966 году как
один из главных героев книги «Крокодил Гена и его друзья» и её продолжений.
После выхода мультфильма Романа Качанова «Крокодил Гена», снятого по этой
книге в 1969 году, персонаж стал широко известен.
"""

words = re.findall(r'\w+', text.lower())

word_count = Counter(words)

most_common_words = word_count.most_common(10)

print("Слова и их количество:")
for word, count in most_common_words:
    print(f"{word}: {count}")