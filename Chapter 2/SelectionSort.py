def smalles_index(arr: list) -> int:
    
    small_val = arr[0]
    small_ind = 0
    
    for i in range(len(arr)):
        if arr[i] < small_val:
            small_val = arr[i]
            small_ind = i
    
    return small_ind


def selection_sort(arr: list) -> list:
    
    sorted_arr = []
    
    for _ in range(len(arr)):
        val = smalles_index(arr)
        sorted_arr.append(arr.pop(val))
    
    return sorted_arr
