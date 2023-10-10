num = input("Введите целое число: ")

if num.isdigit():
    num = int(num)

    if num <= 0 or num > 100000:
        print("Число не соответствует ограничениям")
    elif num <= 1:
        print("Число не является ни простым, ни составным")
    elif num == 2:
        print("Число простое")
    else:
        is_prime = "Простое"
        for i in range(2, num):
            if num % i == 0:
                is_prime = "Составное"
                break
        print(f"Число {is_prime}")
else:
    print("Некорректный ввод. Введите целое число.")