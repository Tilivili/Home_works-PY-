# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# str1 = "a a a b c a a d c d d"
# str1 = str1.split()
# my_dict = {}
# for i in str1:
#     if i not in my_dict:
#         my_dict[i] = 1
#         print(i, end=" ")
#     else:
#         print(f'{i}_{my_dict[i]}', end=' ')
#         my_dict[i] += 1


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# str = '''She sells sea shells on the sea shore 
# The shells that she sells are sea shells I'm sure So if she 
# sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''.lower()
# str = set(str.split())
# print(len(str))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

n = int(input())
max_number = 1000
while n > 0:
 n = int(input())
 if max_number > n:
    max_number = n
print(max_number)












