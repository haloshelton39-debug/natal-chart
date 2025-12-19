
# Подготовка данных для приложения: астрологические константы и справочники
import json

# Планеты и их символы
planets_data = {
    "sun": {"name": "Солнце", "symbol": "☉", "id": 0},
    "moon": {"name": "Луна", "symbol": "☽", "id": 1},
    "mercury": {"name": "Меркурий", "symbol": "☿", "id": 2},
    "venus": {"name": "Венера", "symbol": "♀", "id": 3},
    "mars": {"name": "Марс", "symbol": "♂", "id": 4},
    "jupiter": {"name": "Юпитер", "symbol": "♃", "id": 5},
    "saturn": {"name": "Сатурн", "symbol": "♄", "id": 6},
    "uranus": {"name": "Уран", "symbol": "♅", "id": 7},
    "neptune": {"name": "Нептун", "symbol": "♆", "id": 8},
    "pluto": {"name": "Плутон", "symbol": "♇", "id": 9},
}

# Зодиакальные знаки
zodiac_signs = {
    0: {"name": "Овен", "symbol": "♈", "element": "Огонь", "ruler": "Марс"},
    1: {"name": "Телец", "symbol": "♉", "element": "Земля", "ruler": "Венера"},
    2: {"name": "Близнецы", "symbol": "♊", "element": "Воздух", "ruler": "Меркурий"},
    3: {"name": "Рак", "symbol": "♋", "element": "Вода", "ruler": "Луна"},
    4: {"name": "Лев", "symbol": "♌", "element": "Огонь", "ruler": "Солнце"},
    5: {"name": "Дева", "symbol": "♍", "element": "Земля", "ruler": "Меркурий"},
    6: {"name": "Весы", "symbol": "♎", "element": "Воздух", "ruler": "Венера"},
    7: {"name": "Скорпион", "symbol": "♏", "element": "Вода", "ruler": "Плутон"},
    8: {"name": "Стрелец", "symbol": "♐", "element": "Огонь", "ruler": "Юпитер"},
    9: {"name": "Козерог", "symbol": "♑", "element": "Земля", "ruler": "Сатурн"},
    10: {"name": "Водолей", "symbol": "♒", "element": "Воздух", "ruler": "Уран"},
    11: {"name": "Рыбы", "symbol": "♓", "element": "Вода", "ruler": "Нептун"},
}

# Дома и их значения
houses_meanings = {
    1: "Личность, внешний вид, имидж",
    2: "Финансы, собственность, ценности",
    3: "Общение, учёба, короткие поездки",
    4: "Дом, семья, корни, недвижимость",
    5: "Творчество, развлечения, дети, любовь",
    6: "Работа, здоровье, подчинённые",
    7: "Брак, партнёрство, враги",
    8: "Смерть, наследство, сексуальность, трансформация",
    9: "Путешествия, высшее образование, философия",
    10: "Карьера, общественный статус, репутация",
    11: "Дружба, надежды, группы, сообщество",
    12: "Скрытое, изоляция, духовность, враги",
}

# Аспекты и их значения
aspects_data = {
    "conjunction": {"angle": 0, "name": "Соединение", "symbol": "☌", "description": "Усиление энергий", "type": "напряжённый"},
    "sextile": {"angle": 60, "name": "Секстиль", "symbol": "⬡", "description": "Гармоничный аспект", "type": "гармоничный"},
    "square": {"angle": 90, "name": "Квадратура", "symbol": "□", "description": "Динамическое напряжение", "type": "напряжённый"},
    "trine": {"angle": 120, "name": "Тригон", "symbol": "△", "description": "Гармонично, легко, таланты", "type": "гармоничный"},
    "opposition": {"angle": 180, "name": "Оппозиция", "symbol": "☍", "description": "Противоположные силы", "type": "напряжённый"},
}

# Сохраняем данные в файл для использования в приложении
celestial_data = {
    "planets": planets_data,
    "zodiac_signs": zodiac_signs,
    "houses_meanings": houses_meanings,
    "aspects": aspects_data
}

with open('astrology_data.json', 'w', encoding='utf-8') as f:
    json.dump(celestial_data, f, ensure_ascii=False, indent=2)

print("Данные астрологии сохранены в astrology_data.json")
print(f"Планеты: {len(planets_data)}")
print(f"Знаки зодиака: {len(zodiac_signs)}")
print(f"Дома: {len(houses_meanings)}")
print(f"Аспекты: {len(aspects_data)}")
