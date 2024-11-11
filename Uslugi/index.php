<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Услуга: Аренда</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .services-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .service-card {
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            width: 300px;
            margin: 15px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            text-align: center;
            transition: transform 0.2s;
        }
        .service-card:hover {
            transform: scale(1.05);
        }
        .service-card img {
            width: 100%;
            height: auto;
        }
        .service-card h2 {
            color: #007BFF;
            margin: 10px 0;
        }
        .service-card p {
            padding: 0 15px 15px;
        }
        .service-card a {
            display: inline-block;
            margin: 10px 0;
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .service-card a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<h1>Услуга: Аренда</h1>

<div class="services-container">

    <div class="service-card">
        <img src="https://via.placeholder.com/300x200.png?text=Аренда+Оборудования" alt="Аренда Оборудования">
        <h2>Аренда Оборудования</h2>
        <p>Мы предлагаем аренду различного оборудования для строительных и ремонтных работ. Гарантируем высокое качество и надежность.</p>
        <a href="arenda-oborudovaniya.html">Подробнее</a>
    </div>

    <div class="service-card">
        <img src="https://via.placeholder.com/300x200.png?text=Аренда+Техники" alt="Аренда Техники">
        <h2>Аренда Техники</h2>
        <p>Аренда специализированной техники для выполнения различных задач. Быстрая обработка заявок и гибкие условия аренды.</p>
        <a href="arenda-tehniki.html">Подробнее</a>
    </div>

    <div class="service-card">
        <img src="https://via.placeholder.com/300x200.png?text=Аренда+Автомобилей" alt="Аренда Автомобилей">
        <h2>Аренда Автомобилей</h2>
        <p>Предлагаем аренду автомобилей для личного и коммерческого использования. Удобные условия и широкий выбор моделей.</p>
        <a href="arenda-avtomobiley.html">Подробнее</a>
    </div>

</div>

</body>
</html>