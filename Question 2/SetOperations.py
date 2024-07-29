# set_operations.py

def add_to_set(s, element):
    s.add(element)
    return s

def remove_from_set(s, element):
    s.discard(element)
    return s

def union_and_intersection(set1, set2):
    return set1.union(set2), set1.intersection(set2)

def difference(set1, set2):
    return set1.difference(set2)

def is_subset(set1, set2):
    return set1.issubset(set2)

def length_of_set(s):
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

def power_set(s):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def unique_subsets(s):
    from itertools import chain, combinations
    return set(frozenset(combo) for combo in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))