
class Building:
    """
    Абстрактный класс, описывающий здание.
    """

    def __init__(self, floors: int, area: float, year_built: int) -> None:
        """
        :param floors: Количество этажей (должно быть > 0)
        :param area: Общая площадь здания в м² (должна быть > 0)
        :param year_built: Год постройки здания
        """
        if floors <= 0:
            raise ValueError("Количество этажей должно быть больше нуля")
        if area <= 0:
            raise ValueError("Площадь должна быть больше нуля")
        if year_built <= 0:
            raise ValueError("Год постройки должен быть положительным")

        self.floors: int = floors
        self.area: float = area
        self.year_built: int = year_built

    def calculate_volume(self, floor_height: float) -> float:
        """
        Рассчитывает строительный объём здания.

        :param floor_height: Высота одного этажа в метрах (должна быть > 0)
        :return: Строительный объём здания в м³

        >>> house = Building(2, 120.0, 2015)
        >>> house.calculate_volume(3.0)
        720.0
        """
        if floor_height <= 0:
            raise ValueError("Высота этажа должна быть больше нуля")
        ...

    def renovate(self, added_area: float) -> None:
        """
        Выполняет реконструкцию здания с увеличением площади.

        :param added_area: Добавляемая площадь в м² (должна быть > 0)
        :return: None

        >>> building = Building(5, 1000.0, 1990)
        >>> building.renovate(200.0)
        """
        if added_area <= 0:
            raise ValueError("Добавляемая площадь должна быть положительной")
        ...


class ConstructionMaterial:
    """
    Абстрактный класс, описывающий строительный материал.
    """

    def __init__(self, name: str, density: float, strength: float) -> None:
        """
        :param name: Название материала
        :param density: Плотность материала (кг/м³, должна быть > 0)
        :param strength: Прочность материала (МПа, должна быть > 0)
        """
        if density <= 0:
            raise ValueError("Плотность должна быть больше нуля")
        if strength <= 0:
            raise ValueError("Прочность должна быть больше нуля")

        self.name: str = name
        self.density: float = density
        self.strength: float = strength

    def calculate_mass(self, volume: float) -> float:
        """
        Рассчитывает массу материала по объёму.

        :param volume: Объём материала в м³ (должен быть > 0)
        :return: Масса материала в килограммах

        >>> concrete = ConstructionMaterial("Concrete", 2400.0, 30.0)
        >>> concrete.calculate_mass(2.0)
        4800.0
        """
        if volume <= 0:
            raise ValueError("Объём должен быть положительным")
        ...

    def check_applicability(self, required_strength: float) -> bool:
        """
        Проверяет, подходит ли материал по прочности.

        :param required_strength: Требуемая прочность в МПа
        :return: True, если материал подходит, иначе False

        >>> steel = ConstructionMaterial("Steel", 7850.0, 250.0)
        >>> steel.check_applicability(200.0)
        True
        """
        if required_strength <= 0:
            raise ValueError("Требуемая прочность должна быть положительной")
        ...


class Foundation:
    """
    Абстрактный класс, описывающий фундамент здания.
    """

    def __init__(self, foundation_type: str, depth: float, bearing_capacity: float) -> None:
        """
        :param foundation_type: Тип фундамента (ленточный, свайный и т.д.)
        :param depth: Глубина заложения фундамента в метрах (должна быть > 0)
        :param bearing_capacity: Несущая способность (кПа, должна быть > 0)
        """
        if depth <= 0:
            raise ValueError("Глубина заложения должна быть больше нуля")
        if bearing_capacity <= 0:
            raise ValueError("Несущая способность должна быть больше нуля")

        self.foundation_type: str = foundation_type
        self.depth: float = depth
        self.bearing_capacity: float = bearing_capacity

    def calculate_settlement(self, load: float) -> float:
        """
        Оценивает осадку фундамента под нагрузкой.

        :param load: Нагрузка на фундамент в кПа (должна быть > 0)
        :return: Оценка осадки в миллиметрах

        >>> foundation = Foundation("Strip", 1.5, 250.0)
        >>> foundation.calculate_settlement(180.0)
        0.0
        """
        if load <= 0:
            raise ValueError("Нагрузка должна быть положительной")
        ...

    def is_suitable(self, building_load: float) -> bool:
        """
        Проверяет, подходит ли фундамент под нагрузку здания.

        :param building_load: Нагрузка от здания в кПа
        :return: True, если фундамент подходит, иначе False

        >>> foundation = Foundation("Pile", 6.0, 400.0)
        >>> foundation.is_suitable(350.0)
        True
        """
        if building_load <= 0:
            raise ValueError("Нагрузка здания должна быть положительной")
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()

