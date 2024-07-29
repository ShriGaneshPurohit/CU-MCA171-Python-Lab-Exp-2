# Additionally, create lists using Python comprehension for various scenarios and demonstrate
# the use of the module functions with these lists.
# (b) Create another script named ‘main_ListOpeartions.py’ and Imports the
# ‘module_ListFunction’ to it.
# (c) Demonstrate the execution of each function with suitable examples.

# main_ListOperations.py

from module_ListFunction import module_ListFunction

if __name__ == "__main__":
    # Various lists using list comprehensions
    list1 = [x for x in range(1, 11)]
    list2 = [x**2 for x in range(1, 11)]
    list3 = [x for x in range(10, 0, -1)]
    list4 = [x for x in range(1, 21) if x % 2 == 0]
    list5 = [x for x in range(1, 21) if x % 2 != 0]

    functionModule1 = module_ListFunction(list1)
    functionModule2 = module_ListFunction(list2)
    functionModule3 = module_ListFunction(list3)

    print(f"List1: {list1}")
    print(f"Max element: {functionModule1.maxElement()}")
    print(f"Min element: {functionModule1.minElement()}")
    print(f"Sum of elements: {functionModule1.sumOfElements()}")
    print(f"Average of elements: {functionModule1.avgOfElements()}")
    print(f"Median of elements: {functionModule1.medianOfElements()}")

    print(f"\nList2: {list2}")
    print(f"Max element: {functionModule2.maxElement()}")
    print(f"Min element: {functionModule2.minElement()}")
    print(f"Sum of elements: {functionModule2.sumOfElements()}")
    print(f"Average of elements: {functionModule2.avgOfElements()}")
    print(f"Median of elements: {functionModule2.medianOfElements()}")

    print(f"\nList3: {list3}")
    print(f"Max element: {functionModule3.maxElement()}")
    print(f"Min element: {functionModule3.minElement()}")
    print(f"Sum of elements: {functionModule3.sumOfElements()}")
    print(f"Average of elements: {functionModule3.avgOfElements()}")
    print(f"Median of elements: {functionModule3.medianOfElements()}")