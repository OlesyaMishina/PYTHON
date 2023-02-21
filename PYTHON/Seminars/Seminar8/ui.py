from logger import input_data, print_data, filter_data

def interface():
    print("""Выберите режим работы:
             1 - запись данных
             2 - вывод данных
             3 - посик данных по парметрам
             """)
    command_number = int(input("Введите номер комманды: "))
    while command_number < 1 or command_number > 3:
        print("Введите корректный номер комманды:")
        command_number = int(input("Введите номер комманды: "))

    if command_number == 1:
        input_data()
    elif command_number == 2:
        print_data()
    elif command_number == 3:
        print("Введите параметры поиска через ';' :")
        filter_string = input()
        # print(filter_string)
        filter_data(filter_string)
