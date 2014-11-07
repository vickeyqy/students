#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fact(h):
    if h==1:
        return 1
    else:
        return h*fact(h-1)

a =fact(5)
print a
