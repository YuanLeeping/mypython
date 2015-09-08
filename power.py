#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x):
    if (not isinstance(x, (int, float))):
        raise TypeError('bad openand type')
    return x * x

#print(power('A'))
print(power(13))
