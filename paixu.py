#!/usr/bin/env python
# -*- coding: utf-8 -*-
def bubble_sort (seq):
    for  i in range(len(seq)):
        for j in range(i,len(seq)):
            if seq[j] < seq[i]:
                tmp = seq[j]
                seq[j] = seq[i]
                seq[i] =tmp

def select_sort (seq):
    for i in range(len(seq)):
        pos = i
        for j in range(i,len(seq)):
            if seq[pos]  > seq[j]:
                pos = j
        if pos !=i:
            tmp = seq[pos]
            seq[pos] = seq[i]
            seq[i] = tmp
def insert_sort(seq):

if __name__ =="__main__":
    list1 = [30,15,25]
    select_sort(list1)
    print list1
