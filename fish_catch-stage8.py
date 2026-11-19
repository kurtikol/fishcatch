# === Stage 8: Генерация идентификаторов ===
# Project: FishCatch
PROJECT_FISHCATCH = "FishCatch"
PREFIX = "fc_"


def generate_unique_id(prefix=PREFIX, counter=None):
    """Генерирует уникальный идентификатор с префиксом проекта.

    Если counter равен None, используется случайный числовой суффикс.
    Иначе генерируется последовательный идентификатор.
    """
    if counter is None:
        suffix = "".join(str(random.randint(0, 9)) for _ in range(8))
    else:
        suffix = str(counter)
    return f"{prefix}{suffix}"


def check_collision(existing_ids, new_id):
    """Проверяет, существует ли переданный идентификатор в списке."""
    return new_id in existing_ids


def make_unique_id(prefix=PREFIX, counter=None, existing_ids=None):
    """Генерирует уникальный идентификатор, не конфликтующий с существующими.

    existing_ids - список уже существующих идентификаторов для проверки
    коллизий. Если не передан, используется пустой список.
    """
    if existing_ids is None:
        existing_ids = []
    new_id = generate_unique_id(prefix, counter)
    if check_collision(existing_ids, new_id):
        new_id = make_unique_id(prefix, counter, existing_ids)
    return new_id


def assign_id(existing_ids=None):
    """Присваивает уникальный идентификатор и добавляет его в список."""
    if existing_ids is None:
        existing_ids = []
    new_id = make_unique_id(existing_ids=existing_ids)
    existing_ids.append(new_id)
    return new_id


if __name__ == "__main__":
    ids = []
    id1 = assign_id(ids)
    id2 = assign_id(ids)
    id3 = assign_id(ids)
    print(f"Сгенерированные ID: {id1}, {id2}, {id3}")
    print(f"Все уникальны: {len(set(ids)) == len(ids)}")
