def QuickSort(arr: list) -> list:

    '''Quick sort algorithm
    Time complexity: O(nlogn)
    Space complexity: O(n)
    input: list
    output: list
    '''
    
    # Base case: if arr is empty or consists 1 elemnt, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Select pivot element
    pivot = arr[-1]
    
    # Разделяем массив на две части: меньшие и большие элементы относительно опорного
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    
    # Рекурсивно сортируем подмассивы и соединяем результат
    return QuickSort(left) + [pivot] + QuickSort(right)
