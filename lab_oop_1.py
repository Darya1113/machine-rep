from typing import Union
import doctest

class Car:
    def __init__(self, speed: float, brand: str):
        """
        Создание и подготовка к работе объекта "Машина"

        :param speed: Скорость
        :param brand: Марка

        Примеры:
        >>> car = Car(199.7, 'BMW')
        """
        if not isinstance(speed, float):
            raise TypeError("ОСкорость машины должна быть типа float")
        if speed < 0:
            raise ValueError("Скорость машины должна быть неотрицательным числом")
        self.speed = speed
        if not isinstance(brand, str):
            raise TypeError("Марка машины должна быть типа string")
        self.brand = brand

    def is_stop(self) -> bool:
        """
        Функция, которая проверяет стоит ли машина на месте

        :return: стоит ли машина на месте

        Примеры:
        >>> car = Car(130.2, 'Ford')
        >>> car.is_stop()
        """

    def change_speed(self, dv: float) -> float:
        """
        Функция, которая меняет скорость машины

        :param dv: На сколько изменяется скорость

        Примеры:
        >>> car = Car(50.0, 'Opel')
        >>> car.change_speed(12.1)
        """
        if not isinstance(dv, float):
            raise TypeError("Изменение скорости должно быть типа float")
        self.speed += dv


class Player:
    def __init__(self, score: int, x: Union[int, float], y: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Игрок"

        :param score: Счёт в игре
        :param x: Координата по x
        :param y: Координата по y

        Примеры:
        >>> player = Player(500, 0, 0) #инициализация экземпляра класса
        """
        if not isinstance(score, int):
            raise TypeError("Счет в игре должен быть типом int")
        if score < 0:
            raise TypeError("Счет в игре должен быть неотрицательным числом")
        self.score = score
        if not isinstance(x, (int, float)):
            raise TypeError("Координата x долженая быть типа int или float")
        self.x = x
        if not isinstance(y, (int, float)):
            raise TypeError("Координата y долженая быть типа int или float")
        self.y = y
    def add_score(self, points: int) -> int:
        """
        Функция, которая добавляет очки к текущему счету в игре

        :return: текущее количество очков

        Примеры:
        >>> player = Player(0, 0, 0)
        >>> player.add_score(100)
        """
        if not isinstance(points, int):
            raise TypeError("Добавленные очки должны быть типа int")

        self.score += points
    def move_player(self, dx: float, dy: float):
        """
        Функция, которая меняет координаты x и y у игрока

        :return: Новые координаты x и y

        Примеры:
        >>> player = Player(100, 0, 0)
        >>> player.move_player(30, -15)
        """

        self.x += dx
        self.y += dy

class Student:
    def __init__(self, year: int, university: str, number_debts: int):
        """
        Создание и подготовка к работе объекта "Студент"

        :param year: Год выпуска
        :param university: название университета
        :param number_subjects: кол-во долгов

        Примеры:
        >>> student = Student(2025, 'SPBPU', 2) #инициализация экземпляра класса
        """
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть типом int")
        if year < 1993:
            raise TypeError("Год выпуска должен быть >= 1993")
        self.year = year
        if not isinstance(university, str):
            raise TypeError("Название университета должно быть типа str")
        self.university = university
        if not isinstance(number_debts, int):
            raise TypeError("Кол-во долгов должно быть типом int")
        if number_debts < 0:
            raise TypeError("Кол-во долгов должно быть неотрицательно")
        self.number_debts = number_debts

    def add_year(self) -> int:
        """
        Функция, которая добавляет 1 к году выпуска (если например был взят академический отпуск)

        :return: текущий год выпуска

        Примеры:
        >>> student = Student(2025, 'MSU', 1)
        >>> student.add_year()
        """
        self.year += 1
    def is_study(self) -> bool:
        """
        Функция, которая выясняет учится ли сейчас студент

        :return: true или false

        Примеры:
        >>> student = Student(2025, 'MSU', 1)
        >>> student.is_study()
        """



if __name__ == "__main__":
    doctest.testmod()
    ...  # TODO инициализировать два объекта типа Glass
    student = Student(2026, 'MSU', 1)
    student = Student(2013, 'HSE', 0)
    # TODO попробовать инициализировать не корректные объекты
    #student = Student(12, 'SPBSTU', 2)
    #student = Student(2020, 'ITMO', -1)

    player1 = Player(300, 0, 0)
    player2 = Player(0, 10, -25.5)
    #player3 = Player(-10, 1, 0)
    #player4 = Player(3.2, 0, 0)

    car1 = Car(78.2, 'BMW')
    car2 = Car(22.3, 'Ford')
    #car3 = Car(0, 3)
    #car4 = Car('22', 'Kia')
