import copy

class Configuration:
    def __init__(self, settings=None):
        if settings is None:
            settings = {}
        self.settings = settings

    def clone(self):
        return copy.deepcopy(self)

    def update_setting(self, key, value):
        self.settings[key] = value

    def __str__(self):
        return str(self.settings)

# Создаем базовую конфигурацию
base_config = Configuration({
    "debug": False,
    "log_level": "INFO",
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "password"
    }
})

# Клонируем базовую конфигурацию
dev_config = base_config.clone()

# Изменяем настройки для dev конфигурации
dev_config.update_setting("debug", True)
dev_config.update_setting("log_level", "DEBUG")
dev_config.update_setting("database", {
    "host": "dev.db.example.com",
    "port": 5432,
    "user": "dev_user",
    "password": "dev_password"
})

# Клонируем dev конфигурацию
test_config = dev_config.clone()

# Изменяем настройки для test конфигурации
test_config.update_setting("database", {
    "host": "test.db.example.com",
    "port": 5432,
    "user": "test_user",
    "password": "test_password"
})

# Выводим конфигурации
print("Базовая конфигурация:", base_config)
print("Dev конфигурация:", dev_config)
print("Test конфигурация:", test_config)