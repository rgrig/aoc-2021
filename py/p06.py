#!/usr/bin/env python3

from collections import defaultdict
import sys

start = [int(x) for x in sys.stdin.read().strip().split(',')]

start_cnt = defaultdict(int)
rest_cnt = defaultdict(int)

for x in start:
    start_cnt[x] += 1
for _ in range(256):
    #print('start',sorted(start_cnt.items()))
    #print('rest ',sorted(rest_cnt.items()))
    start_cnt_new = defaultdict(int)
    rest_cnt_new = defaultdict(int)
    for age, cnt in start_cnt.items():
        if age == 0:
            start_cnt_new[6] += cnt
            rest_cnt_new[8] += cnt
        else:
            start_cnt_new[age-1] += cnt
    for age, cnt in rest_cnt.items():
        if age == 0:
            start_cnt_new[6] += cnt
            rest_cnt_new[8] += cnt
        else:
            rest_cnt_new[age-1] += cnt
    rest_cnt = rest_cnt_new
    start_cnt = start_cnt_new
a = sum(x for x in start_cnt.values())        
b = sum(x for x in rest_cnt.values())
sys.stdout.write(f'{a+b}\n')        

