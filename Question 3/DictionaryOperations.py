def merging_Dict(*args):
    merged = {}
    for d in args:
        merged.update(d)
    return merged

def common_keys(*args):
    if not args:
        return set()
    common = set(args[0].keys())
    for d in args[1:]:
        common.intersection_update(d.keys())
    return common

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted

def common_key_value_pairs(*args):
    if not args:
        return set()
    common = set(args[0].items())
    for d in args[1:]:
        common.intersection_update(d.items())
    return common