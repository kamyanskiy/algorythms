import time
n = 1000000
a = list(range(n+1))
a[1] = 0
lst = []

i = 2
start = time.clock()
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
# print(lst)
res = time.clock() - start
print(res)

# 1M
# (interesting) E:\homework\interesting>python mult.py
# 0.9760805424562674
# 10M
# (interesting) E:\homework\interesting>python mult.py
# 10.998157957504526
# 100M
# MemoryError