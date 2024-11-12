using System;

// Интерфейс стратегии
public interface IRouteStrategy
{
    string CalculateRoute(string start, string end);
}

// Конкретные стратегии
public class FastestRouteStrategy : IRouteStrategy
{
    public string CalculateRoute(string start, string end)
    {
        // Логика расчета самого быстрого маршрута
        return $"Самый быстрый маршрут от {start} до {end}";
    }
}

public class ShortestRouteStrategy : IRouteStrategy
{
    public string CalculateRoute(string start, string end)
    {
        // Логика расчета самого короткого маршрута
        return $"Самый короткий маршрут от {start} до {end}";
    }
}

public class MinTrafficRouteStrategy : IRouteStrategy
{
    public string CalculateRoute(string start, string end)
    {
        // Логика расчета маршрута с минимальным количеством пробок
        return $"Маршрут с минимальным количеством пробок от {start} до {end}";
    }
}

// Контекст для выбора стратегии
public class RouteNavigator
{
    private IRouteStrategy _strategy;

    public RouteNavigator(IRouteStrategy strategy)
    {
        _strategy = strategy;
    }

    public void SetStrategy(IRouteStrategy strategy)
    {
        _strategy = strategy;
    }

    public string GetRoute(string start, string end)
    {
        return _strategy.CalculateRoute(start, end);
    }
}

// Использование системы маршрутизации
class Program
{
    static void Main(string[] args)
    {
        // Создаем навигатор с начальной стратегией (например, самый быстрый маршрут)
        RouteNavigator navigator = new RouteNavigator(new FastestRouteStrategy());

        // Получаем маршрут с использованием текущей стратегии
        string route = navigator.GetRoute("Москва", "Санкт-Петербург");
        Console.WriteLine(route);

        // Меняем стратегию на самый короткий маршрут
        navigator.SetStrategy(new ShortestRouteStrategy());
        route = navigator.GetRoute("Москва", "Санкт-Петербург");
        Console.WriteLine(route);

        // Меняем стратегию на маршрут с минимальным количеством пробок
        navigator.SetStrategy(new MinTrafficRouteStrategy());
        route = navigator.GetRoute("Москва", "Санкт-Петербург");
        Console.WriteLine(route);
    }
}