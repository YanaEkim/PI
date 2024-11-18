class Car:
    def __init__(self):
        self.speed = 0
        self.is_running = False

    def Start(self):
        if not self.is_running:
            self.is_running = True
            print("Car started.")
        else:
            print("Car is already running.")

    def Stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print("Car stopped.")
        else:
            print("Car is already stopped.")

    def Accelerate(self, speed):
        if self.is_running:
            self.speed += speed
            print(f"Car accelerated to {self.speed} km/h.")
        else:
            print("Car is not running. Please start the car first.")
            
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class StartCarCommand(Command):
    def __init__(self, car):
        self.car = car

    def execute(self):
        self.car.Start()

    def undo(self):
        self.car.Stop()

class StopCarCommand(Command):
    def __init__(self, car):
        self.car = car

    def execute(self):
        self.car.Stop()

    def undo(self):
        self.car.Start()

class AccelerateCommand(Command):
    def __init__(self, car, speed):
        self.car = car
        self.speed = speed

    def execute(self):
        self.car.Accelerate(self.speed)

    def undo(self):
        self.car.Accelerate(-self.speed)
        
class RemoteControl:
    def __init__(self):
        self.commands = {}
        self.undo_command = None

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if slot in self.commands:
            self.commands[slot].execute()
            self.undo_command = self.commands[slot]

    def press_undo(self):
        if self.undo_command:
            self.undo_command.undo()
            
# Создаем автомобиль
car = Car()

# Создаем команды
start_command = StartCarCommand(car)
stop_command = StopCarCommand(car)
accelerate_command = AccelerateCommand(car, 10)

# Создаем пульт управления
remote = RemoteControl()

# Настраиваем пульт
remote.set_command("start", start_command)
remote.set_command("stop", stop_command)
remote.set_command("accelerate", accelerate_command)

# Используем пульт
remote.press_button("start")
remote.press_button("accelerate")
remote.press_button("accelerate")
remote.press_button("stop")

# Отмена последней команды
remote.press_undo()