#!/usr/bin/env python
# -*- coding: utf-8 -*-
def  f(x,y):
    return x * y

def fn(x):
    return x*x

def addfx():
    L=[]
    for i in range(1,10):
        L.append(f(i))
    print L
#map 函数的实现
#map（f，list []）
def mymap(*args):
    L = []
    for i in args:
        L.append(fn(i))
    print L
#递归
def prod(*args):
    print  reduce(f,args)
#将数字变为list
def listnum(num):
    L =[]
    for i in range(1,num):
        L.append(i)
    return L

def fun(a=1, b=None, c=None, *args):
    print('{0},{1},{2},{3}'.format(a, b, c, args))

def dict(**kw):
    L = []
    for k,v in kw.iteritems():
        L.append(k)
        L.append(v)
    return  L

def main():
    L = []
    fun('one','one','one',['one','two'])
    fun('one')

if  __name__ == "__main__":
    D = {'name':'one','age':'25'}
    S = dict(**D)
    S.append('123')
    print S




