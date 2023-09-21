# Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# list_1 = list()
# for i in range(5):
#     n = int(input("Input number: "))
#     list_1.append(n)
# uniq_numbers = set(list_1)
# print(len(uniq_numbers))

# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# N = [1, 2, 3, 4, 5]
# k = int(input("Введите число: "))
# def cyclic_shift(N, k):
#     return N[k:] + N[:k]
# print(cyclic_shift(N, k))

# n = [1, 2, 3, 4, 5]
# k = int(input("Введите число: "))
# result = []
# result = n[k:] + n[:k]
# print(result)

# Задача21.Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}] 

# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# uniques = set()
# for i in dict:
#     print(i)
#     uniques.add(list(i.values())[0])
# print(uniques)

# Задача №23. Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 

# import random
# N = int(input("Введите число элементов в массиве: "))
# A = random.sample(range(1, 11), N)
# count = 0
# for i in range(1, len(A)):
#     if A[i - 1] < A[i]:
#         count += 1
# print(A)
# print(count)











