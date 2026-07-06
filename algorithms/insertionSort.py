"""
A Simple Insertion Sort implementation. 
"""

def insertionSort(lst):
    steps = []
    arr = lst[:]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        steps.append({
                "array" : arr[:],
                "highlight" : [j],
                "action" : "compare", 
                "pointers" : {"key" : i}
            })
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            steps.append({
                "array" : arr[:],
                "highlight" : [j, j + 1],
                "action" : "overwrite",
                "pointers" : {"key" : i}
            })
            j -= 1
        arr[j + 1] = key
        steps.append({
                "array" : arr[:],
                "highlight" : [j + 1],
                "action" : "overwrite", 
                "pointers" : {"key" : j + 1}
            })
        
    return steps