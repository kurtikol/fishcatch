# === Stage 6: Связанная сущность ===
# Project: FishCatch
from datetime import date

class Catch:
    def __init__(self, fish_name, weight, length=None, notes=""):
        self.id = None
        self.fish_name = fish_name
        self.weight = weight
        self.length = length
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.id,
            "fish_name": self.fish_name,
            "weight": self.weight,
            "length": self.length,
            "notes": self.notes,
        }

    def __repr__(self):
        return f"Catch(id={self.id}, fish_name={self.fish_name!r}, weight={self.weight})"


class TripCatches:
    def __init__(self):
        self._catches = []
        self._counter = 0

    def add_catch(self, trip_id, fish_name, weight, length=None, notes=""):
        catch = Catch(fish_name, weight, length, notes)
        self._counter += 1
        catch.id = self._counter
        catch.trip_id = trip_id
        self._catches.append(catch)
        return catch

    def get_catch(self, catch_id):
        for catch in self._catches:
            if catch.id == catch_id:
                return catch
        return None

    def get_catches_by_trip(self, trip_id):
        return [c for c in self._catches if c.trip_id == trip_id]

    def remove_catch(self, catch_id):
        for index, catch in enumerate(self._catches):
            if catch.id == catch_id:
                del self._catches[index]
                return True
        return False

    def total_weight(self, trip_id=None):
        total = sum(c.weight for c in self._catches)
        if trip_id is not None:
            total = sum(
                c.weight for c in self._catches if c.trip_id == trip_id
            )
        return total

    def count_by_species(self):
        stats = {}
        for catch in self._catches:
            stats[catch.fish_name] = stats.get(catch.fish_name, 0) + 1
        return stats
