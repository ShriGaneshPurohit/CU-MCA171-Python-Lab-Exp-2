# main_SetOperations.py

import SetOperations as so

if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    print("Initial Sets:")
    print("Set 1:", set1)
    print("Set 2:", set2)

    # Add element to set
    so.add_to_set(set1, 6)
    print("\nAfter adding 6 to Set 1:", set1)

    # Remove element from set
    so.remove_from_set(set2, 7)
    print("\nAfter removing 7 from Set 2:", set2)

    # Union and Intersection
    union, intersection = so.union_and_intersection(set1, set2)
    print("\nUnion of Set 1 and Set 2:", union)
    print("Intersection of Set 1 and Set 2:", intersection)

    # Difference
    difference = so.difference(set1, set2)
    print("\nDifference (Set1 - Set2):", difference)

    # Subset check
    is_subset = so.is_subset({1, 2}, set1)
    print("\nIs {1, 2} a subset of Set 1?:", is_subset)

    # Length of set without using len()
    length = so.length_of_set(set1)
    print("\nLength of Set 1 without using len():", length)

    # Symmetric Difference
    sym_diff = so.symmetric_difference(set1, set2)
    print("\nSymmetric Difference of Set 1 and Set 2:", sym_diff)

    # Power Set
    power_set = so.power_set({1, 2, 3})
    print("\nPower Set of {1, 2, 3}:")
    for subset in power_set:
        print(subset)

    # Unique Subsets
    unique_subsets = so.unique_subsets({1, 2, 3})
    print("\nUnique Subsets of {1, 2, 3}:")
    for subset in unique_subsets:
        print(subset)