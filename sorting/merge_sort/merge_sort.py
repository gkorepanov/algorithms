from typing import List

def merge(left: List, right: List):
    """
    Merge two sorted arrays into one
    Parameters
    ----------
        left:   list
        right:  list
    """
    i = j = 0
    arr = []
    while (i < len(left)) and  (j < len(right)):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    return arr + left[i:] + right[j:]
    

def merge_sort(arr: List):
    """
    Function of array sorting using merge-sort algorithm
    Parameters
    ----------
        arr:    list, input array
    Examples
    --------
        >>> arr = [1, 9, 2, 8, 3, 7, 4, 6, 5]
        >>> merge_sort(arr)
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(arr) > 1:
        m = len(arr) // 2
        left = merge_sort(arr[:m])
        right = merge_sort(arr[m:])
        arr = merge(left, right)    
    return arr
    