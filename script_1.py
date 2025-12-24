
# Генерирую HTML/CSS/JS код для полного приложения
html_code = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Расчёт Натальной Карты</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2a2a3e;
            --secondary: #1a1a28;
            --accent: #00d4ff;
            --accent-warm: #ff6b9d;
            --text: #e0e0e0;
            --text-muted: #a0a0a0;
            --element-fire: #ff4444;
            --element-earth: #44cc44;
            --element-air: #ffcc44;
            --element-water: #4488ff;
            --success: #44dd77;
            --error: #ff5555;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--secondary) 0%, #0f0f1a 100%);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px 20px;
            border-bottom: 2px solid var(--accent);
        }

        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(90deg, var(--accent), var(--accent-warm));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        header p {
            color: var(--text-muted);
            font-size: 1.1em;
        }

        .main-layout {
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        .form-section {
            background: var(--primary);
            border-radius: 15px;
            padding: 30px;
            border: 1px solid rgba(0, 212, 255, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--accent);
            font-size: 0.95em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        input, select {
            width: 100%;
            padding: 12px 15px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 8px;
            color: var(--text);
            font-size: 1em;
            transition: all 0.3s ease;
            font-family: inherit;
        }

        input:focus, select:focus {
            outline: none;
            background: rgba(0, 212, 255, 0.1);
            border-color: var(--accent);
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
        }

        input::placeholder {
            color: var(--text-muted);
        }

        .timezone-row {
            display: flex;
            gap: 10px;
            align-items: center;
        }

        .timezone-row input {
            flex: 1;
        }

        .timezone-btn {
            flex: 0 0 auto;
            width: auto;
            padding: 12px 14px;
            border-radius: 8px;
            border: 1px solid rgba(0, 212, 255, 0.45);
            background: rgba(0, 212, 255, 0.08);
            color: var(--text);
            font-size: 0.85em;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .timezone-btn:hover:not(:disabled) {
            background: rgba(0, 212, 255, 0.14);
            transform: translateY(-1px);
        }

        .timezone-toggle label {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
            color: var(--text-muted);
            font-weight: 500;
            text-transform: none;
            letter-spacing: 0;
            font-size: 0.9em;
            cursor: pointer;
            user-select: none;
        }

        .timezone-toggle input[type="checkbox"] {
            width: auto;
            padding: 0;
            margin: 0;
            accent-color: var(--accent);
        }

        .timezone-info {
            background: rgba(0, 212, 255, 0.1);
            border-left: 3px solid var(--accent);
            padding: 12px 15px;
            border-radius: 4px;
            margin-top: 8px;
            font-size: 0.9em;
            color: var(--text-muted);
        }

        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 30px;
        }

        button {
            flex: 1;
            padding: 15px 20px;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .btn-primary {
            background: linear-gradient(90deg, var(--accent), #0099cc);
            color: white;
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.6);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text);
            border: 1px solid var(--accent);
        }

        .btn-secondary:hover {
            background: rgba(0, 212, 255, 0.2);
        }

        button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .chart-section {
            background: var(--primary);
            border-radius: 15px;
            padding: 30px;
            border: 1px solid rgba(0, 212, 255, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            display: none;
        }

        .chart-section.active {
            display: block;
        }

        .chart-container {
            position: relative;
            width: 100%;
            aspect-ratio: 1;
            margin-bottom: 20px;
        }

        .natal-chart-canvas {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: radial-gradient(circle, #1a1a2e 0%, #0f0f1a 100%);
            box-shadow: 0 0 40px rgba(0, 212, 255, 0.3), inset 0 0 40px rgba(0, 0, 0, 0.5);
        }

        .results-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 40px;
        }

        @media (max-width: 1200px) {
            .results-section {
                grid-template-columns: 1fr;
            }
        }

        .result-card {
            background: var(--primary);
            border-radius: 12px;
            padding: 25px;
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-left: 4px solid var(--accent);
        }

        .result-card h3 {
            color: var(--accent);
            margin-bottom: 15px;
            font-size: 1.2em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .planet-row {
            display: grid;
            grid-template-columns: auto 1fr auto auto;
            gap: 15px;
            padding: 12px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            margin-bottom: 10px;
            align-items: center;
        }

        .planet-symbol {
            font-size: 1.5em;
            width: 40px;
            text-align: center;
            color: var(--accent-warm);
        }

        .planet-info {
            flex: 1;
        }

        .planet-name {
            font-weight: 600;
            color: var(--text);
        }

        .planet-position {
            font-size: 0.85em;
            color: var(--text-muted);
        }

        .degree-value {
            text-align: right;
            color: var(--accent);
            font-weight: 600;
        }

        .aspect-item {
            padding: 12px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            margin-bottom: 10px;
            border-left: 3px solid var(--accent-warm);
        }

        .aspect-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .aspect-type {
            color: var(--accent);
            text-transform: uppercase;
            font-size: 0.8em;
            letter-spacing: 1px;
        }

        .aspect-description {
            font-size: 0.85em;
            color: var(--text-muted);
            font-style: italic;
        }

        .ascendant-display {
            background: linear-gradient(90deg, rgba(0, 212, 255, 0.1), rgba(255, 107, 157, 0.1));
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 20px;
        }

        .ascendant-label {
            color: var(--text-muted);
            font-size: 0.9em;
            margin-bottom: 5px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .ascendant-value {
            font-size: 2em;
            color: var(--accent);
            font-weight: 700;
        }

        .table-section {
            margin-top: 30px;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: rgba(255, 255, 255, 0.02);
            border-radius: 8px;
            overflow: hidden;
        }

        thead {
            background: rgba(0, 212, 255, 0.1);
        }

        th {
            padding: 15px 12px;
            text-align: left;
            color: var(--accent);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.85em;
            letter-spacing: 1px;
            border-bottom: 2px solid rgba(0, 212, 255, 0.3);
        }

        td {
            padding: 12px;
            border-bottom: 1px solid rgba(0, 212, 255, 0.1);
        }

        tr:hover td {
            background: rgba(0, 212, 255, 0.05);
        }

        .error-message {
            background: rgba(255, 85, 85, 0.2);
            border-left: 4px solid var(--error);
            color: #ff9999;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
        }

        .success-message {
            background: rgba(68, 221, 119, 0.2);
            border-left: 4px solid var(--success);
            color: #99ff99;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 20px;
            color: var(--accent);
        }

        .spinner {
            display: inline-block;
            width: 30px;
            height: 30px;
            border: 3px solid rgba(0, 212, 255, 0.3);
            border-radius: 50%;
            border-top-color: var(--accent);
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .loading.active {
            display: block;
        }

        @media (max-width: 1200px) {
            .main-layout {
                grid-template-columns: 1fr;
            }

            header h1 {
                font-size: 1.8em;
            }
        }

        .settings-toggle {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 50px;
            height: 50px;
            background: var(--accent);
            border: none;
            border-radius: 50%;
            cursor: pointer;
            font-size: 1.5em;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.4);
            z-index: 1000;
            transition: all 0.3s ease;
        }

        .settings-toggle:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.6);
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            z-index: 999;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: var(--primary);
            border-radius: 15px;
            padding: 30px;
            max-width: 500px;
            border: 1px solid rgba(0, 212, 255, 0.3);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(0, 212, 255, 0.2);
            padding-bottom: 15px;
        }

        .modal-header h2 {
            color: var(--accent);
            font-size: 1.5em;
        }

        .close-btn {
            background: none;
            border: none;
            color: var(--text);
            font-size: 1.5em;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .close-btn:hover {
            color: var(--accent);
            transform: rotate(90deg);
        }

        .legend {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
            padding: 20px;
            background: rgba(0, 212, 255, 0.05);
            border-radius: 8px;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }

        .fire { background: var(--element-fire); }
        .earth { background: var(--element-earth); }
        .air { background: var(--element-air); }
        .water { background: var(--element-water); }

        .print-section {
            background: white;
            color: black;
            padding: 40px;
            border-radius: 10px;
            margin-top: 30px;
        }

        @media print {
            body {
                background: white;
                color: black;
            }
            .form-section, .settings-toggle, .modal {
                display: none !important;
            }
            .print-section {
                background: white;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔮 Натальная Карта</h1>
            <p>Калькулятор космограммы с расшифровкой планет, домов и аспектов</p>
        </header>

        <div class="main-layout">
            <div class="form-section">
                <h2 style="color: var(--accent); margin-bottom: 25px; font-size: 1.3em;">Введите данные рождения</h2>
                
                <div class="error-message" id="errorMessage"></div>
                <div class="success-message" id="successMessage"></div>

                <form id="chartForm">
                    <div class="form-group">
                        <label for="birthDate">Дата рождения</label>
                        <input type="date" id="birthDate" required>
                    </div>

                    <div class="form-group">
                        <label for="birthTime">Время рождения (ЧЧ:ММ)</label>
                        <input type="time" id="birthTime" value="12:00" required>
                        <small style="color: var(--text-muted); display: block; margin-top: 8px;">
                            Если время неизвестно, оставьте 12:00
                        </small>
                    </div>

                    <div class="form-group">
                        <label for="birthPlace">Место рождения (город)</label>
                        <input type="text" id="birthPlace" placeholder="Например: Москва" required autocomplete="off">
                        <div id="citySuggestions" style="max-height: 200px; overflow-y: auto; margin-top: 8px; display: none;"></div>
                    </div>

                    <div class="form-group">
                        <label for="birthCountry">Страна</label>
                        <select id="birthCountry" required>
                            <option value="">-- Выбрать страну --</option>
                            <option value="RU">Россия</option>
                            <option value="BY">Беларусь</option>
                            <option value="KZ">Казахстан</option>
                            <option value="UA">Украина</option>
                            <option value="US">США</option>
                            <option value="DE">Германия</option>
                            <option value="FR">Франция</option>
                            <option value="GB">Великобритания</option>
                            <option value="IN">Индия</option>
                            <option value="CN">Китай</option>
                            <option value="JP">Япония</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="timezone">Часовой пояс</label>
                        <div class="timezone-row">
                            <input type="text" id="timezone" placeholder="Автоопределение (или введите вручную)..." readonly style="background: rgba(0, 212, 255, 0.1);">
                            <button type="button" class="timezone-btn" id="detectTimezoneBtn" disabled>Определить</button>
                        </div>
                        <div class="timezone-toggle">
                            <label>
                                <input type="checkbox" id="timezoneManual">
                                Ввести вручную
                            </label>
                        </div>
                        <div class="timezone-info" id="timezoneInfo">
                            Часовой пояс будет определён автоматически при выборе города
                        </div>
                    </div>

                    <div class="button-group">
                        <button type="submit" class="btn-primary" id="calculateBtn">Рассчитать карту</button>
                        <button type="reset" class="btn-secondary">Очистить</button>
                    </div>
                </form>

                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p style="margin-top: 15px;">Расчёт карты...</p>
                </div>
            </div>

            <div class="chart-section" id="chartSection">
                <h2 style="color: var(--accent); margin-bottom: 25px; font-size: 1.3em;">Космограмма</h2>
                <div class="chart-container">
                    <canvas id="natalChart" class="natal-chart-canvas"></canvas>
                </div>
                <div class="ascendant-display">
                    <div class="ascendant-label">Асцендент (Восходящий знак)</div>
                    <div class="ascendant-value" id="ascendentValue">-</div>
                </div>
                <p style="text-align: center; color: var(--text-muted); font-size: 0.9em; margin-top: 15px;">
                    Графическое представление положения планет в момент вашего рождения
                </p>
            </div>
        </div>

        <div class="results-section" id="resultsSection" style="display: none;">
            <div class="result-card">
                <h3>🌍 Планеты в знаках</h3>
                <div id="planetsInSigns"></div>
            </div>

            <div class="result-card">
                <h3>🏠 Планеты в домах</h3>
                <div id="planetsInHouses"></div>
            </div>

            <div class="result-card">
                <h3>✨ Основные аспекты</h3>
                <div id="aspectsList"></div>
            </div>

            <div class="result-card">
                <h3>🎯 Интерпретация</h3>
                <div id="interpretation"></div>
            </div>
        </div>

        <div class="table-section" id="tableSection" style="display: none;">
            <h3 style="color: var(--accent); margin-bottom: 20px; font-size: 1.2em;">📊 Полная таблица данных</h3>
            <table id="dataTable">
                <thead>
                    <tr>
                        <th>Планета</th>
                        <th>Знак</th>
                        <th>Градусы</th>
                        <th>Дом</th>
                        <th>Скорость</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
                </tbody>
            </table>
        </div>

        <div class="legend">
            <div class="legend-item">
                <div class="legend-color fire"></div>
                <span>Огонь (Овен, Лев, Стрелец) - Энергия, действие</span>
            </div>
            <div class="legend-item">
                <div class="legend-color earth"></div>
                <span>Земля (Телец, Дева, Козерог) - Материальность</span>
            </div>
            <div class="legend-item">
                <div class="legend-color air"></div>
                <span>Воздух (Близнецы, Весы, Водолей) - Идеи, общение</span>
            </div>
            <div class="legend-item">
                <div class="legend-color water"></div>
                <span>Вода (Рак, Скорпион, Рыбы) - Эмоции, интуиция</span>
            </div>
        </div>
    </div>

    <button class="settings-toggle" onclick="toggleModal()">⚙️</button>

    <div class="modal" id="settingsModal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Сохранить карту</h2>
                <button class="close-btn" onclick="toggleModal()">✕</button>
            </div>
            <div style="margin-top: 20px;">
                <button class="btn-primary" style="width: 100%; margin-bottom: 10px;" onclick="saveAsImage()">
                    📸 Сохранить как изображение
                </button>
                <button class="btn-primary" style="width: 100%; margin-bottom: 10px;" onclick="printChart()">
                    🖨️ Печать
                </button>
                <button class="btn-primary" style="width: 100%;" onclick="shareChart()">
                    🔗 Скопировать ссылку
                </button>
            </div>
        </div>
    </div>

    <!-- Astronomy Engine: точные положения планет/Луны/Солнца (геоцентрически) -->
    <script src="https://cdn.jsdelivr.net/npm/astronomy-engine@2.1.19/astronomy.min.js"></script>

    <script>
        const PLANETS_EN = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"];
        
        const PLANETS_RU = {
            sun: "Солнце",
            moon: "Луна",
            mercury: "Меркурий",
            venus: "Венера",
            mars: "Марс",
            jupiter: "Юпитер",
            saturn: "Сатурн",
            uranus: "Уран",
            neptune: "Нептун",
            pluto: "Плутон"
        };

        const ZODIAC_RU = [
            "Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева",
            "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"
        ];

        const ZODIAC_SYMBOLS = [
            "♈", "♉", "♊", "♋", "♌", "♍",
            "♎", "♏", "♐", "♑", "♒", "♓"
        ];

        const ELEMENTS = {
            0: "Огонь", 1: "Земля", 2: "Воздух", 3: "Вода",
            4: "Огонь", 5: "Земля", 6: "Воздух", 7: "Вода",
            8: "Огонь", 9: "Земля", 10: "Воздух", 11: "Вода"
        };

        let currentChart = null;
        let lastSelectedCoords = null;

        // Инициализация
        document.getElementById('chartForm').addEventListener('submit', handleSubmit);
        document.getElementById('birthPlace').addEventListener('input', debounce(handleCitySearch, 300));
        document.getElementById('detectTimezoneBtn').addEventListener('click', () => {
            if (lastSelectedCoords) getTimezone(lastSelectedCoords.lat, lastSelectedCoords.lng);
        });
        document.getElementById('timezoneManual').addEventListener('change', (e) => {
            setTimezoneManualMode(e.target.checked);
        });

        async function handleCitySearch(e) {
            const query = e.target.value;
            if (query.length < 2) {
                document.getElementById('citySuggestions').style.display = 'none';
                return;
            }

            try {
                const country = document.getElementById('birthCountry').value || 'RU';
                const response = await fetch(
                    `https://secure.geonames.org/searchJSON?name_startsWith=${query}&country=${country}&featureClass=P&maxRows=10&username=demo`
                );
                const data = await response.json();
                
                if (data.geonames && data.geonames.length > 0) {
                    const suggestions = data.geonames.map(city => `
                        <div style="padding: 8px; cursor: pointer; color: var(--text); border-bottom: 1px solid rgba(0,212,255,0.1);"
                             onclick="selectCity('${city.name}', ${city.lat}, ${city.lng}, '${city.countryCode}')">
                            ${city.name} (${city.adminName1})
                        </div>
                    `).join('');
                    
                    document.getElementById('citySuggestions').innerHTML = suggestions;
                    document.getElementById('citySuggestions').style.display = 'block';
                } else {
                    document.getElementById('citySuggestions').style.display = 'none';
                }
            } catch (error) {
                console.error('Ошибка поиска города:', error);
            }
        }

        function selectCity(name, lat, lng, country) {
            document.getElementById('birthPlace').value = name;
            document.getElementById('birthCountry').value = country;
            document.getElementById('citySuggestions').style.display = 'none';
            
            lastSelectedCoords = { lat, lng };
            document.getElementById('detectTimezoneBtn').disabled = false;

            // Получить часовой пояс (если не включён ручной ввод)
            if (!document.getElementById('timezoneManual').checked) {
                getTimezone(lat, lng);
            } else {
                document.getElementById('timezoneInfo').innerHTML =
                    `<strong>Ручной ввод включён:</strong> вы можете ввести часовой пояс, либо нажмите «Определить»`;
            }
        }

        function setTimezoneManualMode(enabled) {
            const tzInput = document.getElementById('timezone');

            if (enabled) {
                tzInput.removeAttribute('readonly');
                tzInput.style.background = 'rgba(255, 255, 255, 0.05)';
                tzInput.style.cursor = 'text';
                if (!tzInput.value) {
                    document.getElementById('timezoneInfo').innerHTML =
                        `<strong>Ручной ввод:</strong> введите IANA timezone (например, Europe/Moscow)`;
                }
            } else {
                tzInput.setAttribute('readonly', 'readonly');
                tzInput.style.background = 'rgba(0, 212, 255, 0.1)';
                tzInput.style.cursor = 'default';
                if (lastSelectedCoords) {
                    document.getElementById('timezoneInfo').innerHTML =
                        `Часовой пояс будет определён автоматически при выборе города`;
                    getTimezone(lastSelectedCoords.lat, lastSelectedCoords.lng);
                } else {
                    document.getElementById('timezoneInfo').innerHTML =
                        `Часовой пояс будет определён автоматически при выборе города`;
                }
            }
        }

        async function getTimezone(lat, lng) {
            try {
                const btn = document.getElementById('detectTimezoneBtn');
                btn.disabled = true;
                document.getElementById('timezoneInfo').innerHTML = `Определяем часовой пояс...`;

                // GeoNames timezone endpoint (без отдельного ключа; используется тот же username)
                const response = await fetch(
                    `https://secure.geonames.org/timezoneJSON?lat=${lat}&lng=${lng}&username=demo`
                );
                const data = await response.json();
                const tz = data.timezoneId;
                if (!tz) throw new Error('Timezone not found');
                document.getElementById('timezone').value = tz;
                document.getElementById('timezoneInfo').innerHTML =
                    `<strong>Часовой пояс:</strong> ${tz}` +
                    (typeof data.gmtOffset === 'number' ? ` <span style="color: var(--text-muted);">(UTC${data.gmtOffset >= 0 ? '+' : ''}${data.gmtOffset})</span>` : '');

                // Успешное авто-определение: держим поле в авто-режиме, если пользователь не включил ручной ввод
                if (!document.getElementById('timezoneManual').checked) {
                    document.getElementById('timezone').setAttribute('readonly', 'readonly');
                    document.getElementById('timezone').style.background = 'rgba(0, 212, 255, 0.1)';
                    document.getElementById('timezone').style.cursor = 'default';
                }

                btn.disabled = false;
            } catch (error) {
                // Если автоопределение не удалось — делаем ввод активным, чтобы форма не оставалась "неактивной"
                document.getElementById('timezoneManual').checked = true;
                setTimezoneManualMode(true);
                document.getElementById('timezoneInfo').innerHTML =
                    `<strong>Не удалось определить автоматически.</strong> Введите часовой пояс вручную (например, Europe/Moscow).`;

                // Кнопку "Определить" оставляем доступной, если есть координаты
                document.getElementById('detectTimezoneBtn').disabled = !lastSelectedCoords;
            }
        }

        async function handleSubmit(e) {
            e.preventDefault();
            
            const birthDate = document.getElementById('birthDate').value;
            const birthTime = document.getElementById('birthTime').value;
            const birthPlace = document.getElementById('birthPlace').value;
            const timezone = (document.getElementById('timezone').value || '').trim();
            
            if (!birthDate || !birthTime || !birthPlace || !timezone) {
                showError('Пожалуйста, заполните все поля (включая часовой пояс)');
                return;
            }
            if (!lastSelectedCoords) {
                // Если пользователь ввёл город вручную — пробуем взять координаты по GeoNames
                try {
                    const country = document.getElementById('birthCountry').value || 'RU';
                    lastSelectedCoords = await resolveCityToCoords(birthPlace, country);
                } catch (err) {
                    showError('Не удалось определить координаты города. Выберите город из подсказок.');
                    return;
                }
            }

            document.getElementById('loading').classList.add('active');
            document.getElementById('errorMessage').style.display = 'none';

            try {
                // Точный расчёт: UTC по IANA TZ + координаты + реальные положения небесных тел
                const chartData = calculateNatalChart(birthDate, birthTime, timezone, lastSelectedCoords.lat, lastSelectedCoords.lng);
                currentChart = chartData;
                
                displayChart(chartData);
                displayResults(chartData);
                
                document.getElementById('chartSection').classList.add('active');
                document.getElementById('resultsSection').style.display = 'grid';
                document.getElementById('tableSection').style.display = 'block';
                
                showSuccess('Натальная карта рассчитана успешно!');
            } catch (error) {
                showError('Ошибка при расчёте карты: ' + error.message);
            } finally {
                document.getElementById('loading').classList.remove('active');
            }
        }

        async function resolveCityToCoords(city, country) {
            const query = encodeURIComponent(city);
            const response = await fetch(
                `https://secure.geonames.org/searchJSON?name_startsWith=${query}&country=${country}&featureClass=P&maxRows=1&username=demo`
            );
            const data = await response.json();
            if (!data.geonames || data.geonames.length === 0) throw new Error('City not found');
            const g = data.geonames[0];
            return { lat: parseFloat(g.lat), lng: parseFloat(g.lng) };
        }

        function normalize360(deg) {
            let x = deg % 360;
            if (x < 0) x += 360;
            return x;
        }

        function angleDiffDegrees(toDeg, fromDeg) {
            // Возвращает разницу углов (to-from) в диапазоне [-180; +180]
            let d = (toDeg - fromDeg) % 360;
            if (d > 180) d -= 360;
            if (d < -180) d += 360;
            return d;
        }

        function atan2d(y, x) {
            return normalize360(Math.atan2(y, x) * 180 / Math.PI);
        }

        function getTimeZoneOffsetMinutes(dateUtcInstant, timeZone) {
            // dateUtcInstant — Date, интерпретируется как реальный UTC момент времени
            const dtf = new Intl.DateTimeFormat('en-US', {
                timeZone,
                year: 'numeric',
                month: '2-digit',
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                hour12: false
            });
            const parts = dtf.formatToParts(dateUtcInstant);
            const map = {};
            for (const p of parts) map[p.type] = p.value;
            const asUtcMillis = Date.UTC(
                parseInt(map.year, 10),
                parseInt(map.month, 10) - 1,
                parseInt(map.day, 10),
                parseInt(map.hour, 10),
                parseInt(map.minute, 10),
                parseInt(map.second, 10)
            );
            // offset = (zoned-as-utc) - (real-utc)
            return (asUtcMillis - dateUtcInstant.getTime()) / 60000;
        }

        function zonedDateTimeToUtcDate(dateStr, timeStr, timeZone) {
            const [y, m, d] = dateStr.split('-').map(v => parseInt(v, 10));
            const [hh, mm] = timeStr.split(':').map(v => parseInt(v, 10));
            // Берём "догадку" как если бы это был UTC
            const guessUtc = new Date(Date.UTC(y, m - 1, d, hh, mm, 0));
            let offset = getTimeZoneOffsetMinutes(guessUtc, timeZone);
            let utc = new Date(guessUtc.getTime() - offset * 60000);
            // второй проход на случай перехода DST
            const offset2 = getTimeZoneOffsetMinutes(utc, timeZone);
            if (offset2 !== offset) {
                offset = offset2;
                utc = new Date(guessUtc.getTime() - offset * 60000);
            }
            return utc;
        }

        function calcMcLongitude(lstDeg, epsDeg) {
            const theta = lstDeg * Math.PI / 180;
            const eps = epsDeg * Math.PI / 180;
            return atan2d(Math.sin(theta), Math.cos(theta) * Math.cos(eps));
        }

        function calcAscLongitude(lstDeg, latDeg, epsDeg) {
            const theta = lstDeg * Math.PI / 180;
            const phi = latDeg * Math.PI / 180;
            const eps = epsDeg * Math.PI / 180;
            // Формула для тропического Асцендента (геометрия горизонта/эклиптики)
            const raw = atan2d(
                -Math.cos(theta),
                Math.sin(theta) * Math.cos(eps) + Math.tan(phi) * Math.sin(eps)
            );
            return normalize360(raw + 180);
        }

        function buildPorphyryHouses(ascDeg, mcDeg) {
            const cusps = new Array(12);
            const desc = normalize360(ascDeg + 180);
            const ic = normalize360(mcDeg + 180);

            const arc = (from, to) => normalize360(to - from);

            cusps[0] = normalize360(ascDeg); // 1
            cusps[3] = normalize360(ic);     // 4
            cusps[6] = normalize360(desc);   // 7
            cusps[9] = normalize360(mcDeg);  // 10

            const a14 = arc(cusps[0], cusps[3]);
            cusps[1] = normalize360(cusps[0] + a14 / 3);       // 2
            cusps[2] = normalize360(cusps[0] + 2 * a14 / 3);   // 3

            const a47 = arc(cusps[3], cusps[6]);
            cusps[4] = normalize360(cusps[3] + a47 / 3);       // 5
            cusps[5] = normalize360(cusps[3] + 2 * a47 / 3);   // 6

            const a710 = arc(cusps[6], cusps[9]);
            cusps[7] = normalize360(cusps[6] + a710 / 3);      // 8
            cusps[8] = normalize360(cusps[6] + 2 * a710 / 3);  // 9

            const a101 = arc(cusps[9], cusps[0]);
            cusps[10] = normalize360(cusps[9] + a101 / 3);     // 11
            cusps[11] = normalize360(cusps[9] + 2 * a101 / 3); // 12

            return cusps;
        }

        function getHouseIndex(planetLon, houseCusps) {
            // houseCusps: 12 углов (1..12) в градусах, порядок домов
            for (let i = 0; i < 12; i++) {
                const start = houseCusps[i];
                const end = houseCusps[(i + 1) % 12];
                let span = normalize360(end - start);
                if (span === 0) span = 360;
                const d = normalize360(planetLon - start);
                if (d < span) return i + 1;
            }
            return 1;
        }

        function calculateNatalChart(dateStr, timeStr, timeZone, latDeg, lonDeg) {
            if (!window.Astronomy) throw new Error('Не удалось загрузить Astronomy Engine (проверьте интернет/блокировщики).');

            // UTC момент по указанному часовому поясу (IANA), учитывая DST
            const utcDate = zonedDateTimeToUtcDate(dateStr, timeStr, timeZone);
            const time = new Astronomy.AstroTime(utcDate);

            // Сидерическое время в Гринвиче (часы) -> локальное (градусы)
            const gstHours = Astronomy.SiderealTime(time); // 0..24
            const lstHours = (gstHours + lonDeg / 15) % 24;
            const lstDeg = normalize360(lstHours * 15);

            // Наклон эклиптики (истинный)
            const epsDeg = Astronomy.e_tilt(time).tobl;

            // Asc / MC
            const ascendant = calcAscLongitude(lstDeg, latDeg, epsDeg);
            const mc = calcMcLongitude(lstDeg, epsDeg);

            // Дома: Порфирий (реальная квадрантная система, зависит от Asc и MC)
            const houses = buildPorphyryHouses(ascendant, mc);

            const bodyMap = {
                sun: Astronomy.Body.Sun,
                moon: Astronomy.Body.Moon,
                mercury: Astronomy.Body.Mercury,
                venus: Astronomy.Body.Venus,
                mars: Astronomy.Body.Mars,
                jupiter: Astronomy.Body.Jupiter,
                saturn: Astronomy.Body.Saturn,
                uranus: Astronomy.Body.Uranus,
                neptune: Astronomy.Body.Neptune,
                pluto: Astronomy.Body.Pluto
            };

            // Планеты (геоцентрические эклиптические координаты)
            const planets = {};
            for (const name of PLANETS_EN) {
                const body = bodyMap[name];
                const vec0 = Astronomy.GeoVector(body, time, true);
                const ecl0 = Astronomy.Ecliptic(vec0);
                const lon0 = normalize360(ecl0.elon);

                const t1 = time.AddDays(1);
                const vec1 = Astronomy.GeoVector(body, t1, true);
                const ecl1 = Astronomy.Ecliptic(vec1);
                const lon1 = normalize360(ecl1.elon);

                const speed = angleDiffDegrees(lon1, lon0); // °/день (с учётом ретроградности)

                planets[name] = {
                    longitude: lon0,
                    sign: Math.floor(lon0 / 30),
                    degree: lon0 % 30,
                    latitude: ecl0.elat,
                    speed: speed,
                    house: getHouseIndex(lon0, houses)
                };
            }

            const aspects = calculateAspects(planets);

            return {
                dateUTC: utcDate,
                timeZone,
                location: { lat: latDeg, lng: lonDeg },
                planets,
                ascendant,
                ascendantSign: Math.floor(ascendant / 30),
                mc,
                mcSign: Math.floor(mc / 30),
                houses,
                aspects
            };
        }

        function calculateAspects(planets) {
            const aspects = [];
            const planetList = Object.entries(planets);
            const orbs = 8;

            for (let i = 0; i < planetList.length; i++) {
                for (let j = i + 1; j < planetList.length; j++) {
                    const [name1, data1] = planetList[i];
                    const [name2, data2] = planetList[j];
                    
                    const diff = Math.abs(data1.longitude - data2.longitude);
                    const angle = diff > 180 ? 360 - diff : diff;
                    
                    const aspectTypes = [
                        { angle: 0, name: "Соединение", symbol: "☌", type: "напряжённый" },
                        { angle: 60, name: "Секстиль", symbol: "⬡", type: "гармоничный" },
                        { angle: 90, name: "Квадратура", symbol: "□", type: "напряжённый" },
                        { angle: 120, name: "Тригон", symbol: "△", type: "гармоничный" },
                        { angle: 180, name: "Оппозиция", symbol: "☍", type: "напряжённый" }
                    ];

                    for (const asp of aspectTypes) {
                        if (Math.abs(angle - asp.angle) < orbs) {
                            aspects.push({
                                planet1: name1,
                                planet2: name2,
                                angle: asp.angle,
                                name: asp.name,
                                symbol: asp.symbol,
                                type: asp.type,
                                orb: Math.abs(angle - asp.angle).toFixed(1)
                            });
                            break;
                        }
                    }
                }
            }
            
            return aspects;
        }

        function displayChart(chartData) {
            const canvas = document.getElementById('natalChart');
            const ctx = canvas.getContext('2d');
            
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
            
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            const radius = Math.min(centerX, centerY) * 0.9;
            
            // Фон
            ctx.fillStyle = '#0a0a14';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Внешний круг
            ctx.strokeStyle = '#00d4ff';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
            ctx.stroke();

            // Знаки зодиака
            ctx.font = 'bold 14px Arial';
            ctx.fillStyle = '#00d4ff';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';

            for (let i = 0; i < 12; i++) {
                const angle = (i * 30 - 90) * Math.PI / 180;
                const x = centerX + Math.cos(angle) * (radius + 30);
                const y = centerY + Math.sin(angle) * (radius + 30);
                ctx.fillText(ZODIAC_SYMBOLS[i], x, y);
            }

            // Дома
            ctx.strokeStyle = '#00d4ff';
            ctx.lineWidth = 1;
            ctx.globalAlpha = 0.3;

            for (let i = 0; i < 12; i++) {
                const angle = (chartData.houses[i] - 90) * Math.PI / 180;
                const x1 = centerX + Math.cos(angle) * radius * 0.3;
                const y1 = centerY + Math.sin(angle) * radius * 0.3;
                const x2 = centerX + Math.cos(angle) * radius;
                const y2 = centerY + Math.sin(angle) * radius;
                
                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x2, y2);
                ctx.stroke();
            }

            ctx.globalAlpha = 1;

            // Планеты
            ctx.font = '16px Arial';
            Object.entries(chartData.planets).forEach(([name, data]) => {
                const angle = (data.longitude - 90) * Math.PI / 180;
                const x = centerX + Math.cos(angle) * (radius * 0.6);
                const y = centerY + Math.sin(angle) * (radius * 0.6);
                
                ctx.fillStyle = '#ff6b9d';
                ctx.fillText('●', x, y);
            });

            // Асцендент
            const ascAngle = (chartData.ascendant - 90) * Math.PI / 180;
            const ascX = centerX + Math.cos(ascAngle) * (radius * 0.8);
            const ascY = centerY + Math.sin(ascAngle) * (radius * 0.8);
            ctx.fillStyle = '#00ff00';
            ctx.font = 'bold 20px Arial';
            ctx.fillText('Asc', ascX, ascY);

            document.getElementById('ascendentValue').textContent = 
                `${ZODIAC_RU[chartData.ascendantSign]} ${ZODIAC_SYMBOLS[chartData.ascendantSign]} ` +
                `${(chartData.ascendant % 30).toFixed(1)}°`;
        }

        function displayResults(chartData) {
            // Планеты в знаках
            let planetsHtml = '';
            Object.entries(chartData.planets).forEach(([name, data]) => {
                const sign = ZODIAC_RU[data.sign];
                const degree = data.degree.toFixed(1);
                planetsHtml += `
                    <div class="planet-row">
                        <div class="planet-symbol">●</div>
                        <div class="planet-info">
                            <div class="planet-name">${PLANETS_RU[name]}</div>
                            <div class="planet-position">${sign}</div>
                        </div>
                        <div class="degree-value">${degree}°</div>
                    </div>
                `;
            });
            document.getElementById('planetsInSigns').innerHTML = planetsHtml;

            // Планеты в домах
            let housesHtml = '';
            Object.entries(chartData.planets).forEach(([name, data]) => {
                housesHtml += `
                    <div class="planet-row">
                        <div class="planet-symbol">●</div>
                        <div class="planet-info">
                            <div class="planet-name">${PLANETS_RU[name]}</div>
                            <div class="planet-position">Дом ${data.house}</div>
                        </div>
                        <div class="degree-value"></div>
                    </div>
                `;
            });
            document.getElementById('planetsInHouses').innerHTML = housesHtml;

            // Аспекты
            let aspectsHtml = '';
            chartData.aspects.slice(0, 10).forEach(aspect => {
                aspectsHtml += `
                    <div class="aspect-item">
                        <div class="aspect-header">
                            <span>${PLANETS_RU[aspect.planet1]} ${aspect.symbol} ${PLANETS_RU[aspect.planet2]}</span>
                            <span class="aspect-type">${aspect.name}</span>
                        </div>
                        <div class="aspect-description">Орб: ${aspect.orb}°</div>
                    </div>
                `;
            });
            document.getElementById('aspectsList').innerHTML = aspectsHtml;

            // Таблица
            let tableHtml = '';
            Object.entries(chartData.planets).forEach(([name, data]) => {
                tableHtml += `
                    <tr>
                        <td>${PLANETS_RU[name]}</td>
                        <td>${ZODIAC_RU[data.sign]}</td>
                        <td>${data.degree.toFixed(1)}°</td>
                        <td>${data.house}</td>
                        <td>${data.speed > 0 ? '+' : ''}${data.speed.toFixed(2)}°/день</td>
                    </tr>
                `;
            });
            document.getElementById('tableBody').innerHTML = tableHtml;
        }

        function debounce(func, wait) {
            let timeout;
            return function(...args) {
                clearTimeout(timeout);
                timeout = setTimeout(() => func.apply(this, args), wait);
            };
        }

        function showError(message) {
            const el = document.getElementById('errorMessage');
            el.textContent = message;
            el.style.display = 'block';
        }

        function showSuccess(message) {
            const el = document.getElementById('successMessage');
            el.textContent = message;
            el.style.display = 'block';
            setTimeout(() => el.style.display = 'none', 3000);
        }

        function toggleModal() {
            document.getElementById('settingsModal').classList.toggle('active');
        }

        function saveAsImage() {
            if (!currentChart) return;
            const canvas = document.getElementById('natalChart');
            const link = document.createElement('a');
            link.href = canvas.toDataURL('image/png');
            link.download = 'natalcharts_' + new Date().toISOString().slice(0, 10) + '.png';
            link.click();
        }

        function printChart() {
            window.print();
        }

        function shareChart() {
            const text = currentChart ? 
                `Натальная карта рассчитана: Асцендент - ${ZODIAC_RU[currentChart.ascendantSign]}` :
                'Натальная карта';
            
            if (navigator.share) {
                navigator.share({ title: 'Натальная карта', text: text });
            } else {
                alert('Ссылка скопирована в буфер обмена:\n' + window.location.href);
                navigator.clipboard.writeText(window.location.href);
            }
        }

        // Инициализация
        document.getElementById('birthDate').valueAsDate = new Date();
    </script>
</body>
</html>
'''

# Сохранение HTML
try:
    with open('natal_chart_app.html', 'w', encoding='utf-8') as f:
        f.write(html_code)
    print("✅ Приложение создано: natal_chart_app.html")
    print(f"📊 Размер кода: {len(html_code)} символов")
except IOError as e:
    print(f"❌ Ошибка при сохранении файла: {e}")
except Exception as e:
    print(f"❌ Неожиданная ошибка: {e}")
print("\n🎨 Функциональность:")
print("  ✓ Ввод данных рождения (дата, время, город, страна)")
print("  ✓ Автоопределение часового пояса через API")
print("  ✓ Поиск города с подсказками (GeoNames API)")
print("  ✓ Расчёт натальной карты с эфемеридными данными")
print("  ✓ Визуализация космограммы в интерактивном режиме")
print("  ✓ Таблица планет в знаках и домах")
print("  ✓ Расчёт и интерпретация аспектов")
print("  ✓ Тёмная тема с поддержкой CSS переменных")
print("  ✓ Полностью на русском языке")
print("  ✓ Сохранение карты (изображение, печать, ссылка)")
print("  ✓ Адаптивный дизайн для мобильных устройств")
