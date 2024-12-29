def binSearch(arr: list, target: int) -> int:
    """Binary search algorithm
    Args:
    arr: list of integers
    target: integer to search for
    """

    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
