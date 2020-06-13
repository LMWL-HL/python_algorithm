#!/usr/bin/env python
# coding=utf-8

def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]

def bubbleSort(lyst):
    """
    My Solution.
    """
    for i in range(len(lyst)-2):
        for j in range(len(lyst)-1-i):
            if lyst[j] > lyst[j+1]:
                swap(lyst, j, j+1)

def bubbleSort_example(lyst):
    """
    Example in book.
    """
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i-1)
            i += 1
        n -= 1


if __name__ == "__main__":
    lyst = [5, 3, 1, 2, 4]
    bubbleSort(lyst)
    print("My Solutiom:", lyst)
    lyst = [5, 3, 1, 2, 4]
    bubbleSort_example(lyst)
    print("Example in book:", lyst)
