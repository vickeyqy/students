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
    return  L
arg = (1,2,3,4,5,6)
S= h(arg)
S.append('7')
print S
args = [(1, 1), (2, 4), (3, 9)]
def s(*args):
    L = []
    for k,v in args:
       for c in (k,v):
            L.append(c)
    print L
#列表生成式
T= ['Hello', 'World', 'Apple']
s = [h.lower() for h in T ]
#print s
def o(*args):
    L = []
    for  b in T:
        if isinstance(b,str):
            c = b.lower()
            L.append(c)
        else:
            L.append(b)
    print L
def y(*args):
    L = [c for x,v in args]
    print L

#生成器 斐波那契
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n=n+1

for n in fib(6):
    print n
