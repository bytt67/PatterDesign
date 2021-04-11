#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/11 
@Author  : buyun.liang
"""


class Singleton(object):
    def __new__(cls, *args, **kwarg):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls, *args, **kwarg)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)

