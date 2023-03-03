# NAMA : MUTHMAINNAH AISYAH
# NIM : 2209116001
# KELAS = A-22

import random
import os
os.system("cls")

# MERGE SORT
list_merge = []
for i in range(10):
    x = random.randrange(1, 50)
    list_merge.append(x)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

print("="*40)
print("MERGE SORT\n")
print("List belum terurut:")
print(list_merge)
print("List sudah terurut:")
print(mergeSort(list_merge))
print("="*40)
