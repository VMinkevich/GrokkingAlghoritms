# toDo: function is not working properly, need to fix it
def maximumCount(nums: list) -> int:
    
    left = 0
    right = len(nums) - 1
    neg, pos = 0, 0

    while left <= right:


        if nums[left] != 0:
            if nums[left] < 0:
                neg += 1
            else:
                pos += 1
            left += 1
        else:
            continue

        if nums[right] != 0:
            if nums[right] > 0:
                pos += 1
            else:
                neg += 1
            right -= 1
        else:
            continue
    
    return max(neg, pos)

if __name__ == '__main__':
    print(maximumCount([-1, 3, 5, 7, 10]))