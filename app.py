import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Полный оригинальный код с рабочими кнопками Форума и Скачивания APK!
HTML_CODE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bishkek RP</title>
    <style>
        /* Обнуление стилей */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            background: #110022;
        }

        /* ЗАДНИЙ ФОН: Фиолетовый и жёлтый смешиваются и двигаются сверху вниз */
        .animated-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            background: linear-gradient(135deg, #2b004f 20%, #cca000 50%, #4a0082 80%);
            background-size: 200% 400%;
            animation: moveBackground 12s ease-in-out infinite;
        }

        @keyframes moveBackground {
            0% { background-position: 50% 0%; }
            50% { background-position: 50% 100%; }
            100% { background-position: 50% 0%; }
        }

        /* Контейнер сайта */
        .wrapper {
            width: 100%;
            max-width: 600px;
            padding: 25px 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        /* БОЛЬШОЙ ЖЁЛТЫЙ ГЛЯНЦЕВЫЙ ЗАГОЛОВОК */
        .logo {
            font-size: 3rem;
            font-weight: 900;
            color: #FFD700;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 
                0 0 10px rgba(255, 215, 0, 0.6),
                0 0 20px rgba(255, 215, 0, 0.4),
                2px 4px 0px #8B6508;
            background: linear-gradient(to bottom, #FFFFFF 0%, #FFD700 60%, #FF8C00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.5));
        }

        /* Навигация с кнопками (адаптивная сетка под 4 кнопки) */
        .nav-menu {
            display: flex;
            width: 100%;
            gap: 8px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        /* КНОПКИ С АНИМАЦИЕЙ НАЖАТИЯ */
        .nav-btn, .forum-link, .apk-btn {
            flex: 1;
            min-width: 120px;
            padding: 12px 5px;
            font-size: 0.9rem;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            background: #FFD700;
            color: #1a0033;
            cursor: pointer;
            box-shadow: 0 5px 0 #B8860B, 0 8px 15px rgba(0, 0, 0, 0.4);
            transition: all 0.1s ease;
            text-align: center;
            text-decoration: none;
        }

        /* Кнопка Форума (Бирюзовая) */
        .forum-link {
            background: #00FFCC;
            box-shadow: 0 5px 0 #00A383, 0 8px 15px rgba(0, 0, 0, 0.4);
        }

        /* Кнопка Скачать игру (Ярко-зелёная) */
        .apk-btn {
            background: #2ecc71;
            box-shadow: 0 5px 0 #27ae60, 0 8px 15px rgba(0, 0, 0, 0.4);
            color: #fff;
        }

        /* Эффект нажатия кнопок */
        .nav-btn:active, .forum-link:active, .apk-btn:active {
            transform: translateY(4px);
            box-shadow: 0 1px 0 #B8860B, 0 4px 6px rgba(0, 0, 0, 0.4);
            background: #FFC72C;
        }

        .forum-link:active {
            background: #00E6B8;
            box-shadow: 0 1px 0 #00A383;
        }

        .apk-btn:active {
            background: #27ae60;
            box-shadow: 0 1px 0 #1e7e34;
        }

        .nav-btn.active {
            background: #FF8C00;
            color: #fff;
            box-shadow: 0 5px 0 #CD5C5C, 0 8px 15px rgba(0, 0, 0, 0.4);
        }
        .nav-btn.active:active {
            box-shadow: 0 1px 0 #CD5C5C;
        }

        /* Контентная зона подложки */
        .content-box {
            background: rgba(20, 0, 40, 0.75);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 215, 0, 0.2);
            border-radius: 20px;
            padding: 25px;
            width: 100%;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            flex-grow: 1;
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.4s ease;
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h2 {
            color: #FFD700;
            margin-bottom: 15px;
            font-size: 1.5rem;
            border-bottom: 2px solid rgba(255, 215, 0, 0.3);
            padding-bottom: 5px;
        }

        p {
            font-size: 1.05rem;
            line-height: 1.6;
            color: #f0e6ff;
            margin-bottom: 15px;
        }

        /* Сетка для Доната */
        .donate-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 15px;
        }

        .donate-item {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 14px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 0 rgba(255, 215, 0, 0.2), 0 6px 10px rgba(0,0,0,0.2);
            transition: all 0.1s ease;
        }

        .donate-item:active {
            transform: translateY(3px);
            box-shadow: 0 1px 0 rgba(255, 215, 0, 0.2);
            background: rgba(255, 215, 0, 0.1);
        }

        .som-text {
            font-size: 1.2rem;
            font-weight: bold;
            color: #FFD700;
        }

        .bc-text {
            font-size: 0.95rem;
            color: #00FFCC;
            margin-top: 5px;
            font-weight: 600;
        }
    </style>
</head>
<body>

    <div class="animated-bg"></div>

    <div class="wrapper">
        <div class="logo">Bishkek RP</div>

        <div class="nav-menu">
            <button class="nav-btn active" onclick="openTab('main', this)">Главная</button>
            <button class="nav-btn" onclick="openTab('how-to', this)">Как играть?</button>
            <button class="nav-btn" onclick="openTab('donate', this)">Донат</button>
            <a href="https://bishkek-roleplay.sampproject.ru/index.php?whats-new/" target="_blank" class="forum-link">Форум</a>
            <button id="download-btn" class="apk-btn">Скачать игру</button>
        </div>

        <div class="content-box">
            
            <div id="main" class="tab-content active">
                <h2>Добро пожаловать, Игрок!</h2>
                <p>Мы искренне рады приветствовать тебя в мире <strong>Bishkek RP</strong>! Это место, где твои самые смелые игровые амбиции становятся реальностью.</p>
                <p>Bishkek RP — это продвинутый симулятор реальной жизни на твоем мобильном устройстве. Окунись в потрясающую атмосферу нашего города, общайся с тысячами игроков, создавай уникальные истории и весело проводи время в дружной компании!</p>
            </div>

            <div id="how-to" class="tab-content">
                <h2>Пошаговое руководство</h2>
                <p><strong>1. Начало пути:</strong> Ты появляешься на главном вокзале города Бишкек совершенно один. Твоя первостепенная цель — дойти до ближайшего МФЦ и получить свой первый паспорт.</p>
                <p><strong>2. Первые деньги:</strong> Без денег в городе не прожить. Направляйся к NPC "Прораб" на Шахту или Завод. Это простая работа, которая поможет тебе накопить на твой первый мобильный телефон и мопед.</p>
                <p><strong>3. Получение прав:</strong> Как только на руках будет 5,000 сом, отправляйся в Автошколу. Пройди теоретический тест на знание ПДД и сдай практический экзамен по вождению, чтобы получить водительские права категории "B".</p>
                <p><strong>4. Стремление к лучшему:</strong> Не останавливайся на достигнутом! Устраивайся на высокооплачиваемые работы (Дальнобойщик, Инкассатор), вступай во фракции (МВД, ГКНБ, Медики, ОПГ), покупай элитную недвижимость, крутые тачки и построй собственную бизнес-империю!</p>
            </div>

            <div id="donate" class="tab-content">
                <h2>Донат Меню</h2>
                <p>Здесь ты можешь приобрести внутреннюю валюту <strong>Bish Coins (BC)</strong> за реальные Сомы для быстрого старта.</p>
                
                <div class="donate-grid">
                    <div class="donate-item"><span class="som-text">100 сом</span><span class="bc-text">190 BC</span></div>
                    <div class="donate-item"><span class="som-text">250 сом</span><span class="bc-text">350 BC</span></div>
                    <div class="donate-item"><span class="som-text">340 сом</span><span class="bc-text">420 BC</span></div>
                    <div class="donate-item"><span class="som-text">450 сом</span><span class="bc-text">580 BC</span></div>
                    <div class="donate-item"><span class="som-text">620 сом</span><span class="bc-text">770 BC</span></div>
                    <div class="donate-item"><span class="som-text">750 сом</span><span class="bc-text">990 BC</span></div>
                    <div class="donate-item"><span class="som-text">1290 сом</span><span class="bc-text">1890 BC</span></div>
                    <div class="donate-item"><span class="som-text">1570 сом</span><span class="bc-text">2190 BC</span></div>
                    <div class="donate-item"><span class="som-text">1990 сом</span><span class="bc-text">2790 BC</span></div>
                    <div class="donate-item"><span class="som-text">2390 сом</span><span class="bc-text">3290 BC</span></div>
                </div>
            </div>

        </div>
    </div>

    <script>
        // Функция переключения вкладок
        function openTab(tabId, buttonElement) {
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(content => content.classList.remove('active'));
            
            const buttons = document.querySelectorAll('.nav-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            buttonElement.classList.add('active');
        }

        // Логика интерактивного скачивания APK
        document.getElementById('download-btn').addEventListener('click', function() {
            const btn = this;
            
            // 1. Меняем текст на "Загрузка..."
            btn.textContent = 'Загрузка...';
            btn.style.pointerEvents = 'none'; // Отключаем клики во время старта
            
            // Твоя проверенная ссылка на Google Диск
            const directLink = 'https://drive.google.com/file/d/1wEjTeMJg-49poG-sTZMyHNroF_YPy1AQ/view?usp=drivesdk';
            
            // 2. Инициируем переход
            const tempLink = document.createElement('a');
            tempLink.href = directLink;
            tempLink.target = '_blank';
            document.body.appendChild(tempLink);
            tempLink.click();
            document.body.removeChild(tempLink);
            
            // 3. Через 4 секунды возвращаем прежний текст кнопки
            setTimeout(() => {
                btn.textContent = 'Скачать игру';
                btn.style.pointerEvents = 'auto';
            }, 4000);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
