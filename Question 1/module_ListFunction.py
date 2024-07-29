# 1. (a) Develop a module called module_ListFunction that includes the following functions:
# i. A function to find the maximum value in a given list.
# ii. A function to find the minimum value in a given list.
# iii. A function to calculate the sum of all elements in a list.
# iv. A function to compute the average of the list.
# v. A function to determine the median of a list.

class module_ListFunction():
    def __init__(self, arraylist) -> None:
        self.arrayList = arraylist

    # Maximum value
    def maxElement(self) -> int:
        maxValue = self.arrayList[0]
        for i in self.arrayList:
            if i > maxValue:
                maxValue = i
        return maxValue

    # Minimum value
    def minElement(self) -> int:
        minValue = self.arrayList[0]
        for i in self.arrayList:
            if i < minValue:
                minValue = i
        return minValue

    # Sum of elements
    def sumOfElements(self) -> int:
        sum = 0
        for i in self.arrayList:
            sum += i
        return sum

    # Average of elements
    def avgOfElements(self) -> float:
        sum = 0
        for i in self.arrayList:
            sum += i
        return sum / len(self.arrayList)

    # Median of elements
    def medianOfElements(self) -> float:
        sortedArray = sorted(self.arrayList)
        n = len(sortedArray)
        if n % 2 == 0:
            median = (sortedArray[n//2 - 1] + sortedArray[n//2]) / 2
        else:
            median = sortedArray[n//2]
        return median
