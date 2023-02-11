# Задача №35. Общее обсуждение
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_simple(div):
    if div == n:
        if div == 1:
            print(f"Число {n} является составным.")
            exit()
        else:
            div = n-1
    while div >= 2:
        # print(div)
        if n % (div) == 0:
            print(f"Число {n} является составным.")
            break
        else:
            return is_simple(div-1)
    else:
        print(f"Число {n} является простым.")


n = int(input("Введите n: "))
is_simple(n)
