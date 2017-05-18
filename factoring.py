# coding=utf-8
from functools import reduce
from math import sqrt


class CalculatePrimeNumbersSequence(object):
    @staticmethod
    def get_prime_seq(n):
        """
        Оптимизированная реализация Решето Эратосфена (sieve of Eratosthenes) 
        (начинающаяся с квадратов) на псевдокоде
        
        :param n: int number  
        :return: list of prime numbers for 2..n 
        """
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
        return [i for i, v in enumerate(a) if v == True][1:]


class FactorizeNumber(object):
    @staticmethod
    def factorize(num):
        """
        :param num: int number 
        :return:  sorted list of prime numbers, those are factors of num
        Example :
            n = 27
            return [3, 3, 3]
        """
        if num in [2, 3]:
            return [num]
        sqrt_num = round(sqrt(num))
        prime_numbers_short = CalculatePrimeNumbersSequence.get_prime_seq(
            sqrt_num)[1:]
        prime_numbers_long = CalculatePrimeNumbersSequence.get_prime_seq(
            num)[1:]

        simple_multipliers = []
        # перебором делителей
        while True:
            if num == 1:
                break
            if num > prime_numbers_short[-1] and num in prime_numbers_long:
                simple_multipliers.append(int(num))
                break
            for n in prime_numbers_short:
                if num % n == 0:
                    simple_multipliers.append(n)
                    num = num / n

        return sorted(simple_multipliers)

    @staticmethod
    def show_factorized_result(number):
        print("Представление числа на простые множители:")
        print("{0} = {1}".format(str(number), "*".join(
            str(x) for x in FactorizeNumber.factorize(number))))

    @staticmethod
    def factorize_sequence(limit):
        """
        :param limit: int number to calculate sequence 2..N
        :return: generator object with lists of factors for every 2..N 
        """
        return (FactorizeNumber.factorize(x) for x in range(2, limit))

    @staticmethod
    def show_factorized_sequence(limit):
        for lst in FactorizeNumber.factorize_sequence(limit):
            print("{0} = {1}".format(
                str(reduce(lambda x, y: x*y, lst)), "*".join(
                    str(x) for x in lst)))

