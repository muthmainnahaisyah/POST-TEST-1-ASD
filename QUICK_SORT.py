# NAMA : MUTHMAINNAH AISYAH
# NIM : 2209116001
# KELAS = A-22

import random
import os
os.system("cls")

# QUICK SORT
list_quick = []
for i in range(10):
    x = random.randrange(1, 50)
    list_quick.append(x)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)

print("="*40)
print("QUICK SORT\n")
print("List belum terurut:")
print(list_quick)
print("List sudah terurut:")
print(quickSort(list_quick))
print("="*40)
