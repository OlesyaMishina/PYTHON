# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый 
# ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print ("Введите общее количество журавликов, кратное 6:")
whole = int(input())
if whole%6==0:
    print (f"{int(whole/6)} {int(whole/6*4)} {int(whole/6)}")
else:
    print ("Введенное число не кратно 6 :(")