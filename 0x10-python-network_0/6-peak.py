#!/usr/bin/python3
""" Find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ A peak is when an integer is not smaller
        than its neighbor(s)
    Args:
       list_of_integers: unsorted list of intergers
    """
    length = len(list_of_integers)

    if list_of_integers is None or length == 0:
        return None

    start = 0
    end = int(length - 1)

    while start <= end:
        mid = int((start + end) / 2)
        if ((mid == 0 or list_of_integers[mid - 1] <=
            list_of_integers[mid]) and
            (mid == length - 1 or list_of_integers[mid + 1] <=
                list_of_integers[mid])):
            return list_of_integers[mid]
        elif (mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return None
