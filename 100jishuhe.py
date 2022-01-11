#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum():
    sum = 0
    n=99
    while n>0:
        sum = sum+n
        n=n-2
    print (sum)
def bianli():
    list = ['1','2','3','4']
    list.append('5')
    for x in list:
        trup = ('10','20',['30','40'])
    for a in trup:
        for b in trup(3):
            print  (b)
def myabs(x):
    if not isinstance(x,int):
        print ('1111')
    else:
        print ('22222')
def six():
    t = ('1','2','3','4')
    for x in t:
        print (x)

def  add(L=None):
    if L is None:
        L=[]
    L.append('end')
    print (L)


#计算a2+B2+C2--------

def sum(*numbers):
    sum=0
    if not len(numbers):
        for n in numbers:
            sum = sum + n*n
        print (sum)

turpe = [1,2,3,4]

#练习函数调用参数

def fun(a,b,c=0,*agrs,**kw):
    sum =0
    print ('a=',a,'b=',b,'c=',c,',agrs=',agrs,'kw=',kw)
    if agrs:
        for n in agrs:
            sum = sum + n*n
        print (sum)
#递归
def fact(h):
    if h==1:
        return 1
    else:
        return h*fact(h-1)
#s = fact(5)
#print s
#构造1 3 5 7列表

def list(b,**kw):
    L = []
    n=1
    x =0
    if  b :
        while x< b:
            L.append(n)
            n =n+2
            x=x+1
        print (L[0:len(L)/2])
    else:
        while x<kw['E']:
            L.append(n)
            n=n+2
            x=x+1
        print (L)

