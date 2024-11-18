import time
from datetime import datetime

class Singleton:
    _instance = None
    _log = []

    def _new_(cls):
        if cls._instance is None:
            cls.instance = super(Singleton, cls).new_(cls)
        return cls._instance

    def get_current_time(self):
        # Получаем текущее время
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Добавляем время в лог
        self._log.append(current_time)
        return current_time

    def get_log(self):
        # Возвращаем лог времени
        return self._log


# Пример использования
singleton1 = Singleton()
print("Первое время:", singleton1.get_current_time())

time.sleep(1)  # Задержка для демонстрации разницы времени

singleton2 = Singleton()
print("Второе время:", singleton2.get_current_time())

# Проверка того, что оба объекта ссылаются на один и тот же экземпляр
print("Один и тот же объект:", singleton1 is singleton2)

# Лог времени
print("Лог времени:", singleton1.get_log())