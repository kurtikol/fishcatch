# === Stage 3: Хранилище в памяти ===
# Project: FishCatch
from datetime import date


class Trip:
    def __init__(self, trip_id, trip_date, water_body, gear, weather):
        self.trip_id = trip_id
        self.trip_date = trip_date
        self.water_body = water_body
        self.gear = gear
        self.weather = weather

    def __repr__(self):
        return (
            f"Trip(id={self.trip_id}, date={self.trip_date}, "
            f"water_body={self.water_body!r}, gear={self.gear!r}, "
            f"weather={self.weather!r})"
        )


class TripStore:
    def __init__(self):
        self._trips = {}

    def add(self, trip):
        if trip.trip_id in self._trips:
            raise ValueError(f"Trip with id {trip.trip_id} already exists")
        self._trips[trip.trip_id] = trip
        return trip

    def get(self, trip_id):
        return self._trips.get(trip_id)

    def list_all(self):
        return list(self._trips.values())

    def count(self):
        return len(self._trips)


if __name__ == "__main__":
    store = TripStore()

    store.add(Trip(1, date(2024, 5, 10), "озеро Вишнёвое", "фидер", "солнечно"))
    store.add(Trip(2, date(2024, 5, 15), "река Волга", "поплавок", "облачно"))

    print("Всего выездов:", store.count())

    print(store.get(1))

    for trip in store.list_all():
        print(trip)

    print("Удалённый:", store.get(2))
