# main_DictOperations.py

import DictionaryOperations as do

if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 2, "c": 4, "d": 5}
    dict3 = {"c": 3, "d": 6, "e": 7}

    print("Initial Dictionaries:")
    print("Dict1:", dict1)
    print("Dict2:", dict2)
    print("Dict3:", dict3)

    # Merging dictionaries
    merged_dict = do.merging_Dict(dict1, dict2, dict3)
    print("\nMerged Dictionary:", merged_dict)

    # Finding common keys
    common_keys = do.common_keys(dict1, dict2, dict3)
    print("\nCommon Keys:", common_keys)

    # Inverting a dictionary
    inverted_dict = do.invert_dict(dict1)
    print("\nInverted Dictionary (Dict1):", inverted_dict)

    # Finding common key-value pairs
    common_kv_pairs = do.common_key_value_pairs(dict1, dict2, dict3)
    print("\nCommon Key-Value Pairs:", common_kv_pairs)