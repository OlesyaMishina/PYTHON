# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

vowels = ['а', 'я', 'о', 'ё', 'е', 'и', 'ы', 'у', 'ю', 'э']
chant_list = input("Введите кричалку: ").lower().split()
count=lambda x: sum (1 for i in x if i in vowels)
rhyme=True
for i in range(len(chant_list)):
    if count(chant_list[0])!=count(chant_list[i]):
        print("Пам парам")
        rhyme=False
        break
if rhyme:
    print("Парам пам-пам")


