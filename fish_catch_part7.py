# === Stage 7: Связи между сущностями ===
# Project: FishCatch
from datetime import date


class FishTrip:
    def __init__(self, trip_id, date, body_of_water, gear, weather):
        self.trip_id = trip_id
        self.date = date
        self.body_of_water = body_of_water
        self.gear = gear
        self.weather = weather
        self.catches = []


class Catch:
    def __init__(self, catch_id, trip_id, species, weight):
        self.catch_id = catch_id
        self.trip_id = trip_id
        self.species = species
        self.weight = weight


class CatchBookRepository:
    def __init__(self, trips=None, catches=None):
        self.trips = trips if trips is not None else []
        self.catches = catches if catches is not None else []

    def add_trip(self, trip):
        self.trips.append(trip)

    def add_catch(self, catch):
        self.catches.append(catch)

    def get_trips_by_date(self, target_date):
        result = []
        for trip in self.trips:
            if trip.date == target_date:
                result.append(trip)
        return result

    def get_catches_by_trip(self, trip):
        result = []
        for catch in self.catches:
            if catch.trip_id == trip.trip_id:
                result.append(catch)
        return result


def get_catches_for_trip(repository, trip):
    return repository.get_catches_by_trip(trip)


def verify_integrity(repository, trip):
    catches = repository.get_catches_by_trip(trip)
    expected_count = len(catches)
    for catch in catches:
        if catch.trip_id != trip.trip_id:
            raise ValueError(
                f"Целостность нарушена: улов {catch.catch_id} "
                f"принадлежит выезду {catch.trip_id}, "
                f"а не {trip.trip_id}"
            )
    return len(catches), expected_count


if __name__ == "__main__":
    repo = CatchBookRepository()
    trip = FishTrip(
        trip_id=1,
        date=date(2024, 6, 15),
        body_of_water="озеро",
        gear="спиннинг",
        weather="солнечно",
    )
    repo.add_trip(trip)
    repo.add_catch(Catch(1, 1, "окунь", 0.5))
    repo.add_catch(Catch(2, 1, "плотва", 0.3))

    catches = get_catches_for_trip(repo, trip)
    print(f"Уловов: {len(catches)}")
    for catch in catches:
        print(f"  {catch.species}: {catch.weight}")

    count, expected = verify_integrity(repo, trip)
    print(f"Целостность: {count} == {expected}")
