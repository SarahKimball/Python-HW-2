def includes(collection, sought, start=None):
    if isinstance(collection, dict):
        return sought in collection.values()

    if start is not None:
        collection = collection[start:]

    return sought in collection
