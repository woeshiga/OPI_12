#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def C(m, n):
    if m == n or m == 0:
        return 1
    elif 0 <= m <= n:
        return C(m, n - 1) + C(m - 1, n - 1)


if __name__ == '__main__':
    print(C(int(input()), int(input())))
