#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_s(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_s(n - 1)


def factorial_i(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


code_1 = """
from __main__ import factorial
n = 12
"""

code_2 = """
from __main__ import factorial_s
n = 12
"""

code_3 = """
from __main__ import factorial_i
n = 12
"""

if __name__ == "__main__":
    print("Рекурсивная функция с lru_cache: ")
    print(timeit.timeit(setup=code_1, stmt="factorial(n)", number=10000))
    print("Рекурсивная функция: ")
    print(timeit.timeit(setup=code_2, stmt="factorial_s(n)", number=10000))
    print("Итеративная функция: ")
    print(timeit.timeit(setup=code_3, stmt="factorial_i(n)", number=10000))
    