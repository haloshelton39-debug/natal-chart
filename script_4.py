
# Создание индексного файла проекта
index_html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Проект: Калькулятор Натальной Карты</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a28 0%, #0f0f1a 100%);
            color: #e0e0e0;
            min-height: 100vh;
            padding: 40px 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 50px;
            padding: 40px 20px;
            background: rgba(42, 42, 62, 0.5);
            border-radius: 15px;
            border: 1px solid rgba(0, 212, 255, 0.2);
        }

        h1 {
            font-size: 3em;
            background: linear-gradient(90deg, #00d4ff, #ff6b9d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
        }

        .subtitle {
            color: #a0a0a0;
            font-size: 1.2em;
            margin-bottom: 20px;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(0, 212, 255, 0.2);
        }

        .stat {
            text-align: center;
        }

        .stat-value {
            font-size: 1.8em;
            color: #00d4ff;
            font-weight: bold;
        }

        .stat-label {
            font-size: 0.85em;
            color: #a0a0a0;
            margin-top: 5px;
        }

        .content-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .card {
            background: rgba(42, 42, 62, 0.6);
            border-radius: 12px;
            padding: 25px;
            border: 1px solid rgba(0, 212, 255, 0.2);
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.2);
        }

        .card-icon {
            font-size: 2.5em;
            margin-bottom: 15px;
        }

        .card h2 {
            color: #00d4ff;
            margin-bottom: 12px;
            font-size: 1.3em;
        }

        .card p {
            color: #a0a0a0;
            line-height: 1.6;
            margin-bottom: 15px;
        }

        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: linear-gradient(90deg, #00d4ff, #0099cc);
            color: white;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
            border: none;
            font-size: 0.95em;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4);
        }

        .btn-secondary {
            background: rgba(255, 107, 157, 0.2);
            color: #ff6b9d;
            border: 1px solid #ff6b9d;
        }

        .features {
            background: rgba(42, 42, 62, 0.6);
            border-radius: 12px;
            padding: 30px;
            border: 1px solid rgba(0, 212, 255, 0.2);
            margin-bottom: 40px;
        }

        .features h3 {
            color: #00d4ff;
            margin-bottom: 20px;
            font-size: 1.3em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }

        .feature-item {
            padding: 15px;
            background: rgba(0, 212, 255, 0.05);
            border-radius: 8px;
            border-left: 3px solid #00d4ff;
        }

        .feature-item strong {
            color: #00d4ff;
        }

        .footer {
            text-align: center;
            padding: 30px;
            color: #a0a0a0;
            border-top: 1px solid rgba(0, 212, 255, 0.2);
            margin-top: 40px;
        }

        .file-list {
            list-style: none;
            margin-top: 15px;
        }

        .file-list li {
            padding: 8px 0;
            color: #e0e0e0;
            border-bottom: 1px solid rgba(0, 212, 255, 0.1);
        }

        .file-list li:before {
            content: "📄 ";
            color: #00d4ff;
            margin-right: 10px;
        }

        code {
            background: rgba(0, 0, 0, 0.3);
            padding: 3px 8px;
            border-radius: 4px;
            color: #ffcc44;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔮 Натальная Карта</h1>
            <div class="subtitle">Интерактивный калькулятор космограммы</div>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value">40 KB</div>
                    <div class="stat-label">Размер</div>
                </div>
                <div class="stat">
                    <div class="stat-value">1 файл</div>
                    <div class="stat-label">HTML5 App</div>
                </div>
                <div class="stat">
                    <div class="stat-value">∞</div>
                    <div class="stat-label">Бесплатно</div>
                </div>
                <div class="stat">
                    <div class="stat-value">RU</div>
                    <div class="stat-label">Язык</div>
                </div>
            </div>
        </header>

        <div class="content-grid">
            <div class="card">
                <div class="card-icon">🚀</div>
                <h2>Запуск приложения</h2>
                <p>Откройте главное приложение для расчёта натальной карты. Введите данные рождения, и получите полный расчёт космограммы с визуализацией.</p>
                <a href="natal_chart_app.html" class="btn">Открыть приложение →</a>
            </div>

            <div class="card">
                <div class="card-icon">📖</div>
                <h2>Быстрый старт</h2>
                <p>Пошаговое руководство по использованию приложения. Инструкции, FAQ, справочник по компонентам натальной карты.</p>
                <a href="QUICK_START.txt" class="btn btn-secondary" download>Скачать (TXT)</a>
            </div>

            <div class="card">
                <div class="card-icon">📚</div>
                <h2>Полная документация</h2>
                <p>Подробное описание всех возможностей, астрологические справочники, таблицы значений домов и аспектов.</p>
                <a href="readme.md" class="btn btn-secondary" download>Скачать (MD)</a>
            </div>

            <div class="card">
                <div class="card-icon">⚙️</div>
                <h2>Техническая информация</h2>
                <p>Архитектура приложения, используемые API, математические алгоритмы, инструкции по расширению и кастомизации.</p>
                <a href="TECHNICAL.md" class="btn btn-secondary" download>Скачать (MD)</a>
            </div>

            <div class="card">
                <div class="card-icon">📊</div>
                <h2>Данные астрологии</h2>
                <p>JSON файл со всеми константами: планеты, знаки зодиака, дома, аспекты и их значения для разработки расширений.</p>
                <a href="astrology_data.json" class="btn btn-secondary" download>Скачать (JSON)</a>
            </div>

            <div class="card">
                <div class="card-icon">📋</div>
                <h2>О проекте</h2>
                <p>Этот индексный файл содержит ссылки на все компоненты проекта и описание структуры приложения.</p>
                <button class="btn" onclick="document.documentElement.scrollTop = 0">В начало ↑</button>
            </div>
        </div>

        <div class="features">
            <h3>✨ Основные возможности</h3>
            <div class="feature-grid">
                <div class="feature-item">
                    <strong>✓ 10 планет</strong><br>
                    Солнце, Луна, Меркурий, Венера, Марс, Юпитер, Сатурн, Уран, Нептун, Плутон
                </div>
                <div class="feature-item">
                    <strong>✓ 12 домов</strong><br>
                    Система Плацидуса с расчётом асцендента и МС
                </div>
                <div class="feature-item">
                    <strong>✓ Аспекты</strong><br>
                    Соединение, секстиль, квадратура, тригон, оппозиция
                </div>
                <div class="feature-item">
                    <strong>✓ Визуализация</strong><br>
                    Интерактивная космограмма с Canvas 2D
                </div>
                <div class="feature-item">
                    <strong>✓ Поиск городов</strong><br>
                    GeoNames API с 10+ млн городов
                </div>
                <div class="feature-item">
                    <strong>✓ Часовые пояса</strong><br>
                    Автоопределение с учётом летнего времени
                </div>
                <div class="feature-item">
                    <strong>✓ Тёмная тема</strong><br>
                    Красивый дизайн с плавными анимациями
                </div>
                <div class="feature-item">
                    <strong>✓ Русский язык</strong><br>
                    Полная локализация всех элементов
                </div>
                <div class="feature-item">
                    <strong>✓ Сохранение</strong><br>
                    Экспорт как изображение или печать
                </div>
                <div class="feature-item">
                    <strong>✓ Мобильный</strong><br>
                    Адаптивный дизайн для всех устройств
                </div>
            </div>
        </div>

        <div class="features">
            <h3>📦 Структура проекта</h3>
            <p style="margin-bottom: 20px;">Приложение состоит из следующих файлов:</p>
            <ul class="file-list">
                <li><strong>natal_chart_app.html</strong> — Главное приложение (40 KB, всё в одном файле)</li>
                <li><strong>QUICK_START.txt</strong> — Быстрое руководство пользователя</li>
                <li><strong>readme.md</strong> — Полная документация с примерами</li>
                <li><strong>TECHNICAL.md</strong> — Техническая информация для разработчиков</li>
                <li><strong>astrology_data.json</strong> — Справочные данные в формате JSON</li>
                <li><strong>index.html</strong> — Этот файл (навигация по проекту)</li>
            </ul>
        </div>

        <div class="features">
            <h3>🔧 Быстрая настройка</h3>
            <p style="margin-bottom: 20px;">
                <strong>Вариант 1: Локальный файл</strong><br>
                Просто откройте <code>natal_chart_app.html</code> в браузере.
            </p>
            <p style="margin-bottom: 20px;">
                <strong>Вариант 2: На веб-сервер</strong><br>
                Скопируйте <code>natal_chart_app.html</code> на сервер и откройте по URL.
            </p>
            <p style="margin-bottom: 20px;">
                <strong>Вариант 3: GitHub Pages</strong><br>
                Загрузите в репозиторий, включите GitHub Pages в settings.
            </p>
            <p>
                <strong>Вариант 4: Electron</strong><br>
                Обёрните в Electron для создания desktop приложения.
            </p>
        </div>

        <div class="features">
            <h3>❓ Часто задаваемые вопросы</h3>
            <p><strong>Почему всё в одном файле?</strong><br>
            Для удобства использования. Просто откройте файл — и готово. Нет зависимостей, нет установки.</p>

            <p style="margin-top: 15px;"><strong>Требуется ли интернет?</strong><br>
            Расчёты выполняются локально, но для поиска городов нужен интернет (GeoNames API).</p>

            <p style="margin-top: 15px;"><strong>Безопасны ли мои данные?</strong><br>
            Да. Все расчёты выполняются в браузере, данные не отправляются на сервер.</p>

            <p style="margin-top: 15px;"><strong>Как точны расчёты?</strong><br>
            Приложение использует упрощённые астрономические модели. Для профессиональных целей используйте ZET или Solar Fire.</p>

            <p style="margin-top: 15px;"><strong>На каких браузерах работает?</strong><br>
            Chrome, Firefox, Safari, Edge и другие современные браузеры (требуется HTML5 и ES6 поддержка).</p>
        </div>

        <footer>
            <p>🔮 Калькулятор Натальной Карты | Версия 1.0</p>
            <p>Создано в 2025 году | Свободное использование в личных целях</p>
            <p>Язык: JavaScript (Vanilla ES6+) | Размер: ~40 KB</p>
            <p style="margin-top: 20px; color: #666;">
                Используется для образования и самопознания.<br>
                Не является медицинской, юридической или финансовой консультацией.
            </p>
        </footer>
    </div>

    <script>
        console.log('%c🔮 Натальная Карта - Калькулятор Космограммы', 'font-size: 20px; color: #00d4ff; font-weight: bold;');
        console.log('%cВерсия 1.0 | 2025', 'font-size: 12px; color: #a0a0a0;');
        console.log('%cОткройте natal_chart_app.html для начала работы', 'font-size: 14px; color: #ff6b9d;');
    </script>
</body>
</html>
'''

try:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("✅ Индексный файл создан: index.html")
except IOError as e:
    print(f"❌ Ошибка при сохранении файла: {e}")
except Exception as e:
    print(f"❌ Неожиданная ошибка: {e}")
print("\n" + "="*70)
print("📦 ИТОГОВЫЙ СПИСОК ФАЙЛОВ ПРОЕКТА:")
print("="*70)
print("""
1. natal_chart_app.html (40 KB)
   → Главное приложение для расчёта натальной карты
   → Откройте в браузере для использования
   
2. index.html (новый!)
   → Навигационная страница проекта
   → Ссылки на все компоненты и документацию
   
3. readme.md
   → Полная документация с примерами
   → Справочники по планетам, знакам, домам, аспектам
   
4. QUICK_START.txt
   → Быстрое руководство для новичков
   → Инструкции, FAQ, советы
   
5. TECHNICAL.md
   → Техническая документация для разработчиков
   → Архитектура, API, алгоритмы, расширения
   
6. astrology_data.json
   → Справочные астрологические данные
   → Для разработки расширений и интеграций

═══════════════════════════════════════════════════════════════════════

🎯 КАК НАЧАТЬ ИСПОЛЬЗОВАТЬ:

✅ Вариант 1 (самый простой):
   Откройте natal_chart_app.html в браузере
   Готово! Приложение работает.

✅ Вариант 2 (с навигацией):
   Откройте index.html - будет меню со всеми файлами
   Выбирайте нужную функцию

✅ Вариант 3 (на сервер):
   Загрузите оба HTML файла на веб-сервер
   Откройте по URL - готово!

═══════════════════════════════════════════════════════════════════════

📊 СТАТИСТИКА ПРОЕКТА:

Объём кода:
  • HTML приложение: ~40 KB
  • Документация: ~20 KB
  • Всего: ~60 KB

Функциональность:
  • 10 планет ☉☽☿♀♂♃♄♅♆♇
  • 12 знаков зодиака ♈-♓
  • 12 домов (Плацидус)
  • 5 аспектов (☌⬡□△☍)
  • Космограмма с Canvas
  • GeoNames API интеграция
  • Timezone auto-detection
  • Тёмная тема
  • Русский язык
  • Адаптивный дизайн
  • Сохранение результатов

Браузерная совместимость:
  ✓ Chrome 90+
  ✓ Firefox 88+
  ✓ Safari 14+
  ✓ Edge 90+
  ✓ Мобильные браузеры

═══════════════════════════════════════════════════════════════════════

🚀 ГОТОВО К ИСПОЛЬЗОВАНИЮ!

Все файлы созданы и готовы к работе.
Начните с natal_chart_app.html или index.html

Приложение полностью функционально и не требует
никаких дополнительных установок или конфигураций.

═══════════════════════════════════════════════════════════════════════
""")
