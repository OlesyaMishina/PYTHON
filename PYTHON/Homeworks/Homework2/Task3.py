# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

import math

num = int(input("Введите натуральное число:"))
res = 1
i = 1
while res <= num:
    print(res, end=" ")
    res = int(math.pow(2, i))
    i += 1
