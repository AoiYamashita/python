#!/usr/bin/python3

num = int(input("max of primes : "))

flags = [1 for i in range(num+1)]

flags[0] = 0
flags[1] = 0

for i in range(0,len(flags)):
    if flags[i] != 0:
        t = 2
        while i * t < num+1:
            flags[i*t] = 0
            t += 1
        print(i)

