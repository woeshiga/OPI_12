#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib_s(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_s(n - 2) + fib_s(n - 1)


def fib_i(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


code_1 = """
from __main__ import fib
n = 12
"""

code_2 = """
from __main__ import fib_s
n = 12
"""

code_3 = """
from __main__ import fib_i
n = 12
"""

if __name__ == "__main__":
    print("Рекурсивная функция с lru_cache: ")
    print(timeit.timeit(setup=code_1, stmt="fib(n)", number=10000))
    print("Рекурсивная функция: ")
    print(timeit.timeit(setup=code_2, stmt="fib_s(n)", number=10000))
    print("Итеративная функция: ")
    print(timeit.timeit(setup=code_3, stmt="fib_i(n)", number=10000))
