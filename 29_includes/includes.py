def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # if isinstance(collection, dict):
    #     # return sought in collection.values()
    #     if sought in collection:
    #         return True
    # elif isinstance(collection, set):
    #     if sought in collection:
    #         return True
    # elif sought in collection:
    #     return True
    # if start:
    #     collection_slice = collection[start::]
    #     if sought in collection_slice:
    #         return True
    # else:
    #     return False

    # if isinstance(collection, dict):
    #     return sought in collection.values()

    # if start is None or isinstance(collection, set):
    #     return sought in collection

    # return sought in collection[start:]

    if isinstance(collection, dict):
        if sought in collection.values():
            return True
    elif isinstance(collection, (list, set, str, tuple)):
        if start is not None:
            if sought in collection[start:]:
                return True
        else:
            if sought in collection:
                return True
    return False
