# === Stage 11: Поиск по нескольким словам ===
# Project: FishCatch
def search_trips(trips, terms):
    """Поиск выездов по нескольким словам с поддержкой исключений через префикс '-'.

    Args:
        trips: список словарей (выездов), каждый содержит поля:
            date, body_of_water, tackle, weather.
        terms: список строк. Термин с префиксом '-' исключает выезды,
            в которых встречается этот термин (по любому из полей).

    Returns:
        список выездов, соответствующих всем условиям.
    """
    if not terms:
        return list(trips)

    positive_terms = [t for t in terms if not t.startswith('-')]
    negative_terms = [t[1:] for t in terms if t.startswith('-')]

    def contains(term, trip):
        haystack = ' '.join(str(trip.get(field, '')) for field in
                            ('date', 'body_of_water', 'tackle', 'weather')).lower()
        return term.lower() in haystack

    result = []
    for trip in trips:
        if any(contains(term, trip) for term in negative_terms):
            continue
        if positive_terms and not all(contains(term, trip) for term in positive_terms):
            continue
        result.append(trip)
    return result


def main():
    sample_trips = [
        {'date': '2024-06-01', 'body_of_water': 'озеро Пятух', 'tackle': 'фидер', 'weather': 'солнечно'},
        {'date': '2024-06-02', 'body_of_water': 'река Волга', 'tackle': 'поплавочная удочка', 'weather': 'пасмурно'},
        {'date': '2024-06-03', 'body_of_water': 'озеро Пятух', 'tackle': 'спиннинг', 'weather': 'дождливо'},
        {'date': '2024-06-04', 'body_of_water': 'река Ока', 'tackle': 'фидер', 'weather': 'солнечно'},
    ]

    print(search_trips(sample_trips, ['озеро']))
    print(search_trips(sample_trips, ['-река']))
    print(search_trips(sample_trips, ['фидер', '-дождливо']))


if __name__ == '__main__':
    main()
