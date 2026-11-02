# === Stage 1: Каркас модуля ===
# Project: FishCatch
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Trip:
    date: date
    body_of_water: str
    tackle: str
    weather: str


def create_demo_trips() -> list[Trip]:
    return [
        Trip(date(2024, 5, 15), "озеро Светлое", "фидер", "солнечно"),
        Trip(date(2024, 5, 16), "река Волга", "поп-up", "пасмурно"),
        Trip(date(2024, 5, 17), "пруд у леса", "мак-спиннинг", "дождь"),
        Trip(date(2024, 5, 18), "озеро Светлое", "дальний крючок", "солнечно"),
    ]


def main() -> None:
    trips = create_demo_trips()
    print("FishCatch: дневник рыбалки")
    print(f"Демо-записей: {len(trips)}")
    for trip in trips:
        print(f"  {trip.date} | {trip.body_of_water} | {trip.tackle} | {trip.weather}")


if __name__ == "__main__":
    main()
