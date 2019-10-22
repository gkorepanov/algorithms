def run_test_cases(merge_sort):
    assert merge_sort([1, 4, 5, 9, 12, 0, -4, 2, 1]) == [-4, 0, 1, 1, 2, 4, 5, 9, 12]
    assert merge_sort([0]) == [0]
    assert merge_sort([-1, 0]) == [-1, 0]
    assert merge_sort([0, -1]) == [-1, 0]
    assert merge_sort([-1, 0, -1]) == [-1, -1, 0]
    assert merge_sort([]) == []
    assert merge_sort([2]*1000 + [0]*1000) == [0]*1000 + [2]*1000


def test_merge_sort():
    from merge_sort import merge_sort
    run_test_cases(merge_sort)

def test_merge_sort_no_recursion():
    from merge_sort_no_recursion import merge_sort
    run_test_cases(merge_sort)

