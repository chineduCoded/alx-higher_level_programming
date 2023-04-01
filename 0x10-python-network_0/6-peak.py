#!/usr/bin/python3
""" Function find_peak """


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers using binary search"""

    if list_of_integers is None or list_of_integers == []:
        return None

    start = 0
    end = len(list_of_integers) - 1
    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return list_of_integers[start]
