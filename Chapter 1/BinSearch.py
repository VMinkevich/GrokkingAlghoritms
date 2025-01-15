def binSearch(arr: list, target: int) -> int:
    
    '''Binary search algorithm
    Time complexity: O(logn)
    Space complexity: O(1)
    input: list, target
    output: int'''
    
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
