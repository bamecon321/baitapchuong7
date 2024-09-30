# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:55:12 2024

@author: ACER
"""

a = int(input("Nhập một số: "))
def kiem_tra_so(n):
    if a < 0 and a % 2 != 0:
        return -1
    elif a > 0 and a % 2 == 0:
        return 1
    else:
        return 0
b = kiem_tra_so(a)
print("Kết quả:", b)