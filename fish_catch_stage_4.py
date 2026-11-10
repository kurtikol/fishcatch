# === Stage 4: Редактирование записей ===
# Project: FishCatch
from datetime import date

ALLOWED_FIELD = ("водаем", "снасть", "погода")

def edit_trip(trips, trip_id, new_data):
    trips = trips.copy()
    for trip in trips:
        if trip["id"] == trip_id:
            for field in ALLOWED_FIELD:
                if field in new_data:
                    trip[field] = new_data[field]
            return trips
    return None
