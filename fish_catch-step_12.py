# === Stage 12: Теги ===
# Project: FishCatch
TAG_FIELD = "tags"


def add_tag(entry, tag):
    entries = entry.get(TAG_FIELD)
    if entries is None:
        entries = []
    if tag not in entries:
        entries.append(tag)
    entry[TAG_FIELD] = entries


def remove_tag(entry, tag):
    entries = entry.get(TAG_FIELD)
    if entries and tag in entries:
        entries.remove(tag)
        if not entries:
            entry.pop(TAG_FIELD, None)


def search_by_tag(entries, tag):
    return [e for e in entries if tag in e.get(TAG_FIELD, [])]
