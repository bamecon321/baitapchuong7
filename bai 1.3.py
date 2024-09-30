# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:52:49 2024

@author: ACER
"""

n=int(input("Nhập số = "))
def chanam(a):
    return a < 0 and a % 2 == 0
print(chanam(n))