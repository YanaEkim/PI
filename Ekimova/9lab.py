from abc import ABC, abstractmethod

class CookingTemplate(ABC):
    def prepare_ingredients(self):
        print("Подготовка ингредиентов...")

    @abstractmethod
    def cook(self):
        pass

    def serve(self):
        print("Подача блюда...")

    def cook_dish(self):
        self.prepare_ingredients()
        self.cook()
        self.serve()

class Borscht(CookingTemplate):
    def cook(self):
        self.boil_meat()
        self.prepare_vegetables()
        self.prepare_zazharka()
        self.add_zazharka_to_broth()
        self.season_and_rest()

    def boil_meat(self):
        print("Заливаем холодной водой и доводим до кипения мясо.")
        print("Снимаем пену и бульон варим на медленном огне до готовности мяса.")

    def prepare_vegetables(self):
        print("Подготавливаем овощи:")
        print("- Свёкла очищается, натирается на тёрке и тушится с добавлением уксуса и томатной пасты.")
        print("- Нарезаем картофель, капусту, морковь и лук.")

    def prepare_zazharka(self):
        print("Готовим зажарку:")
        print("- Обжариваем лук и морковь на сковороде.")
        print("- Добавляем тушёную свёклу.")

    def add_zazharka_to_broth(self):
        print("Когда мясо готово, его вынимаем из бульона, нарезаем и возвращаем обратно.")
        print("Добавляем картофель и капусту.")
        print("Добавляем зажарку в бульон и варим до готовности всех ингредиентов.")

    def season_and_rest(self):
        print("Солим, перчим и добавляем лавровый лист и другие специи по вкусу.")
        print("Настаиваем борщ под крышкой 5-10 минут, чтобы все вкусы смешались.")

# Приготовление борща
borscht = Borscht()
borscht.cook_dish()