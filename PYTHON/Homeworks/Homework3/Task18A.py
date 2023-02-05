# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i].
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

num = int(input("Введите количество элементов списка:"))
my_list = [0]*num
for i in range(len(my_list)):
    my_list[i] = int(input(f"Введите {i} элемент списка: "))
what_num = int(input("\nВведите число для поиска ближайшего к нему:"))
seach_num = []

# Находим первый элемент списка, отличный от заданного what_num
i = 0
while what_num == my_list[i]:
    i+=1
seach_num.append(my_list[i])

# находим минимальную разницу числа what_num с каждым элементом списка
for list in my_list:
    if list != what_num:
        if abs(list - what_num) < abs(seach_num[0] - what_num):
            seach_num[0] = list

# еще раз проходим по списку и ищем второй ближайший элемент         
for list in my_list:
    if list not in seach_num:
        if abs(list - what_num) == abs(seach_num[0] - what_num):
            seach_num.append(list)
 
print(f"Ближайшее число к числу {what_num} это {seach_num}.")
