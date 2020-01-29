#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:23:56 2017

@author: Ola
"""

#assume citations is a list of a PIs citations.
def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    cnt = [0] * (len(citations)+1)
    for c in citations:
        if c>= len(citations):
            cnt[-1] += 1
        else:
            cnt[c] += 1
        
    total = 0
    for i in xrange(len(cnt)-1, -1, -1):
        print(i)
        total += cnt[i]
        if total >= i:
            return i
