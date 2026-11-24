# === Stage 10: Текстовый поиск ===
# Project: FishCatch
import re
from datetime import date


def normalize(text: str) -> str:
    return (text or "").strip().lower()


def build_query(data: list, keywords: list) -> list:
    if not keywords:
        return data

    query = " ".join(normalize(k) for k in keywords)
    if not query:
        return data

    pattern = re.escape(query)
    regex = re.compile(pattern, re.IGNORECASE)

    results = []
    for trip in data:
        fields = {
            "дата": normalize(trip.get("дата", "")),
            "водоём": normalize(trip.get("водоём", "")),
            "снасть": normalize(trip.get("снасть", "")),
            "погода": normalize(trip.get("погода", "")),
        }
        if any(regex.search(value) for value in fields.values()):
            results.append(trip)
    return results


def highlight(text: str, keywords: list) -> str:
    text = text or ""
    if not keywords:
        return text

    query = " ".join(normalize(k) for k in keywords)
    if not query:
        return text

    pattern = re.escape(query)
    regex = re.compile(pattern, re.IGNORECASE)

    def _replace(match):
        return f"<mark>{match.group(0)}</mark>"

    return regex.sub(_replace, text)


def format_trip(trip: dict, keywords: list) -> str:
    if not trip:
        return ""

    date_value = trip.get("дата", "")
    if isinstance(date_value, date):
        date_value = date_value.isoformat()

    parts = [
        ("Дата:", date_value),
        ("Водоём:", trip.get("водоём", "")),
        ("Снасть:", trip.get("снасть", "")),
        ("Погода:", trip.get("погода", "")),
    ]

    lines = [f"{label}: {value}" for label, value in parts]
    lines = [line for line in lines if line]
    body = "\n".join(lines)

    return highlight(body, keywords)


def search_trips(data: list, keywords: list) -> list:
    matches = build_query(data, keywords)
    return [format_trip(trip, keywords) for trip in matches]
