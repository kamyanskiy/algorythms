# https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%AD%D1%80%D0%B0%D1%82%D0%BE%D1%81%D1%84%D0%B5%D0%BD%D0%B0
# Оптимизированная реализация (начинающаяся с квадратов) на псевдокоде[5][6]:

# Вход: натуральное число n

# Пусть A — булевый массив, индексируемый числами от 2 до n, 
# изначально заполненный значениями true.
#  для i := 2, 3, 4, ..., пока i2 ≤ n:
#   если A[i] = true:
#     для j := i2, i2 + i, i2 + 2i, ..., пока j ≤ n:
#       A[j] := false

# Выход: числа i, для которых A[i] = true.


import time
start = time.clock()

n = 100000000
a = [True] * (n + 1)
i = 2
while i*i <= n:
	if a[i]:
		k = 0
		j = i*i
		while j <= n:
			a[j] = False
			k += 1
			j = i*i + i*k
	i += 1		

simple_numbers = [i for i, v in enumerate(a) if v == True][1:]

#print(simple_numbers)
res = time.clock() - start
print(len(simple_numbers))
print(res)

# 1M
# (interesting) E:\homework\interesting>python mult3.py
# 1.4187237235942776
# 10M
# (interesting) E:\homework\interesting>python mult3.py
# 15.858602404138459
# 100M
# 191.36943235779387