"""
A Simple Quick Sort implementation. 
"""

def quickSort(lst):
    steps = []
    arr = lst[:]
    _quick_sort(arr, 0, len(arr) - 1, steps)
    return steps

def _quick_sort(arr, start, end, steps):
    if start >= end:
        return
    p = _partition(arr, start, end, steps)
    _quick_sort(arr, start, p - 1, steps)
    _quick_sort(arr, p + 1, end, steps)

def _partition(arr, start, end, steps):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            steps.append({
                "array": arr[:],
                "highlight": [high],
                "action": "compare",
                "pointers": {"pivot": start}
            })
            high = high - 1

        while low <= high and arr[low] <= pivot:
            steps.append({
                "array": arr[:],
                "highlight": [low],
                "action": "compare",
                "pointers": {"pivot": start}
            })
            low = low + 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            steps.append({
                "array": arr[:],
                "highlight": [low, high],
                "action": "swap",
                "pointers": {"pivot": start}
            })
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]
    steps.append({
        "array": arr[:],
        "highlight": [start, high],
        "action": "swap",
        "pointers": {"pivot": start}
    })
    return high