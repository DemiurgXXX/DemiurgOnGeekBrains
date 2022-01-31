# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, init_string: str):
        try:
            li = list(map(int, init_string.split('-')))
        except Exception:
            raise TypeError('Ошибка инициализации объекта класса: неверный формат строки инициализации!')

        if len(li) == 3 and Date.check_date_info(li[0], li[1], li[2]):
            return cls(li[0], li[1], li[2])
        else:
            raise TypeError('Ошибка инициализации объекта класса: неверные значения в строке инициализации!')

    @staticmethod
    def is_leap_year(year):                        # проверка года на високосность чтобы верно проверять 29 февраля
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    @staticmethod
    def check_date_info(day, month, year):
        if month < 1 or month > 12:
            return False
        elif day < 1 or day > 31:
            return False
        elif month in [4, 6, 9, 11] and day > 30:
            return False
        elif month == 2 and day > (29 if Date.is_leap_year(year) else 28):
            return False
        elif year < 1 or year > 9999:
            return False
        else:
            return True

    def __str__(self):
        return f'{self.day:02}-{self.month:02}-{self.year}'


try:
    d_err = Date.set_date('31-06-1855')
except Exception as e:
    print(e.args[0])

d1 = Date.set_date('01-02-1900')
print(d1)

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnZeroDivisionError (Exception):
    def __init__(self, text):
        self.text = text


def division (a, b):
    if b == 0:
        raise OwnZeroDivisionError('На 0 делить нельзя!')
    return a / b


try:
    dividend = float(input('Введите делимое: '))
    divider = float(input('Введите делитель: '))
    division(dividend, divider)
except ValueError as ve:
    print(f'ValueError: {ve.args[0]}')
except OwnZeroDivisionError as oe:
    print(oe)

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class OnlyDigitError(Exception):
    def __init__(self, text):
        self.text = text

li = []

while True:
    inp = input('Введите целое число (или stop для выхода): ')

    if inp.lower() != 'stop':
        try:
            if not inp.isdigit():
                raise OnlyDigitError('Вводить необходимо только целое число')
            else:
                li.append(int(inp))
        except OnlyDigitError as er:
            print(f'Ошибка ввода: {er}')
    else:
        break

print(f'Список чисел, которые вы ввели: {li}')

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


from abc import ABC, abstractmethod


class MyError(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, name, address, square):
        self.name = name
        self.address = address
        self.square = square
        self.equipment = {}

    def store_report(self):
        print(f'Сводный отчёт по хранимым на складе {self.name} материальным ценностям:')
        for k, v in self.equipment.items():
            print(f'{k} - {v} шт')


class OfficeEquipment(ABC):
    def __init__(self, brand, name, mass, long, width, height):
        self.brand = brand
        self.name = name

        if OfficeEquipment.check_param_isdigit([mass, long, width, height]):
            self.mass = mass
            self.long = long
            self.width = width
            self.height = height
        else:
            raise MyError('Линейные параметры оргтехники должны быть числами!')

    def __str__(self):
        return f'"{self.brand} {self.name}" Масса: {self.mass} кг. Габариты: {self.long}*{self.width}*{self.height}'

    @staticmethod
    def check_param_isdigit(param):
        for elem in param:
            if not isinstance(elem, (int, float)):
                return False

        return True

    @abstractmethod
    def create(self):
        pass

    def get_balance(self, obj):
        value = obj.equipment.get(self)
        return value if value is not None else 0

    def to_warehouse(self, obj, count):
        if count > 0:
            value = OfficeEquipment.get_balance(self, obj)
            obj.equipment[self] = value + count

            print(f'{self} успешно отправлен на склад {obj.name} в количестве {count} шт.')
            print(f'Текущее кол-во на складе: {OfficeEquipment.get_balance(self, obj)} шт')
        else:
            print('Верно укажите количество оприходуемого на склад товара')

    def from_warehouse(self, obj, count):
        if count > 0:
            value = OfficeEquipment.get_balance(self, obj)

        if value >= count:
            obj.equipment[self] = value - count
            print(f'{self} успешно списан со склада {obj.name} в количестве {count} шт.')
        else:
            print(f'Кол-во выписываемого со склада товара {self} больше того что есть в наличии')

        print(f'Текущее кол-во на складе: {OfficeEquipment.get_balance(self, obj)}  шт')


