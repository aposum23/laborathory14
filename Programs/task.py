#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def func(a, b):
    def func2():
        res = math.sqrt(a**2 + b**2)
        res = f'Для значений {a}, {b} функция f({a}, {b}) = {res}'
        return res
    return func2



if __name__ == '__main__':
    a = int(input('a = '))
    b = int(input('b = '))
    print(func(a, b)())
