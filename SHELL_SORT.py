# NAMA : MUTHMAINNAH AISYAH
# NIM : 2209116001
# KELAS = A-22

import random
import os
os.system("cls")

# SHELL SORT
list_shell = []
for i in range(10):
    x = random.randrange(1, 30)
    list_shell.append(x)

def shellSort(list_shell):
    a = len(list_shell)
    h = a // 2
    while h > 0:
        for i in range(h, a):
            t = list_shell[i]
            j = i
            while j >= h and list_shell[j - h] > t:
                list_shell[j] = list_shell[j - h]
                j -= h
            list_shell[j] = t
        h //= 2
    return list_shell

print("="*40)
print("SHELL SORT\n")
print("List belum terurut:")
print(list_shell)
print("List sudah terurut:")
print(shellSort(list_shell))
print("="*40)
