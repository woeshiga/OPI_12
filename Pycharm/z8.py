#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа показывает работу декоратора, который производит оптимизацию
# хвостового вызова. Он делает это, вызывая исключение, если оно является его
# прародителем, и перехватывает исключения, чтобы вызвать стек.

import sys
import timeit


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    Эта программа показывает работу декоратора, который производит оптимизацию
    хвостового вызова. Он делает это, вызывая исключение, если оно является его
    прародителем, и перехватывает исключения, чтобы подделать оптимизацию хвоста.
    Эта функция не работает, если функция декоратора не использует хвостовой вызов.
    """
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, n*acc)


@tail_call_optimized
def factorial_o(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


def fib(i, current=0, next=1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)


@tail_call_optimized
def fib_o(i, current=0, next=1):
    if i == 0:
        return current
    else:
        return fib_o(i - 1, next, current + next)


code_1 = """
from __main__ import factorial
n = 100
"""

code_2 = """
from __main__ import factorial_o
n = 100
"""

code_3 = """
from __main__ import fib
n = 10
"""

code_4 = """
from __main__ import fib_o
n = 10
"""

if __name__ == '__main__':
    print("Рекурсивная функция (factorial):")
    print(timeit.timeit(setup=code_1, stmt="factorial(n)", number=10000))
    print("Рекурсивная функция c @tail_call_optimized(factorial):")
    print(timeit.timeit(setup=code_2, stmt="factorial_o(n)", number=10000))
    print("Рекурсивная функция (fib):")
    print(timeit.timeit(setup=code_3, stmt="fib(n)", number=10000))
    print("Рекурсивная функция c @tail_call_optimized (fib):")
    print(timeit.timeit(setup=code_4, stmt="fib_o(n)", number=10000))
