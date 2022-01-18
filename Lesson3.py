# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(var1, var2):
    return var1 / var2

dividend = float(input('Введите делимое: '))
divider = float(input('Введите делитель: '))

try:
    print(division(dividend, divider))
except ZeroDivisionError:
    print('На ноль делить нельзя')

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def ShowUserInfo(name, surname, birthyear, city, email, phone):
    print(f'Здравствуйте {surname} {name} {birthyear} года рождения, проживающий в городе {city}. Контактные данные email: {email}, телефон: {phone}')

print('Будьте добры, укажите информацию о себе')
UserName = input('Имя: ')
UserSurname = input('Фамилия: ')
UserBirthyear = input('Год рождения: ')
UserCity = input('Город проживания: ')
UserEmail = input('email: ')
UserPhone = input('Телефон: ')

ShowUserInfo(name = UserName, surname = UserSurname, birthyear = UserBirthyear, city = UserCity, email = UserEmail, phone = UserPhone)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def TwoMaxArgSum(var1, var2, var3):
    li = [var1, var2, var3]
    MinArg = min(li)                                      # поиск минимального аргумента в списке
    MinArgCount = li.count(MinArg)                        # определение количества вхождений минимального аргумента в список

    if MinArgCount == 1:                                  # если минимальный по значению аргумент в списке встречается только 1 раз тогда удаляем его
        li.remove(MinArg)
        return sum(li)
    else:
        return None                                       # если минимальный по значению аргумент в списке встречается несколько раз то исходя из условия просто не наберётся два наибольших

FirstVar = float(input('Введите первый аргумент: '))
SecondVar = float(input('Введите второй аргумент: '))
ThirdVar = float(input('Введите третий аргумент: '))
result = TwoMaxArgSum(FirstVar, SecondVar, ThirdVar)

if type(result) != type(None):
    print(result)
else:
    print('Подсчёт невозможен т.к. наибольших аргументов менее двух')

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Функция реализована с помощью оператора **
def exponentiation1(basis, exponent):
    return basis ** (-exponent if exponent > 0 else exponent)     # защита от дурака

# Функция реализована с помощью цикла
def exponentiation2(basis, exponent):
    if exponent == 0:
        return 1
    else:
        if exponent < 0:
            exponent = -exponent                         # защита от дурака

        result = basis
        for i in range(1, exponent):
            result *= basis
        return 1/result

UserBasis = float(input('Введите основание степени: '))
UserExponent = int(input('Введите показатель степени: '))

print(f'Результат возведения {UserBasis} в степень {(-UserExponent if UserExponent > 0 else UserExponent)} равен {exponentiation1(UserBasis, UserExponent)}')
print(f'Результат возведения {UserBasis} в степень {(-UserExponent if UserExponent > 0 else UserExponent)} равен {exponentiation2(UserBasis, UserExponent)}')

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def SumOfNumberInString():
    result = 0
    flag = False

    while True:
        UserString = input('Введите строку чисел, разделенных пробелом или введите "n" если желаете прекратить ввод: ')

        if UserString.replace(' ', '').isdigit():              # если строка без пробелов состоит из чисел
            result += sum(map(int, UserString.split()))        # то проводим массовое суммирование (я надеюсь массовая обработка "под капотом" работает быстрее чем поэлементный перебор)
        else:
            li = UserString.split()                            # иначе проводим поэлементный разбор строки

            for elem in li:
                if elem.isdigit():
                    result += int(elem)
                else:
                    if elem.lower() == 'n':
                        flag = True                             # при встрече стоп-символа прекращаем дальнейшую обработку списка и ставим флаг на выход
                        break

        print(f'Сумма введённых чисел составляет {result}')

        if flag:
            break

SumOfNumberInString()

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(UserString: str):
    return UserString.title()                                # самый легкий способ


def int_func2(UserString: str):
    return UserString[0].upper() + UserString[1:]            #но наверное задача была научить нас писать свои функции, а не умело использовать встроенные


UserText = input('Введите строку из слов, разделенных пробелом где каждое слово состоит из латинских букв в нижнем регистре: ')

print('Первый способ')
li = list(map(int_func, UserText.split()))
print(" ".join(li))


print('Второй способ')
li2 = UserText.split()
for elem in li2:
    print(int_func2(elem), end=' ')