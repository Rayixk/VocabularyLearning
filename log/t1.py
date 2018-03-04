# encoding: utf-8
# !/usr/bin/env python
# __author__ = "yang"
# Date: 2017/8/27

80000

80000 + 80000 * 1.1

80000 + (80000 + 80000 * 1.1) * 1.1

rate=1.5
money=200000
def aa(n):
    if n == 1:
        return money
    else:
        return money + aa(n - 1) * rate

s = aa(20)
print(s)
