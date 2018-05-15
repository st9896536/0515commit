#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:09:06 2018

@author: Rong
"""

num = int(input("input a number:"))
i = 1
ans = []
for i in range(num+1):
    if i % 3 != 0 and i % 5 != 0:
        ans.append(i)
    elif i % 15 == 0:
        ans.append(i)
print(ans)