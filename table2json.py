#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
import json
from collections import OrderedDict


with open(argv[1], 'rt') as A:
    head_infor = A.readline().rstrip().split('\t')
    table_infor = A.readlines()


Z = []

for line in table_infor:
    s = line.rstrip().split('\t')
    d = OrderedDict()
    for i in range(len(s)):
        d[head_infor[i]] = s[i]
    Z.append(d)

print(Z)
print('***********')
print(json.dumps(Z))
