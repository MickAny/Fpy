# 8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
#   Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
#   Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#   Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#   Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека.
#   Берем первое совпадение по фамилии.
#   Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#   Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

from os.path import join, abspath, dirname, exists

def input_data() -> list:
    user = []
    user.append(input("Input first name "))
    user.append(input("Input second name "))
    user.append(input("Input phone "))
    user.append(input("Input description "))
    return user

def create(phone_dir_local: dict, cntr: int, user: list) -> tuple:
    cntr += 1
    phone_dir_local[cntr] = user
    return phone_dir_local, cntr


def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.txt')
    with open(full_name, mode='w', encoding='utf-8') as file:
        for idc, user in phone_dir.items():
            file.write(f"{idc}#{user[0]}#{user[1]}#{user[2]}#{user[3]}\n")


def search_user(phone_dir_local: dict, searching: str) -> int:
    for idc, user in phone_dir_local.items():
        lastname: str = user[0]
        if lastname.upper().startswith(searching.upper()):
            return idc
    return 0


def print_dict(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}: {user[0]} {user[1]} {user[2]} {user[3]}")

def import_phone_dir(phone_dir, file_name):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, f"{file_name}.txt")
    if not exists(full_name):
        print("Error! File not found.")
        return
    idc = 0
    phone_dir = dict()
    with open(full_name, mode='r', encoding='utf-8') as file:
        for line in file:
            lst = line.strip().split('#')[1:]
            phone_dir, idc = create(phone_dir, idc, lst)
    return phone_dir, idc


def delete_user(phone_dir_local: dict, del_index: int) -> bool:
    result = phone_dir_local.pop(del_index, [0])
    if result == 0:
        print("Not found")
        return False
    print(f"{result} удалено")
    return True


def update_user(phone_dir_local: dict, upd_index: int):
    user = input_data()
    phone_dir_local[upd_index] = user
    print(f'{phone_dir_local[upd_index]} is updated')


def menu():
    key_count = 0
    phone_dir = dict()
    while True:
        expl()
        user_command = int(input("Выберите операцию: "))
        if user_command == 8:
            break
        if user_command == 1:
            data = input_data()
            phone_dir, key_count = create(phone_dir, key_count, data)
        if user_command == 2:
            print_dict(phone_dir)
        if user_command == 3:
            searching = input("Кого ищем? ")
            cntr = search_user(phone_dir, searching)
            if cntr == None:
                print("Not found")
        if user_command == 4:
            data = input("Номер записи или фамилия: ")
            cntr = 0
            if data.isdigit():
                cntr = int(data)
            else:
                cntr = search_user(phone_dir, data)
                if cntr == 0:
                    key_count += 1
                    cntr = key_count
            update_user(phone_dir, cntr)
        if user_command == 5:
            file_name = input("Введите имя файла: ")
            export_phone_dir(phone_dir, file_name)
        if user_command == 6:
            file_name = input("Введите имя файла: ")
            phone_dir, key_count = import_phone_dir(phone_dir, file_name)
            print(f"Импортировано {key_count} записей")
        if user_command == 7:
            id_delete = int(input("Номер удаляемой записи(0-отмена): "))
            if id_delete != 0:
                delete_user(phone_dir, id_delete)

def expl():
    print('Введите:')
    print('"1" чтобы добавить запись в список')
    print('"2" для вывода программы')
    print('"3" для поиска записи в списке')
    print('"4" чтобы изменить запись')
    print('"5" для экспорта программы')
    print('"6" для импорта программы')
    print('"7" для удаления записи')
    print('"8" для выхода из программы')


key_count = 0
phone_dir = dict()

menu()

# def menu():
#     key_count = 0
#     phone_dir = dict()
#     while True:
#         expl()
#         match(input("Выберите операцию: ")):
#          case 8:
#             break
#          case 1:
#             data = input_data()
#             phone_dir, key_count = create(phone_dir, key_count, data)
#          case 2:
#             print_dict(phone_dir)
#          case 3:
#             searching = input("Кого ищем? ")
#             cntr = search_user(phone_dir, searching)
#             if cntr == None:
#                 print("Not found")
#          case 4:
#             data = input("Номер записи или фамилия: ")
#             cntr = 0
#             if data.isdigit():
#                 cntr = int(data)
#             else:
#                 cntr = search_user(phone_dir, data)
#                 if cntr == 0:
#                     key_count += 1
#                     cntr = key_count
#             update_user(phone_dir, cntr)
#          case 5:
#             file_name = input("Введите имя файла: ")
#             export_phone_dir(phone_dir, file_name)
#          case 6:
#             file_name = input("Введите имя файла: ")
#             phone_dir, key_count = import_phone_dir(phone_dir, file_name)
#             print(f"Импортировано {key_count} записей")
#          case 7:
#             id_delete = int(input("Номер удаляемой записи(0-отмена): "))
#             if id_delete != 0:
#                 delete_user(phone_dir, id_delete)