book_name = 'phone_book.txt'


def work_with_phone_book():

    choice = show_menu()

    while True:
        if choice == 1:
            show_phone_book(book_name)
        elif choice == 2:
            name = input("Введите имя, фамилию или номер пользователя: ")
            find_user(name)
        elif choice == 3:
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            number = input("Введите телефон: ")
            print(add_user(book_name,last_name,first_name, number))
        else:
            return print("Программа остановленна ")
        
        choice = show_menu()


def show_menu():
    print("\nВыберите функцию:\n"
          "1. Показать справочник\n"
          "2. Найти абонента\n"
          "3. Добавить абонента")
    choice = int(input("Введите номер: "))
    return choice

def show_phone_book(book_name):
    fields = ['Фамилия', 'Имя', 'Номер']
    with open(book_name, 'r', encoding='utf-8') as book:
        for line in book:
            record = dict(zip(fields, line.split()))
            print(*record.values())
            # print(record)
        return 


def find_user(charachteristic):
    with open(book_name, 'r', encoding='utf-8') as data:
        charachteristic.lower()
        result = list()
        for i in data:
            if charachteristic.lower() in i.lower():
                result.append(i.split())
        if len(result) > 0 :
            return print(*result)
        else:
            return print("\nПользователь не найден")


def add_user(phone_book, last_name, fisrt_name, number):
    names = [last_name, fisrt_name, number]
    with open(book_name, 'a', encoding='utf-8') as data_book:
        data_book.write('\n')
        for i in  range(len(names)):
            data_book.write(names[i] + ' ')
    return phone_book

work_with_phone_book()








        
