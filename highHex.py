#!/usr/bin/env python
# -*- coding: utf-8 -*-
##dict 的迭代
def h(**KW):
    for k,v in KW.iteritems():
        print k,':',v
#kw = {'a':1,'b':2}
#h(**kw)

##list 里的turpe的迭代

def h(*args):
    L =[]
    for k in args:
       # print k
        for x in k:
            L.append(x)
    print L

args = [(1, 1), (2, 4), (3, 9)]
def s(*args):
    L = []
    for k,v in args:
       for c in (k,v):
            L.append(c)
    print L

s(*args)
