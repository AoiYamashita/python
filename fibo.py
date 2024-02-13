#!/usr/bin/python3

value_num = int(input("number is "))

fibo_nums = [0 for i in range(value_num+2)]

fibo_nums[0] = 1
fibo_nums[1] = 1

def fibo_num(value):
    if value == 0 or value == 1:
        return 1
    if fibo_nums[value-1] == 0:fibo_nums[value-1] = fibo_num(value-1)
    if fibo_nums[value-2] == 0:fibo_nums[value-2] = fibo_num(value-2)
    return fibo_nums[value-1] + fibo_nums[value-2]

print(fibo_num(value_num))
#print(fibo_nums)