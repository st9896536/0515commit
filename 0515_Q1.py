#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:03:27 2018

@author: Rong
"""

s = input("input:")
ans = []
new_list = s.split()
for word in range(len(new_list)):
    #print(new_list[word][::-1])
    ans.append(new_list[word][::-1])

ans_str = ' '.join(ans)
print(ans_str)
    