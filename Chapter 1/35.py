def searchInsert(nums: list, target: int) -> int:
    
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = left + 1
        else:
            right = right - 1
    
    return left


if __name__ == '__main__':
    print(searchInsert([1,3,5,7,10], 10))