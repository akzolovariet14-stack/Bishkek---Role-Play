from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Bishkek Role Play</title>
    <style>
        /* Стильный вишнево-черный перелив */
        body { 
            background: linear-gradient(135deg, #2b0000 0%, #000000 50%, #4a0404 100%);
            background-size: 400% 400%;
            animation: gradientMove 8s ease infinite;
            color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; 
        }
        @keyframes gradientMove { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        
        h1, h2 { color: #fff; text-align: center; text-shadow: 2px 2px 6px #000; }
        .nav { display: flex; justify-content: center; gap: 20px; margin-bottom: 30px; }
        button { 
            background-color: #000; color: #ff0000; border: 3px solid #ff0000; 
            padding: 20px 40px; cursor: pointer; font-size: 18px; font-weight: bold; 
            border-radius: 10px; transition: 0.3s;
        }
        button:hover { background-color: #ff0000; color: #fff; transform: scale(1.1); }
        
        .section { display: none; border: 3px solid #ff0000; padding: 30px; border-radius: 20px; background: rgba(0,0,0,0.85); line-height: 1.6; }
        .active { display: block; }
        
        .donate-item { display: flex; justify-content: space-between; align-items: center; padding: 15px; border-bottom: 1px solid #444; font-size: 18px; }
        .footer { text-align: center; margin-top: 30px; font-weight: bold; color: #ff0000; }
    </style>
</head>
<body>
    <h1>BISHKEK ROLE PLAY</h1>
    <div class="nav">
        <button onclick="show('home')">Главная</button>
        <button onclick="show('rules')">Правила</button>
        <button onclick="show('guide')">Как играть</button>
        <button onclick="show('donate')">Донат</button>
    </div>

    <div id="home" class="section active">
        <h2>Добро пожаловать в Bishkek Role Play</h2>
        <p>Бишкек — это город контрастов и великих возможностей. Наш сервер — это полноценная симуляция реальной жизни в сердце Кыргызстана. Здесь каждый игрок может прочувствовать атмосферу наших улиц, от шумных рынков до спокойных горных пейзажей Ала-Тоо.</p>
        <p>Экономика нашего сервера продумана до мелочей: бизнес, торговля, работа в государственных структурах или нелегальный заработок в криминальном мире. Мы создали экосистему, где каждый игрок важен. Наш народ — это игроки, которые ценят честность, патриотизм и качественный RP-процесс. Вместе мы строим лучшее сообщество, где каждый может стать легендой.</p>
        <div class="footer">Разработано проект Bishkek RP "Ариет Акжолов и Нурислам Эндешеев"</div>
    </div>

    <div id="rules" class="section">
        <h2>Правила сервера (1-25)</h2>
        <div id="rules-list"></div>
    </div>

    <div id="guide" class="section">
        <h2>Сюжетный путь игрока</h2>
        <div id="guide-list"></div>
    </div>

    <div id="donate" class="section">
        <h2>Донат</h2>
        <div class="donate-item">100 сом = 230 BC <button onclick="alert('Купить 100 сом')">Купить</button></div>
        <div class="donate-item">250 сом = 390 BC <button onclick="alert('Купить 250 сом')">Купить</button></div>
        <div class="donate-item">400 сом = 560 BC <button onclick="alert('Купить 400 сом')">Купить</button></div>
        <div class="donate-item">590 сом = 680 BC <button onclick="alert('Купить 590 сом')">Купить</button></div>
        <div class="donate-item">990 сом = 1590 BC <button onclick="alert('Купить 990 сом')">Купить</button></div>
        <div class="donate-item">1380 сом = 2190 BC <button onclick="alert('Купить 1380 сом')">Купить</button></div>
        <div class="donate-item">2180 сом = 3500 BC <button onclick="alert('Купить 2180 сом')">Купить</button></div>
        <div class="donate-item">3590 сом = 4390 BC <button onclick="alert('Купить 3590 сом')">Купить</button></div>
        <div class="donate-item">4990 сом = 7290 BC <button onclick="alert('Купить 4990 сом')">Купить</button></div>
    </div>

    <script>
        function show(id) {
            document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
            document.getElementById(id).classList.add('active');
        }
        
        const rules = ["Ник Имя_Фамилия", "Читы (Бан)", "DM запрещен", "DB запрещен", "SK запрещен", "RK запрещен", "MG запрещен", "PG запрещен", "Уход от RP (Варн)", "Злоупотребление командами", "Выдача за админа", "Багоюз", "Реклама", "Правила семьи", "Правила ОПГ", "Собеседования", "Мошенничество", "Зеленая зона", "Защита родных", "Non-RP поведение", "Правила RP", "Работы", "VIP-чат", "Рынок", "Налоги"];
        const rulesList = document.getElementById('rules-list');
        rules.forEach((r, i) => rulesList.innerHTML += '<div style="margin-bottom:10px;">' + (i+1) + '. ' + r + '</div>');

        const guide = ["Спавн на вокзале, капитал 5000 сом.", "Визит в Правительство за паспортом.", "Получение медкарты в больнице.", "Первая работа: Шахта или Курьер.", "Накопление денег до 2 уровня.", "Автошкола: сдача на права.", "Покупка первого автомобиля.", "Работа таксистом.", "Работа автобусником.", "Работа дальнобойщиком.", "Работа мусоровозом.", "Накопление на недвижимость.", "Покупка собственного дома.", "Вступление в гос. органы (ГКНБ/МВД).", "Собеседование и инструктаж.", "Альтернативный путь: Вступление в ОПГ.", "Торговля на рынке (ЦУМ).", "Участие в RP-митингах.", "Создание семьи и бизнеса.", "Стань легендой нашего штата!"];
        const guideList = document.getElementById('guide-list');
        guide.forEach((g, i) => guideList.innerHTML += '<div style="margin-bottom:8px;"><b>' + (i+1) + '.</b> ' + g + '</div>');
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)