#!/usr/bin/env python
# -*- coding: utf-8 -*-
def bubble_sort (seq):
    for  i in range(len(seq)):
        for j in range(i,len(seq)):
            if seq[j] < seq[i]:
                tmp = seq[j]
                seq[j] = seq[i]
                seq[i] =tmp
