# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('lesson5_1.txt', 'w') as f:
    while True:
        new_record = input('Введите новую строку (пустая строка - окончание ввода): ')
        if len(new_record) == 0:
            break
        else:
            new_record += '\n'
            f.write(new_record)

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('lesson5_2.txt', 'r') as f:
    text = f.readlines()

print(f'Всего в тексте {len(text)} строк')
for el in text:
    el = el.replace("\n", "")
    print(f'В строке "{el}" {len(el.split())} слов')

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def check_salary(salary: str):                                                          # функция проверки параметра зарплата
    if salary.isdigit():                                                                # проверка параметра на целое число
        return int(salary)
    elif len(salary.split('.')) == 2 and all(j.isdigit() for j in salary.split('.')):  # проверка параметра на дробь
        return float(salary)
    else:
        return None

with open('lesson5_3.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

poor_worker = []
total_salary = 0
worker_count = len(text)

for el in text:
    li = el.split()
    salary = check_salary(li[1])
    if isinstance(salary, int | float):
        if salary < 20000:
            poor_worker.append(el)

        total_salary += salary
    else:
        print(f'У работника {li[0]} некорректно введёна величина зарплаты {li[1]}')

if len(poor_worker) > 0:
    print('Перечень работников с зарплатой менее 20000')
    for i, el in enumerate(poor_worker, 1):
        print(i, el, end='')

if worker_count > 0 and total_salary > 0:
    print(f'Средняя величина дохода сотрудников {round(total_salary/worker_count, 2)}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

li = []

with open('lesson5_4.txt', 'r') as f:
    while True:
        content = f.readline()

        if not content:
            break
        else:
            if content.find('One') != -1:
                new_content = content.replace('One', 'Один')
            elif content.find('Two')  != -1:
                new_content = content.replace('Two', 'Два')
            elif content.find('Three') != -1:
                new_content = content.replace('Three', 'Три')
            else:
                new_content = content.replace('Four', 'Четыре')
            print(f'Исходная строка: {content}')
            print(f'Новая строка: {new_content}')

            li.append(new_content)

with open('lesson5_4_1.txt', 'w', encoding='utf-8') as wf:
    wf.writelines(li)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

random_number_count = 3                              # кол-во чисел в файле

with open('lesson5_5.txt', 'w+') as f:
    number_string = ''
    j = 0

    while j < random_number_count:
        i = randint(1, 1001)                         # генерирую псевдослучайным образом числа
        number_string += str(i) + ' '
        j += 1

    f.write(number_string)

    f.seek(0)
    text = f.readline()

print(f'Сумма чисел в файле равна: {sum(map(int, text.split()))}')

# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('lesson5_6.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

subject_dict = {}

for el in text:
    li = el.split()
    li = list(map(lambda var: var.replace('(л)', '').replace('(пр)', '').replace('(лаб)', ''), li))       #чищу от типа занятий
    subject_dict[str(li[0])[0:len(li[0]) - 1]] = sum(list(map(lambda var: int(var) if var.isdigit() else 0, li[1:4])))

print(subject_dict)

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

from json import dump

firm_with_income_counter = 0
total_income = 0
firm_dict = {}

with open('lesson5_7.txt', 'r', encoding='utf-8') as f:
    while True:
        content = f.readline()

        if not content:
            break
        else:
            li = content.split()
            if len(li) > 0:
                firm_income = int(li[2]) - int(li[3])          # вычисление прибыли

                if firm_income > 0:                            # в подсчёт средней прибыли по условию идут только фирмы с прибылью
                    firm_with_income_counter += 1
                    total_income += firm_income

                firm_dict[li[0]] = firm_income

average_profit = round(total_income / firm_with_income_counter, 2)
final_list = [firm_dict, {'average_profit': average_profit}]

with open('json5_7.json', 'w', encoding='utf-8') as fw:            # сериализация
    dump(final_list, fw)

#https://github.com/DemiurgXXX/DemiurgOnGeekBrains/pull/5
