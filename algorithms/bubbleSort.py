"""
A Simple Bubble Sort implementation. 
"""

def bubbleSort(lst):
    steps = []
    arr = lst[:]
    n = len(lst)

    for i in range (n-1):
        for j in range(0, n - i - 1):

            steps.append({
                "array" : arr[:],
                "highlight" : [j, j + 1], 
                "action" : "compare"
            })
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append({
                "array" : arr[:],
                "highlight" : [j, j + 1], 
                "action" : "swap"
            })
                
    return steps 