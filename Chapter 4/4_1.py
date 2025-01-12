def reucrsion_list_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + reucrsion_list_sum(arr[1:])
    
def recursion_list_cnt(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + recursion_list_cnt(arr[1:])
    
def recursion_list_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], recursion_list_max(arr[1:]))

print(recursion_list_max([2,3,55,5,6]))

def binse(arr, t):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # base case
        if arr[mid] == t:
            return mid
        
        # recursion-like
        if arr[left] < t:
            left += 1
        else:
            right -= 1
        
    return -1

print(binse([2,3,4,8,10,55,2154, 215125], 10))