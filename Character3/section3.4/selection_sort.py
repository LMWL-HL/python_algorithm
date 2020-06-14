#!/usr/bin/env python
# coding=utf-8

def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]

def selectionSort(lyst):
    """
    My solution.
    """
    print("My solution:")
    for i in range(len(lyst)):
        for j in range(i+1, len(lyst)):
            if lyst[i] > lyst[j]:
                swap(lyst, i, j)
        print(lyst)

def selectionSort_example(lyst):
    """
    Example in book.
    """
    print("Example in book:")
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        print(lyst)
        i += 1

if __name__ == "__main__":
    lyst = [5, 3, 1, 2, 4]
    print("origin:", lyst, "\n")
    selectionSort(lyst)
    print("\n")
    # print("My solution:", lyst)
    lyst = [5, 3, 1, 2, 4]
    selectionSort_example(lyst)
    # print("Example in book:", lyst)

