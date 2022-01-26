# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep

class TrafficLight:
    __color = (("red", 7), ("yellow", 2), ("green", 3))

    def running(self):
        print(f'Горит {self.__color[0][0]}')
        sleep(self.__color[0][1])

        print(f'Горит {self.__color[1][0]}')
        sleep(self.__color[1][1])

        print(f'Горит {self.__color[2][0]}')
        sleep(self.__color[2][1])

s = TrafficLight()

for i in range(3):
    s.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asfalt_massa(self, mass_of_layer, layer_count):
        return self._width * self._length * mass_of_layer * layer_count

r = Road(20, 5000)
print(f'Масса асфальта составит {r.calculate_asfalt_massa(25, 5) / 1000} т')

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

# создаём экземпляр класса
w1 = Position('Василий', 'Бардюров', 'Менеджер', {"wage": 20000, "bonus": 5000})

# проверяем значения атрибутов
print(f'Значение атрибута name = "{w1.name}", Значение атрибута surname = "{w1.surname}", Значение атрибута position = "{w1.position}", Значение атрибута income = "{w1._income}"')

# вызываем методы экземпляра
name, surname = w1.get_full_name()
print(surname, name)
print(w1.get_total_income())

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    __turn_direction = ('left', 'right')

    def __init__(self, color, name):
        self.__speed = 0
        self.color = color
        self.name = name
        self.__is_police = False

    def go(self, go_speed):
        if go_speed > 0:
            self.__speed = go_speed
            print(f'Машина поехала со скоростью {go_speed} км/час')
        else:
            print('Для полной остановки машины предусмотрен метод stop')

    def stop(self):
        self.__speed = 0
        print('Машина полностью остановилась')

    def turn(self, direction):
        if direction in self.__turn_direction:
            print(f'Машина повернула {direction}')

    def get_speed(self):
        return self.__speed

    def get_is_police(self):
        return self.__is_police

    def __set_is_police(self, is_police):
        self.__is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость = {self.__speed}')


class TownCar(Car):
    __max_speed = 60

    def show_speed(self):
        super(TownCar, self).show_speed()

        if self.get_speed() > self.__max_speed:
            print(f'Внимание! Максимально допустимая скорость движения на машине данного типа превышена на {self.get_speed() - self.__max_speed} км/час')


class SportCar(Car):
    def __init__(self, color, name, power):
        super().__init__(color, name)
        self.power = power


class WorkCar(Car):
    __max_speed = 40

    def show_speed(self):
        super(WorkCar, self).show_speed()

        if self.get_speed() > self.__max_speed:
            print(f'Внимание! Максимально допустимая скорость движения на машине данного типа превышена на {self.get_speed() - self.__max_speed}')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self._Car__set_is_police(True)

pc = PoliceCar('Синий', 'Уазик')
pc.show_speed()
pc.go(120)
pc.turn('right')
pc.stop()
print('Это полицейская машина' if pc.get_is_police() else 'Это не полицейская машина')

tc = TownCar('Красный', 'Москвич')
tc.show_speed()
tc.go(100)
tc.show_speed()
tc.turn('left')
tc.go(60)
tc.stop()
print('Это полицейская машина' if tc.get_is_police() else 'Это не полицейская машина')

pc2 = PoliceCar('Черный', 'Уазик')
print('Это полицейская машина' if pc2.get_is_police() else 'Это не полицейская машина')

wc = WorkCar('Грязный', 'Камаз')
print('Это полицейская машина' if wc.get_is_police() else 'Это не полицейская машина')

sc = SportCar('Синий', 'Bugatti Weiron', 500)
sc.go(250)
print('Это полицейская машина' if sc.get_is_police() else 'Это не полицейская машина')

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')

pen = Pen('Parker')
pen.draw()

percil = Pencil('Koh-i-nor')
percil.draw()

handle = Handle('Whiteboard')
handle.draw()


