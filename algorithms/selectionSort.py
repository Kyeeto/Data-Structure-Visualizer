"""
A Simple Selection Sort implementation. 
"""

def selectionSort(lst):
    steps = []
    arr = lst[:]
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps.append({
                "array": arr[:],
                "highlight": [min_index, j], 
                "action": "compare", 
                "pointers": {"min": min_index}
            })
            if arr[min_index] > arr[j]:
                min_index = j

        steps.append({
            "array": arr[:], 
            "highlight": [i, min_index], 
            "action": "swap", 
            "pointers": {"min": min_index}
        })
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return steps