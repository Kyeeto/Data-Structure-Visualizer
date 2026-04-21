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
                "comparing" : [j, j + 1], 
                "swapped" : False
            })
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                steps.append({
                "array" : arr[:],
                "comparing" : [j, j + 1], 
                "swapped" : True
            })
                
    return steps 