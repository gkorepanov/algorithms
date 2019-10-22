from merge_sort import merge
from typing import List


def merge_sort(arr: List):
    """
    Sort input array using merge sort algorithm w/o recursion
    """

    # copy input array
    arr = arr[:]

    # Start from chunk of 2 and increase twice on each loop iteration
    chunk_size = 2

    while chunk_size // 2 < len(arr):
        half_chunk_size = chunk_size // 2

        # split array into chunks and sort each chunk
        for i in range(0, len(arr), chunk_size):
            print(i, i + chunk_size)
            left = arr[i : i+half_chunk_size]
            right = arr[i+half_chunk_size : i+chunk_size]
            arr[i:i+chunk_size] = merge(left, right)

        chunk_size *= 2

    return arr

