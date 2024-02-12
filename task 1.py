class Car:
    """
    Базовый класс "Автомобиль"
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор для класса Car.

        :param make (str): Марка машины.
        :param model (str): Модель машины.
        :param year (int): Год выпуска автомобиля.
        """
        if not isinstance(make, str):
            raise TypeError("Марка машины должна быть типа string")
        self._make = make  # защищенный атрибут
        if not isinstance(model, str):
            raise TypeError("Модель машины должна быть типа string")
        self._model = model  # защищенный атрибут
        if not isinstance(year, int):
            raise TypeError("Год выпуска машины должен быть типа int")
        if year < 1000:
            raise ValueError("Год выпуска машины должен быть больше 1000")
        self._year = year  # защищенный атрибут

    """Защищенные атрибуты нужны потому что марку, модель и год выпуска автомобиля нельзя изменить после того, как он уже был выпущен"""
    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self._year} {self._make} {self._model}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Car('{self._make}', '{self._model}', {self._year})"


class PassengerCar(Car):
    """
    Дочерний класс, представляющий легковой автомобиль.
    """

    def __init__(self, make: str, model: str, year: int, num_passengers: int):
        """
        Конструктор для класса PassengerCar.

        :param make (str): Марка машины.
        :param model (str): Модель машины.
        :param year (int): Год выпуска машины.
        :param num_passengers (int): Количество пассажиров, которое может вместить автомобиль.
        """
        super().__init__(make, model, year)
        self._num_passengers = num_passengers  # защищенный атрибут

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Passenger Car: {self._year} {self._make} {self._model} - {self._num_passengers} passengers"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"PassengerCar('{self._make}', '{self._model}', {self._year}, {self._num_passengers})"

    def start(self) -> str:
        """
        Заводит легковой автомобиль.
        Returns:
        Появится сообщение о том, что автомобиль запущен.
        """
        return "Легковой автомобиль заведен"

    def is_open_trunk(self) -> bool:
        """
        Показывает, открыт ли багажник у автомобиля.

        Returns:
        True - открыт, False - закрыт
        """
        return False
