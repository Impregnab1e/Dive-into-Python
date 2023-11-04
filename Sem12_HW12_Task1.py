import warnings
warnings.filterwarnings('ignore')

import csv

class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file, encoding='utf-8')

    def load_subjects(self, subjects_file, encoding='utf-8'):
        with open(subjects_file, mode='r', encoding=encoding) as file:
            reader = csv.reader(file)
            for row in reader:
                for subject in row:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject in self.subjects:
            if 2 <= grade <= 5:
                self.subjects[subject]['grades'].append(grade)
            else:
                print("Оценка должна быть целым числом от 2 до 5")
        else:
            print(f"Предмет {subject} не найден")

    def add_test_score(self, subject, test_score):
        if subject in self.subjects:
            if 0 <= test_score <= 100:
                self.subjects[subject]['test_scores'].append(test_score)
            else:
                print("Результат теста должен быть целым числом от 0 до 100")
        else:
            print(f"Предмет {subject} не найден")

    def get_average_test_score(self, subject):
        if subject in self.subjects:
            scores = self.subjects[subject]['test_scores']
            if scores:
                return sum(scores) / len(scores)
            else:
                return 0
        else:
            print(f"Предмет {subject} не найден")
            return 0

    def get_average_grade(self):
        grades = [grade for subject in self.subjects for grade in self.subjects[subject]['grades']]
        if grades:
            return sum(grades) / len(grades)
        else:
            return 0

    def __str__(self):
        subjects_str = ', '.join(self.subjects.keys()) if self.subjects else "не найдены"
        return f"Студент: {self.name}\nПредметы: {subjects_str}"

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
