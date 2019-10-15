from typing import List

def select_k(arr: List, k: int):
    """
    Function of selecting k-th element of array
    Parameters
    ----------
        arr:    list, input array
        k:      int, index number in sorted array
        
    Examples
    --------
        >>> arr = [1, 9, 2, 8, 3, 7, 4, 6, 5]
        >>> select_k(arr, 1)
        2
        >>> select_k(arr, -1)
        9
        >>> select_k(arr, 5) == sorted(arr)[5]
        True

    Complexity
    --------
         O(n) in average. O(n^2) in worst-case
    """
    k = len(arr) + k if k < 0 else k

    assert 0 <= k < len(arr) 

    if len(arr) == 1:
        return arr[k]
    else:
        pivot = arr[len(arr)//2]
        left, right, pivots = split_array(arr, pivot)
        if k < len(left):
            return select_k(left, k)
        elif k < len(left) + len(pivots):
            return pivot
        else:
            return select_k(right, k - len(left) - len(pivots))


def split_array(arr: List, pivot: int):
    """
    Function of split array into three, where each element
    larger, smaller or equal to the pivot
    Parameters
    ----------
        arr:    list, input array
        pivot:  int, boundary value

    Complexity
    --------
         O(n). One pass on the list
    """
    left, right, pivots = [], [], []
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            pivots.append(element)
    return left, right, pivots


def select_median(arr: List):
    """
    Function of selecting median of array
    Parameters
    ----------
        arr:    list, input array
        
    Examples
    --------
        >>> arr = [1, 9, 2, 8, 3, 7, 4, 6, 5]
        >>> select_median(arr)
        5
        >>> arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
        >>> select_median(arr)
        4.5

    Complexity
    --------
         O(n) in average. O(n^2) in worst-case
    """
    if len(arr) % 2 == 1:
        return select_k(arr, len(arr) // 2)
    else:
        return (select_k(arr, len(arr) // 2 - 1) +
                select_k(arr, len(arr) // 2 )) / 2
