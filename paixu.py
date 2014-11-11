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
    for i  in range(len(seq)):
        position = i
        for j in range(i,len(seq)):
            if seq[position] > seq[j]:
                position = j
        if position != i:
            tmp = seq[position]
            seq[position] = seq[i]
            seq[i]= tmp


seq1 = [30,15,25]
select_sort(seq1)
print seq1


