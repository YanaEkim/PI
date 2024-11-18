from abc import ABC, abstractmethod

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass

class MeleeAttack(AttackStrategy):
    def attack(self):
        return "Атака ближним боем!"

class RangedAttack(AttackStrategy):
    def attack(self):
        return "Атака дальним боем!"

class MagicAttack(AttackStrategy):
    def attack(self):
        return "Магическая атака!"

class Character:
    def __init__(self, name, attack_strategy: AttackStrategy):
        self.name = name
        self.attack_strategy = attack_strategy

    def set_attack_strategy(self, attack_strategy: AttackStrategy):
        self.attack_strategy = attack_strategy

    def attack(self):
        print(f"{self.name} атакует: {self.attack_strategy.attack()}")

# Создаем стратегии атаки
melee_attack = MeleeAttack()
ranged_attack = RangedAttack()
magic_attack = MagicAttack()

# Создаем персонажей с разными стратегиями атаки
warrior = Character("Воин", melee_attack)
archer = Character("Лучник", ranged_attack)
wizard = Character("Маг", magic_attack)

# Персонажи атакуют
warrior.attack()  # Воин атакует: Атака ближним боем!
archer.attack()   # Лучник атакует: Атака дальним боем!
wizard.attack()   # Маг атакует: Магическая атака!

# Изменяем стратегию атаки у Воина
warrior.set_attack_strategy(magic_attack)
warrior.attack()  # Воин атакует: Магическая атака!