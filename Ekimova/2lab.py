from abc import ABC, abstractmethod

class Furniture(ABC):
    @abstractmethod
    def __str__(self):
        pass
class Chair(Furniture):
    def __init__(self, material, color, height):
        self.material = material
        self.color = color
        self.height = height

    def __str__(self):
        return f"Стул из {self.material} цвета {self.color} высотой {self.height} см."
class Table(Furniture):
    def __init__(self, material, color, diameter):
        self.material = material
        self.color = color
        self.diameter = diameter

    def __str__(self):
        return f"Стол из {self.material} цвета {self.color} диаметром {self.diameter} см."
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self, material, color, height):
        pass

    @abstractmethod
    def create_table(self, material, color, diameter):
        pass
class WoodenFurnitureFactory(FurnitureFactory):
    def create_chair(self, material, color, height):
        return Chair(material, color, height)

    def create_table(self, material, color, diameter):
        return Table(material, color, diameter)
class MetalFurnitureFactory(FurnitureFactory):
    def create_chair(self, material, color, height):
        return Chair(material, color, height)

    def create_table(self, material, color, diameter):
        return Table(material, color, diameter)
if __name__ == "__main__":
    # Создаем деревянную мебель
    wooden_factory = WoodenFurnitureFactory()
    wooden_chair = wooden_factory.create_chair("древесина", "коричневый", 90)
    wooden_table = wooden_factory.create_table("древесина", "светлый", 120)

    print(wooden_chair)  # Вывод информации о деревянном стуле
    print(wooden_table)  # Вывод информации о деревянном столе

    # Создаем металлическую мебель
    metal_factory = MetalFurnitureFactory()
    metal_chair = metal_factory.create_chair("металл", "черный", 100)
    metal_table = metal_factory.create_table("металл", "серебристый", 150)

    print(metal_chair)  # Вывод информации о металлическом стуле
    print(metal_table)  # Вывод информации о металлическом столе