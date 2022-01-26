# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

li11 = [[10]]
li12 = [[1, 2]]
li21 = [[1], [2]]
li32 = [[31, 32], [37, 43], [51, 86]]
li33 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
li24 = [[3, 5, 8, 3], [8, 3, 7, 1]]

li_err = [[1, 2, 3], [4, 5]]


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def dimension(self):
        check = []

        for i in range(0, len(self.matrix_list)):
            check.append(len(self.matrix_list[i]))

        for i in range(1, len(check)):
            if check[i] != check[i -1]:
                return None, None

        return len(self.matrix_list), check[0]

    def __str__(self):
        a, b = self.dimension()

        if a is not None and b is not None:
            m_string =  f'Матрица размерностью {a} строк * {b} столбцов\n'

            for i in range(0, a):
                for j in range(0, b):
                    m_string += str(self.matrix_list[i][j]) + (' ' if j != len(self.matrix_list[i]) - 1 else '')
                m_string += '\n' if i != len(self.matrix_list) - 1 else ''
        else:
            m_string = 'Некорректные данные'

        return m_string

    def __add__(self, other):
        i, j = self.dimension()

        if i == other.dimension()[0] and j == other.dimension()[1]:
            for k in range(0, i):
                for f in range(0, j):
                    self.matrix_list[k][f] += other.matrix_list[k][f]

            return self
        else:
            raise ValueError('Действие невозможно так как операнды обладают разной размерностью')

k = Matrix(li_err)
m = Matrix(li24)
n = Matrix(li32)
p = Matrix(li24)

print(k)
print(m)
print(n)

try:
    print(m + n)
except ValueError as e:
    print(e.args[0])

try:
    print(m + p)
except ValueError as e:
    print(e.args[0])

# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self.consumption = size

    def __str__(self):
        return f'Пальто "{self.name}", размер {self.size}, расход материала {self.consumption}'

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, size):
        self.__consumption = round(size / 6.5 + 0.5, 2)


class Suit(Cloth):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        self.consumption = height

    def __str__(self):
        return f'Костюм "{self.name}", рост {self.height}, расход материала {self.consumption}'

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, height):
        self.__consumption = round(2 * self.height + 0.3, 2)

c = Coat('Ивановский трикотаж', 50)
print(c)

s = Suit('Armany', 1.2)
print(s)

# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.

class Cell:
    def __init__(self, size):
        if size > 0:
            self.size = size
        else:
            raise TypeError('Объект с размерами <= 0 не может существовать')

    def __str__(self):
        return f'Клетка с количеством ячеек {self.size}'

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        return Cell(self.size - other.size)      # Проверка не нужна т.к она реализована в конструкторе

    def __mul__(self, other):
         return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def make_order(self, value):
        r = ''
        for i in range(self.size // value):
            r += '*' * value + ('\n' if i < self.size // value - 1 else '\n' if self.size % value > 0 else '')

        r += '*' * (self.size % value)

        return r

ameba = Cell(10)
infuzoria = Cell(3)

print(ameba.make_order(5))
print(infuzoria.make_order(4))

try:
    err = Cell(0)
except Exception as e:
    print(f'Создание клетки невозможно: {e.args[0]}')

с_add = ameba + infuzoria
print(с_add)
print(с_add.make_order(4))

try:
    c_sub = infuzoria - ameba
except Exception as e:
    print(f'Вычитание из клетки невозможно: {e.args[0]}')

try:
    c_sub = ameba - infuzoria
    print(c_sub)
except Exception as e:
    print(f'Вычитание из клетки невозможно: {e.args[0]}')

print(c_sub.make_order(7))

c_mul = ameba * infuzoria
print(c_mul)
print(c_mul.make_order(10))

try:
  c_div = infuzoria / ameba
except Exception as e:
    print(f'Деление клетки невозможно: {e.args[0]}')

try:
    c_div = ameba / infuzoria
except Exception as e:
    print(f'Деление клетки невозможно: {e.args[0]}')

print(c_div)
print(c_div.make_order(1))





