n = int(input("Введите число: "))

hex_result = hex(n)
print("Шестнадцатеричное представление (с использованием hex()):", hex_result)

symbols = '0123456789ABCDEF'
result = ""
while n != 0:
    result = symbols[n % 16] + result
    n //= 16

print("Шестнадцатеричное представление (без использования hex()):", result)

if hex_result[2:].upper() == result:
    print("Результаты совпадают.")
else:
    print("Результаты не совпадают.")