# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:54:37 2024

@author: ACER
"""

def kiemtra():
    while True:
        a = float(input("Nhập giá trị (trong khoảng [-89, 90]): "))
        if -89 <= a <= 90:
            print("hợp lệ:", a)
            break
        else:
            print(" không hợp lệ, vui lòng nhập lại.")
kiemtra()