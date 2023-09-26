# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def step(a, b, count , res):
    if b == 0:
        return 1
    if b == 1:
        return a
    if count == 0:
        res = a * a
        count += 1
        return step(a, b, count, res)
    elif count != (b-1) and count > 0:
        res = res * a
        count += 1
        return step(a, b, count, res)
    else:
        return res
    
# a = int(input())
# b = int(input())
# print(step(a, b, count = 0, res = 0))

def step(a,b):
    if b == 0:
        return 1
    return a * step(a,b - 1) 
a = int(input())
b = int(input())
print(step(a,b))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):
    if a == 0:
        return b
    return sum(a - 1, b + 1)

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))

# print(sum(a, b))
