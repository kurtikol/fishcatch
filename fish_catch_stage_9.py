# === Stage 9: Сортировка записей ===
# Project: FishCatch
def sort_by_date(records, reverse=False):
    return sorted(records, key=lambda r: r.get("date"), reverse=reverse)


def sort_by_created_at(records, reverse=False):
    return sorted(records, key=lambda r: r.get("created_at"), reverse=reverse)


def sort_by_date_and_created(records, reverse=False):
    return sorted(
        records,
        key=lambda r: (r.get("created_at"), r.get("date")),
        reverse=reverse,
    )


def sort_records(records, field="date", reverse=False):
    return sorted(records, key=lambda r: r.get(field), reverse=reverse)