class Printer(OfficeEquipment):
    def __init__(self, brand, name, mass, long, width, height, printer_type):
        super().__init__(brand, name, mass, long, width, height)
        self.printer_type = printer_type

    def __str__(self):
        val = super().__str__()
        return f'Принтер {val} Тип: {self.printer_type}'

    @staticmethod
    def check_printer_type(printer_type):
        return printer_type in ['matrix', 'laser', 'termo']

    @classmethod
    def create(cls, brand, name, mass, long, width, height, printer_type):
        try:
            if not Printer.check_printer_type(printer_type):
                raise MyError(f'Принтер "{brand} {name}" неккорректного типа')
            else:
                return cls(brand, name, mass, long, width, height, printer_type)

        except MyError as e:
            print(f'Ошибка валидации данных Принтер: {e}')


class Monitor(OfficeEquipment):
    def __init__(self, brand, name, mass, long, width, height, diagonal):
        super().__init__(brand, name, mass, long, width, height)
        self.diagonal = diagonal

    def __str__(self):
        val = super().__str__()
        return f'Монитор {val} Диагональ: {self.diagonal} дюймов'

    @classmethod
    def create(cls, brand, name, mass, long, width, height, diagonal):
        try:
            if not OfficeEquipment.check_param_isdigit([diagonal]) or diagonal <= 0:
                raise MyError(f'У монитора "{brand} {name}" некоректно указано значение диагонали')
            else:
                return cls(brand, name, mass, long, width, height, diagonal)
        except MyError as e:
            print(f'Ошибка валидации данных Монитор: {e}')


class Telephone(OfficeEquipment):
    def __init__(self, brand, name, mass, long, width, height, phone_type):
        super().__init__(brand, name, mass, long, width, height)
        self.phone_type = phone_type

    @staticmethod
    def check_phone_type(phone_type):
        return phone_type in ['analog', 'digit']

    def __str__(self):
        val = super().__str__()
        return f'Телефон {val} Тип: {self.phone_type}'

    @classmethod
    def create(cls, brand, name, mass, long, width, height, phone_type):
        try:
            if not Telephone.check_phone_type(phone_type):
                raise MyError(f'У телефона "{brand} {name}" некоректно указан его тип')
            else:
                return cls( brand, name, mass, long, width, height, phone_type)
        except MyError as e:
            print(f'Ошибка валидации данных Телефон: {e}')


w = Warehouse('Офисная кладовка', 'Первый этаж, под лестницей', 10)

p = Printer.create('Canon', 'MF211d', 15, 0.5, 0.5, 0.5, 'laser')
print(p)

p.from_warehouse(w, 5)
p.to_warehouse(w, 10)
p.from_warehouse(w, 2)

m = Monitor.create('Philips', '243V', 1.5, 0.6, 0.01, 0.3, 23)
print(m)
m.to_warehouse(w, 4)

t = Telephone.create('Panasonic', 'KS-TSC35RUM', 1, 0.24, 0.15, 0.1, 'analog')
print(t)
t.to_warehouse(w, 5)

print(f'Текущее количество {p} на складе {w.name} составляет: {p.get_balance(w)} шт')
print(f'Текущее количество {m} на складе {w.name} составляет: {m.get_balance(w)} шт')
print(f'Текущее количество {t} на складе {w.name} составляет: {t.get_balance(w)} шт')

w.store_report()


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, rez, imz):
        self.rez = rez
        self.imz = imz

    def __str__(self):
        if self.rez == 0:
            re = ''
        else:
            re = str(self.rez)

        if self.imz == 0:
            im = ''
        elif self.imz > 0:
            if self.rez != 0:
                im = f' + {self.imz}i'
            else:
                im = f'{self.imz}i'
        else:
            if self.rez != 0:
                im = f' - {abs(self.imz)}i'
            else:
                im = f'-{abs(self.imz)}i'

        return f'{re}{im}'

    def __add__(self, other):
        return Complex(self.rez + other.rez, self.imz + other.imz)

    def __mul__(self, other):
        return Complex(self.rez * other.rez - self.imz * other.imz, self.rez * other.imz + other.rez * self.imz)

c1 = Complex(5, -4)
print(c1)
c2 = Complex(-6, 4)
print(c2)
print(c1 + c2)
print(c1 * c2)


