# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# a = set()
# b = set()
# n = int(input("Введите длину множества a: "))
# m = int(input("Введите длину множества b: "))
# for i in range(n):
#     x = int(input("Введите число из множества a: "))
#     a.add(x)
# for i in range(m):
#     y = int(input("Введите число из множества b: "))
#     b.add(y)
# c = a.intersection(b)
# print(f'Общими элементами множеств {a} и {b} являются элементы {c}')