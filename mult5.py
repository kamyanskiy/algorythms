# Решето Аткина
#https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%90%D1%82%D0%BA%D0%B8%D0%BD%D0%B0#.D0.A3.D0.BF.D1.80.D0.BE.D1.89.D1.91.D0.BD.D0.BD.D0.B0.D1.8F_.D0.B2.D0.B5.D1.80.D1.81.D0.B8.D1.8F_.D0.B0.D0.BB.D0.B3.D0.BE.D1.80.D0.B8.D1.82.D0.BC.D0.B0

import time
from math import sqrt


limit = 100000000
# Инициализация решета
is_prime = [False] * (limit + 1)
sqr_lim = int(sqrt(limit)) + 1
is_prime[2] = True
is_prime[3] = True

# Предположительно простые — это целые с нечётным числом
# представлений в данных квадратных формах.
# x2 и y2 — это квадраты i и j (оптимизация).
start = time.clock()
x2 = 0;
for i in range(1, sqr_lim): 
    x2 += 2 * i - 1
    y2 = 0
    for j in range(1, sqr_lim):
        y2 += 2 * j - 1
        n = 4 * x2 + y2
        if ((n <= limit) and (n % 12 == 1 or n % 12 == 5)):
            is_prime[n] = not is_prime[n];
        
        # n = 3 * x2 + y2; 
        n -= x2 # Оптимизация
        if ((n <= limit) and (n % 12 == 7)):
            is_prime[n] = not is_prime[n]
        
        # n = 3 * x2 - y2;
        n -= 2 * y2 # Оптимизация
        if ((i > j) and (n <= limit) and (n % 12 == 11)):
            is_prime[n] = not is_prime[n]

# Отсеиваем кратные квадратам простых чисел в интервале [5, sqrt(limit)].
# (основной этап не может их отсеять)
for i in range(5, sqr_lim):
    if (is_prime[i]):
        n = i * i
        for j in range(n, limit,n):
            is_prime[j] = False

# Вывод списка простых чисел в консоль.
# добавлена проверка делимости на 3 и 5. В оригинальной версии алгоритма потребности в ней нет.
prime_num = [2, 3, 5]
for i in range(6, limit):
    if ((is_prime[i]) and (i % 3 != 0) and (i % 5 !=  0)):
        prime_num.append(i)
res = time.clock() - start
print(res)
#print(prime_num)

# 1M
# (interesting) E:\homework\interesting>python mult5.py
# 1.7834912432165255
# 10M
# (interesting) E:\homework\interesting>python mult5.py
# 18.5402480332594
# 100M
# (interesting) E:\homework\interesting>python mult5.py
# 199.73071941468453