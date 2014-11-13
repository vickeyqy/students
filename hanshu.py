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

if  __name__ == "__main__":
    list1=[1,2,3,4,5,6,7,8,9,10]
    list2 = listnum(1000)
    mymap(*list1)
    prod(*list2)



