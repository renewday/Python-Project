#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
    集成方法：bagging
    随着抽样次数的增加，多个相互独立的弱分类器集成在一起也可以得到很好的分类效果
"""
import operator
def c(n, k):
    return reduce(operator.mul, range(n-k+1, n+1)) / reduce(operator.mul, range(1, k+1))


def bagging(n, p):
    s = 0
    for i in range(n / 2 + 1, n + 1):
        s += c(n, i) * p ** i * (1 - p) ** (n - i)
    return s


if __name__ == "__main__":
    for t in range(9, 100, 10):
        print t, '次采样正确率：', bagging(t, 0.6)
