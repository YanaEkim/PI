class GameObject:
    def __init__(self, name):
        self.name = name

    def describe(self):
        raise NotImplementedError("Метод 'describe' должен быть реализован в подклассах.")
    
class Player(GameObject):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health

    def describe(self):
        return f"Игрок {self.name} с {self.health} HP."


class Enemy(GameObject):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def describe(self):
        return f"Враг {self.name} наносит {self.damage} урона."


class NPC(GameObject):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def describe(self):
        return f"NPC {self.name} выполняет роль: {self.role}."
    
class GameObjectFactory:
    @staticmethod
    def create_game_object(object_type, *args, **kwargs):
        if object_type == 'player':
            return Player(*args, **kwargs)
        elif object_type == 'enemy':
            return Enemy(*args, **kwargs)
        elif object_type == 'npc':
            return NPC(*args, **kwargs)
        else:
            raise ValueError(f"Неизвестный тип объекта: {object_type}")
    
if __name__ == "__main__":
    player = GameObjectFactory.create_game_object('player', 'Hero', 100)
    enemy = GameObjectFactory.create_game_object('enemy', 'Goblin', 15)
    npc = GameObjectFactory.create_game_object('npc', 'Merchant', 'торговля')

    print(player.describe())
    print(enemy.describe())
    print(npc.describe())