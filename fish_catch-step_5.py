# === Stage 5: Удаление и восстановление ===
# Project: FishCatch
class Trip:
    def __init__(self, trip_id, date, waterbody, gear, weather):
        self.trip_id = trip_id
        self.date = date
        self.waterbody = waterbody
        self.gear = gear
        self.weather = weather
        self.deleted = False
        self.deleted_at = None

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = _now()

    def restore(self):
        if not self.deleted:
            return False
        self.deleted = False
        self.deleted_at = None
        return True

    def is_deleted(self):
        return self.deleted

    def display(self):
        status = "удалён" if self.deleted else "активен"
        return (
            f"Выезд #{self.trip_id} [{status}]"
            f"\n  Дата: {self.date}"
            f"\n  Водоём: {self.waterbody}"
            f"\n  Снасть: {self.gear}"
            f"\n  Погода: {self.weather}"
        )


class TripRepository:
    def __init__(self):
        self._trips = {}

    def add(self, trip):
        self._trips[trip.trip_id] = trip
        return trip

    def get(self, trip_id):
        return self._trips.get(trip_id)

    def list_active(self):
        return [t for t in self._trips.values() if not t.is_deleted()]

    def list_deleted(self):
        return [t for t in self._trips.values() if t.is_deleted()]

    def soft_delete(self, trip_id):
        trip = self.get(trip_id)
        if trip is None:
            return False
        trip.soft_delete()
        return True

    def restore(self, trip_id):
        trip = self.get(trip_id)
        if trip is None:
            return False
        return trip.restore()

    def remove_permanent(self, trip_id):
        trip = self.get(trip_id)
        if trip is None:
            return False
        del self._trips[trip_id]
        return True


def _now():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
