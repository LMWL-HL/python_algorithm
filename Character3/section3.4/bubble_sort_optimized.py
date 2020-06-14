#!/usr/bin/env python
# coding=utf-8

def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]

def bubbleSort(lyst):
    """
    My Solution.
    """
    print("My solution:")
    for i in range(len(lyst)-2):
        swapped = False
        for j in range(len(lyst)-1-i):
            if lyst[j] > lyst[j+1]:
                swap(lyst, j, j+1)
                swapped = True
            print(lyst)
        # print(swapped)
        if not swapped: break

def bubbleSort_example(lyst):
    """
    Example in book.
    """
    print("Example in book:")
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i-1)
                swapped = True
            i += 1
            print(lyst)
        # print(swapped)
        if not swapped: return
        n -= 1


if __name__ == "__main__":
    lyst = [5, 3, 1, 2, 4, 10]
    print("origin:", lyst, "\n")
    bubbleSort(lyst)
    print("\n")
    # print("My Solutiom:", lyst)
    lyst = [5, 3, 1, 2, 4, 10]
    bubbleSort_example(lyst)
    print("\b")
    # print("Example in book:", lyst)
