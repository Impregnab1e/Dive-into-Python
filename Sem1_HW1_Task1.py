a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Треугольник с такими сторонами не существует")
elif a == b == c:
    print("Треугольник равносторонний")
elif a != b and b != c and c != a:
    print("Треугольник разносторонний")
elif a == b or b == c or c == a:
    print("Треуольник равнобедренный")
