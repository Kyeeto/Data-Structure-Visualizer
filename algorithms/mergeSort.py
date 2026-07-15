"""
A Simple Merge Sort implementation. 
"""

def mergeSort(lst):
    steps = []
    arr = lst[:]
    _merge_sort(arr, 0, len(arr) - 1, steps)
    return steps

def _merge_sort(arr, left, right, steps):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(arr, left, mid, steps)
        _merge_sort(arr, mid + 1, right, steps)
        _merge(arr, left, mid, right, steps)

def _merge(arr, left, mid, right, steps):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        steps.append({
            "array": arr[:],
            "highlight": [left + i, mid + 1 + j],
            "action": "compare",
            "pointers": {}
        })
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        steps.append({
            "array": arr[:],
            "highlight": [k],
            "action": "overwrite",
            "pointers": {}
        })
        k += 1

    while i < len(L): 
        arr[k] = L[i]
        steps.append({
            "array": arr[:],
            "highlight": [k],
            "action": "overwrite",
            "pointers": {}
        })
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        steps.append({
            "array": arr[:],
            "highlight": [k],
            "action": "overwrite",
            "pointers": {}
        })
        j += 1
        k += 1