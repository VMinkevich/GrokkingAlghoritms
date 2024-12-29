def binSerach(arr: list, target: int) -> int:
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

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(binSerach(arr, target))
    target = 20
    print(binSerach(arr, target))
