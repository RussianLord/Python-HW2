# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

N = input('Введите число... ')
sum = 0
if ',' in N:
    listN = N.split(',')
    for N in str(listN[0]):
        sum = sum + int(N)
    for N in str(listN[1]):
        sum = sum + int(N) 
else:
    listN = [N]
    for N in str(N):
        sum = sum + int(N)   
print(f'Сумма чисел числа {str(listN)[1:-1]} = {sum}')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите число N... '))
# S = 1
# if N < 0:
#     N *= (-1)
#     for i in range(1, N):
#         S = S * i
#         print(S, end=' , ')
#     print(S * N)
# else:
#     for i in range(1, N):
#         S = S * i
#         print(S, end=' , ')
#     print(S * N)
    

# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# N = int(input('Введите число N... ')) 
# S = 1
# if N == 0:
#     print('Нельзя использовать ноль!')
# elif N < 0:
#     N *= (-1)
#     for i in range(1, N):
#         S = S + round((1 + 1 / N) ** N, 0)
#         print(i , ' = ' , S, end=' , ')
#     print(N , ' = ' , S + round((1 + 1 / N) ** N, 0))
# else:
#     for i in range(1, N):
#         S = S + round((1 + 1 / N) ** N, 0)
#         print(i , ' = ' , S, end=' , ')
#     print(N , ' = ' , S + round((1 + 1 / N) ** N, 0))

# 4. Реализуйте алгоритм перемешивания списка.

# import random
# listN = list(input())
# print('Оригинальный список ==>> ', listN)
# random.shuffle(listN)
# print('Перемешанный список ==>> ', listN)
