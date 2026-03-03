from typing import Optional


class ConstructionObject:
    """
    Базовый класс, представляющий строительный объект.

    Attributes:
        name (str): Название объекта.
        location (str): Местоположение объекта.
        total_area (float): Общая площадь объекта в м².
        _floors (int): Количество этажей (инкапсулированный атрибут).
    """

    def __init__(self, name: str, location: str, total_area: float, floors: int) -> None:
        """
        Инициализация строительного объекта.

        Args:
            name (str): Название объекта.
            location (str): Адрес или район строительства.
            total_area (float): Общая площадь в м².
            floors (int): Количество этажей.
        """
        self.name: str = name
        self.location: str = location
        self.total_area: float = total_area
        self._floors: int = floors  # Инкапсуляция для защиты от некорректного изменения

    def __str__(self) -> str:
        """Возвращает удобочитаемое представление объекта."""
        return (f"{self.name}, расположение: {self.location}, "
                f"площадь: {self.total_area} м², этажей: {self._floors}")

    def __repr__(self) -> str:
        """Возвращает официальное представление объекта."""
        return (f"ConstructionObject(name='{self.name}', "
                f"location='{self.location}', "
                f"total_area={self.total_area}, floors={self._floors})")

    def calculate_density(self) -> float:
        """
        Рассчитывает среднюю площадь на один этаж.

        Returns:
            float: Площадь одного этажа в м².
        """
        if self._floors == 0:
            raise ValueError("Количество этажей не может быть равно 0.")
        return self.total_area / self._floors

    def add_floor(self) -> None:
        """
        Увеличивает количество этажей на один.
        """
        self._floors += 1


class ResidentialBuilding(ConstructionObject):
    """
    Дочерний класс, представляющий жилое здание.

    Дополнительно содержит информацию о количестве квартир.
    """

    def __init__(
        self,
        name: str,
        location: str,
        total_area: float,
        floors: int,
        apartments: int
    ) -> None:
        """
        Расширенный конструктор жилого здания.

        Args:
            apartments (int): Количество квартир в здании.
        """
        super().__init__(name, location, total_area, floors)
        self.apartments: int = apartments

    def calculate_density(self) -> float:
        """
        Перегруженный метод расчёта плотности.

        Причина перегрузки:
        Для жилого здания более логично рассчитывать
        среднюю площадь на одну квартиру, а не на этаж.

        Returns:
            float: Средняя площадь одной квартиры в м².
        """
        if self.apartments == 0:
            raise ValueError("Количество квартир не может быть равно 0.")
        return self.total_area / self.apartments

    def calculate_occupancy(self, avg_people_per_apartment: float) -> float:
        """
        Рассчитывает примерное количество жильцов.

        Args:
            avg_people_per_apartment (float): Среднее количество человек в квартире.

        Returns:
            float: Оценочное количество жильцов.
        """
        return self.apartments * avg_people_per_apartment


if __name__ == "__main__":
    # Пример использования

    object1 = ConstructionObject(
        name="Бизнес-центр 'Север'",
        location="Санкт-Петербург",
        total_area=12000.0,
        floors=10
    )

    print(object1)
    print("Средняя площадь этажа:", object1.calculate_density())

    house = ResidentialBuilding(
        name="ЖК 'Парковый'",
        location="Санкт-Петербург",
        total_area=15000.0,
        floors=16,
        apartments=240
    )

    print(house)
    print("Средняя площадь квартиры:", house.calculate_density())
    print("Примерное количество жильцов:", house.calculate_occupancy(2.5))