using System;

// Интерфейс команды
public interface ICommand
{
    void Execute();
}

// Класс, представляющий телевизор
public class Television
{
    public int Volume { get; private set; }
	public int Light { get; private set; }

	public void SetVolume(int volume)
    {
        Volume = volume;
        Console.WriteLine($"Громкость установлена на {Volume}");
    }
	public void SetLight(int light)
	{
		Light = light;
		Console.WriteLine($"Яркость установлена на {Light}");
	}

}

// Команда для установки яркости телевизора
public class SetLightCommand : ICommand
{
	private readonly Television _television;
	private readonly int _light;

	public SetLightCommand(Television television, int light)
	{
		_television = television;
		_light = light;
	}

	public void Execute()
	{
		_television.SetLight(_light);
	}
}

// Команда для установки громкости
public class SetVolumeCommand : ICommand
{
    private readonly Television _television;
    private readonly int _volume;

    public SetVolumeCommand(Television television, int volume)
    {
        _television = television;
        _volume = volume;
    }

    public void Execute()
    {
        _television.SetVolume(_volume);
    }
}

// Класс удаленного управления для выполнения команд
public class RemoteControl
{
    private ICommand _command;

    public void SetCommand(ICommand command)
    {
        _command = command;
    }

    public void PressButton()
    {
        _command.Execute();
    }
}

// Пример использования
public class Program
{
    public static void Main(string[] args)
    {
        // Создаем объект телевизора
        var television = new Television();
		var remoteControl = new RemoteControl();

		// Запрашиваем у пользователя уровень громкости
		Console.Write("Введите уровень громкости (0-100): ");
        if (int.TryParse(Console.ReadLine(), out int volume) && volume >= 0 && volume <= 100)
        {
            // Создаем команду для изменения громкости
            var setVolumeCommand = new SetVolumeCommand(television, volume);

            // Создаем пульт и назначаем команду
            
            remoteControl.SetCommand(setVolumeCommand);

            // Выполняем команду
            remoteControl.PressButton(); // Громкость устанавливается на введенное значение
        }
        else
        {
            Console.WriteLine("Некорректный ввод. Пожалуйста, введите число от 0 до 100.");
        }
		// Запрашиваем у пользователя уровень Яркости
		Console.Write("Введите уровень яркости (0-100): ");
		if (int.TryParse(Console.ReadLine(), out int light) && light >= 0 && light <= 100)
		{
			// Создаем команду для изменения громкости
			var setLightCommand = new SetLightCommand(television, light);

			// Создаем пульт и назначаем команду
			remoteControl.SetCommand(setLightCommand);

			// Выполняем команду
			remoteControl.PressButton(); // Громкость устанавливается на введенное значение
		}
		else
		{
			Console.WriteLine("Некорректный ввод. Пожалуйста, введите число от 0 до 100.");
		}
        Console.ReadLine();
    }
}