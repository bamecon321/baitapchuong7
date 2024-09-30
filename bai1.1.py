# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:51:21 2024

@author: ACER
"""

def tich_tong(*args, **kwargs):
    a = sum(args)
    b = 1
    for i in args:
        b *= i
    return a, b
c, d = tich_tong(1, 2, 3, 4, 5)
print("tổng:", c)
print("tích:", d)