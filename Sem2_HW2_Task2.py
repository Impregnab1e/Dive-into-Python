# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

fraction_str1 = input("Введите первую дробь a/b: ")
fraction_str2 = input("Введите вторую дробь a/b: ")

numerator1, denominator1 = map(int, fraction_str1.split('/'))
numerator2, denominator2 = map(int, fraction_str2.split('/'))

sum_numerator = (numerator1 * denominator2) + (numerator2 * denominator1)
product_numerator = numerator1 * numerator2
product_denominator = denominator1 * denominator2

print(f"Сумма без fractions: {sum_numerator}/{denominator1 * denominator2}")
print(f"Произведение без fractions: {product_numerator}/{product_denominator}")

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

print(f"Сумма с fractions: {fraction1 + fraction2}")
print(f"Произведение с fractions: {fraction1 * fraction2}")
