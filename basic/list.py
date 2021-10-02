#!/usr/bin/env python3
#
# list practice
# C. Lin, 2021 Oct 2
#
# Reference: https://docs.python.org/3/tutorial/introduction.html#
# 

num = [1, 2, 3, 4, 5, 6]

###########################
# I. list operator
#
print('num       : ', num)
print('num[3]    : ', num[3])
print('num[-1]   : ', num[-1])
print('num[-3:]  : ', num[-3:])

#
# concatenation
#
num2 = [7, 8, 9, 10]
print('num2      : ', num2)
print('num+num2  : ', num+num2)

#
# assign value by index
#
num[0] = 0
print('num[0] = 0: ', num)

#
# append numbers in the list
#
num.append(7)
print('append(7)   ', num)

#
# (1) list is not required to contain the same type
# (2) words can be replaced by slicing operator
# (3) elements can be removed by assigning empty list
#
num[0] = 'a'
print('num[0] = a  ', num)
num[1:3] = ['b','c']
print('num[1:3]=b,c', num)
num[3:] = []
print('num[4:]=[]  ', num)
print('len(num) =  ', len(num))

#
# list can be neseted
#
nest = [num, num2]
print('nest=[num, num2] : ', nest)
print('nest[0][0]       : ', nest[0][0])
print('nest[1][0]       : ', nest[1][0])


