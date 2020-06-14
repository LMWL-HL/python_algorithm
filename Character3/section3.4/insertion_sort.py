#!/usr/bin/env python
# coding=utf-8

def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]

def insertionSort(lyst):
    """
    My solution.
    """
    print("My solution:")
    for i in range(1, len(lyst)):
        f = lyst[i]
        for j in range(i):
            if lyst[i-j-1] > f:
                swap(lyst, i-j-1, i-j)
            else:
                lyst[i-j] = f
                break
        print(lyst)


def insertionSort_example(lyst):
    """
    Example in book.
    """
    print("Example in book:")
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1
        print(lyst)

if __name__ == "__main__":
    lyst = [5, 3, 1, 2, 4]
    print("origin:", lyst, "\n")
    insertionSort(lyst)
    print("\n")
    # print("My solution:", lyst)
    lyst = [5, 3, 1, 2, 4]
    insertionSort_example(lyst)
    # print("Example in book:", lyst)
