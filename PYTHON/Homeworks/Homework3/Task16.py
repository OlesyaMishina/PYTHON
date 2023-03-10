# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. Пользователь в
# первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i].
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

num = int(input("Введите количество элементов списка:"))
my_list = [0]*num
for i in range(len(my_list)):
    my_list[i] = int(input(f"Введите {i} элемент списка: "))
search_num = int(input("\nВведите искомое число:"))

# Если число не в списке
while search_num not in my_list:
    search_num = int(input("В списке нет введенного числа. Введите число еще раз:"))

# считаем сколько раз встречается число
count = 0
for list in my_list:
    if list == search_num:
        count += 1
print(f"Число {search_num} встречается {count} раз.")
