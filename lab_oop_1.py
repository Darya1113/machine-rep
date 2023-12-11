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
        Создание и подготовка к работе объекта "Стакан"

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



class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 10)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занятый объем должен быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Занятый объем стакана должен быть положительным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 10)
        >>> glass.is_empty_glass()
        """

        def add_water_to_glass(self, water: float) -> None:
            """
            Добавление воды в стакан.
            :param water: Объем добавляемой жидкости

            :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

            Примеры:
            >>> glass = Glass(500, 0)
            >>> glass.add_water_to_glass(200)
            """
            if not isinstance(water, (int, float)):
                raise TypeError("Добавляемая жидкость должна быть типа int или float")
            if water < 0:
                raise ValueError("Добавляемая жидкость должна положительным числом")
            ...

        def remove_water_from_glass(self, estimate_water: float) -> None:
            """
            Извлечение воды из стакана.

            :param estimate_water: Объем извлекаемой жидкости
            :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
            то возвращается ошибка.

            :return: Объем реально извлеченной жидкости

            Примеры:
            >>> glass = Glass(500, 500)
            >>> glass.remove_water_from_glass(200)
            """
            ...
            # TODO инициализировать объект "Стакан"



if __name__ == "__main__":
    doctest.testmod()
    ...  # TODO инициализировать два объекта типа Glass
    glass1 = Glass(300, 0)
    glass2 = Glass(200, 100)
    # TODO попробовать инициализировать не корректные объекты
    glass3 = Glass(-50, 0)
    glass4 = Glass(100, -1)

    player1 = Player(300, 0, 0)
    player2 = Player(0, 10, -25.5)
    #player3 = Player(-10, 1, 0)
    #player4 = Player(3.2, 0, 0)

    car1 = Car(78.2, 'BMW')
    car2 = Car(22.3, 'Ford')
    #car3 = Car(0, 3)
    #car4 = Car('22', 'Kia')