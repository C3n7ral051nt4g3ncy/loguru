def filter_none(record):
    return record["name"] is not None


def filter_by_name(record, parent, length):
    name = record["name"]
    return False if name is None else f"{name}."[:length] == parent


def filter_by_level(record, level_per_module):
    name = record["name"]

    while True:
        level = level_per_module.get(name, None)
        if level is False:
            return False
        if level is not None:
            return record["level"].no >= level
        if not name:
            return True
        index = name.rfind(".")
        name = name[:index] if index != -1 else ""
