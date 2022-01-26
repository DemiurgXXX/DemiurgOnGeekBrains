# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

li = [1, 3.14, 'Hello World', True, ['H', 'e', 'l', 'l', 'o'], (1, 'World', False), {1: 'один', 2: 'два', 3: 'три'}, None ]

for elem in li:
    print(type(elem))

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

li = input('Введите элементы списка через пробел: ').split()
print(f'Изначальный список:  {li}')
length = len(li)                      # чтобы при длинном списке всё время не запрашивать его длинну

for i in range(0, length, 2):
    if i + 1 < length:
        li[i], li[i+1] = li[i+1], li[i]

print(f'Список после обмена: {li}')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# list
li = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
MonthNumber = int(input('Введите номер месяца: '))

if 1 <= MonthNumber <= 12:
    print(li[MonthNumber - 1])
else:
    print('Месяца с таким номером не существует')

# # dict
di = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь' }
MonthNumber = int(input('Введите номер месяца: '))

if 1 <= MonthNumber <= 12:
    print(di.get(MonthNumber))
else:
    print('Месяца с таким номером не существует')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

li = input('Введите строку из нескольких слов, разделённых пробелами: ').split()

for i, elem in enumerate(li, 1):
    print(i, elem[:10] if len(elem) > 10 else elem)

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде

my_list = [7, 5, 3, 3, 2]
flag = False

while True:
    NewElem = input('Введите новый элемент рейтинга (или exit для выхода): ')
    flag = False

    if NewElem.isdigit():
        NewElem = int(NewElem)

        for i in range(0, len(my_list)):                # проходим по индексам элементов списка (знать индекс нужно для вставки в середину)
            if NewElem > my_list[i]:                    # если новый введённый элемент меньше текущего
                my_list.insert(i, NewElem)              # производим вставку перед меньшим (обыгрываем ситуацию с размещением нового элемента после существующих элементов с одинаковыми значениями)
                flag = True                             # помечаем что вставка нового элемента была произведена
                break

        if flag == False:                               # если прошёл по всему списку а вставку так и не произвёл (список пуст или введён минимальный по значению элемент)
            my_list.append(NewElem)
    else:
        if NewElem == 'exit':
            break
        else:
            print('Новый элемент не является цифрой или словом exit')

    print(my_list)

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

ProductList = list()
ProductNumber = 0

while True:
    ProductNumber += 1

    product = dict()
    product['название'] = input('Наименование: ')
    product['цена'] = float(input('Цена: '))
    product['количество'] = int(input('Количество: '))
    product['eд'] = input('Единица измерения: ')

    ProductRecord = (ProductNumber, product)
    ProductList.append(ProductRecord)

    flag = input('Прекратить ввод "y" ? : ')

    if flag == 'y':
        break

NameList = list()
PriceList = list()
CountList = list()
UnitList = list()

for elem in ProductList:
    NameList.append(elem[1].get('название'))
    PriceList.append(elem[1].get('цена'))
    CountList.append(elem[1].get('количество'))
    UnitList.append(elem[1].get('eд'))

ResultDict = {'название': list(set(NameList)), 'цена': list(set(PriceList)), 'количество': list(set(CountList)), 'eд': list(set(UnitList))}

print(ResultDict)

# https://github.com/DemiurgXXX/DemiurgOnGeekBrains/pull/2