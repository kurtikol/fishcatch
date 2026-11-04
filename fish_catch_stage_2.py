# === Stage 2: Проверка полей ===
# Project: FishCatch
import datetime


DATE_FORMAT = "%Y-%m-%d"


def normalize_date(value):
    if value is None:
        raise ValueError("Дата не может быть пустой")
    text = value.strip()
    if not text:
        raise ValueError("Дата не может быть пустой")
    try:
        return datetime.datetime.strptime(text, DATE_FORMAT).date()
    except ValueError:
        raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")


def normalize_waterbody(value):
    if value is None:
        raise ValueError("Водоём не может быть пустым")
    text = value.strip()
    if not text:
        raise ValueError("Водоём не может быть пустым")
    if len(text) > 80:
        raise ValueError("Водоём слишком длинный")
    return text


def normalize_gear(value):
    if value is None:
        raise ValueError("Снасть не может быть пустой")
    text = value.strip()
    if not text:
        raise ValueError("Снасть не может быть пустой")
    if len(text) > 60:
        raise ValueError("Снасть слишком длинная")
    return text


def normalize_weather(value):
    if value is None:
        raise ValueError("Погода не может быть пустой")
    text = value.strip()
    if not text:
        raise ValueError("Погода не может быть пустой")
    return text


def validate_trip(raw):
    try:
        date = normalize_date(raw.get("date"))
        waterbody = normalize_waterbody(raw.get("waterbody"))
        gear = normalize_gear(raw.get("gear"))
        weather = normalize_weather(raw.get("weather"))
    except ValueError as error:
        return None, str(error)
    return {
        "date": date,
        "waterbody": waterbody,
        "gear": gear,
        "weather": weather,
    }, None


def main():
    sample = {
        "date": "2024-06-15",
        "waterbody": "Озеро Песчаное",
        "gear": "Поплавок",
        "weather": "Солнечно",
    }
    result, error = validate_trip(sample)
    if error:
        print("Ошибка:", error)
    else:
        print("Данные валидны:", result)


if __name__ == "__main__":
    main()
