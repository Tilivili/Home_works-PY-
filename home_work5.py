# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# mas = list()
# a = int(input("Введите первый элемент прогрессии : "))
# b = int(input("Введите разность прогрессии: "))
# c = int(input("Введите количество элементов прогрессии: "))
# for a in range(a,(a + c*b) - 1):
#     mas.append(a)
# print(mas[0:len(mas):b])

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# a = [int(i) for i in input("Введите числа: ").split()]
# min = int(input("Введите минимальное значение диапазона: "))
# max = int(input("Введите максимальное значение диапазона: "))
# b = set(range(min,max + 1))
# mas_diap = set()
# for i in a:
#     if i in b:
#         mas_diap.add(i)
# print(mas_diap)





