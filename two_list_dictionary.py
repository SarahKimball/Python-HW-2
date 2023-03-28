def two_list_dictionary(keys, values):
    d = {}
    for i, k in enumerate(keys):
        if i < len(values):
            d[k] = values[i]
        else:
            d[k] = None
    return d
