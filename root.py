#!/usr/bin/python3

import numpy as np

num = int(input())

flag = 0

for i in range(2,int(np.sqrt(num))):
    if num % i == 0:
        flag = 1
        break

if flag == 1:
    print("Not Prime")
else:
    print("Prime")
