# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


def list_create(text, n):
    numbers = []
    for char in text:
        if char.isdigit():
            numbers.append(int(char))
        if len(numbers) == n:
            break
    return (numbers)


size = list_create(text=input("Введите размеры наборов чисел: "), n=2)
print(size)
numbers1 = list_create(text=input(
    f"Введите первый набор из {size[0]} целых чисел: "), n=size[0])
print(numbers1)
numbers2 = list_create(text=input(
    f"Введите второй набор из {size[1]} целых чисел: "), n=size[1])
print(numbers2)

s1 = set(numbers1)
s2 = set(numbers2)
result = s1 & s2
result2 = sorted(list(result))
print(result2)
