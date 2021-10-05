#!/usr/bin/env python3
#
# list practice
# C. Lin, 2021 Oct 2
#
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# 

num = [1, 2, 3, 4, 5, 6]

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

num = [1, 2, 3, 4, 5, 6]
print('\n num = ',num,'\n')

#
# append(x): equivalent to a[len(a):] = [x].
#
num.append(7)
print('append(7)       ', num)

#
# extend(iterable): equivalent to a[len(a):] = iterable.
#
num.extend([8,9])
print('extend([8,9])   ', num)

#
# insert(i,x): equivalent to a[i] = x 
#
num.insert(3,2)
print('insert(3,2)     ', num)

#
# remove(x): remove the "first" item whose value is x from the list. 
#
# *** Warning: If there is no such value, ValueError is shown.
# e.g num.remove(-1)
#     ValueError: list.remove(x): x not in list
#
num.remove(2)
print('remove(2)       ', num)

#
# pop(i): Remove the i-th element from the list. 
#         If no index is specified, a.pop() removes and returns the last item in the list.
#
num.pop()
print('pop()           ', num)
num.pop(1)
print('pop(1)          ', num)

#
# clear(): remove everything, equivalent to del a[:]
#
num.clear()
print('clear()         ', num)

num = [-1, -2, -3, -2, -1, -2]
print('\n num = ',num,'\n')

#
# index(x,index_a,index_b): 
#     The index of the first term  whose value is x.
#     - index_a, index_b: optional
#
#     index(x,index_a): 
# 
# *** Warning: if there is no such value, a ValueError is raised.
#
print('num.index(-2)     = ', num.index(-2))
print('num.index(-2,2)   = ', num.index(-2,2))
print('num.index(-2,4,6) = ', num.index(-2,4,6))

#
# count(x): Frequency of x appears in list.
#
print('num.count(-2)     = ', num.count(-2))
print('num.count(0)      = ', num.count(0))


#
# sort(): 
#
num.sort()
print('sort()            = ', num)

#
# reverse():
#
num.reverse()
print('reverse()         = ', num)

#
# copy(): equivalent to a[:]
#
print('num.copy()        = ', num.copy())

#
# Tips:
#    copy is not the same as b = a.
#    "copy" creates another object, which is allocated at different addrress.
#
num_a = num
print('num_a = num')
print('id(num)   = ' ,id(num))
print('id(num_a) = ' ,id(num_a))

num_b = num.copy()
print('num_b = num.copy()')
print('id(num_b) = ' ,id(num_b))

#
# When we change "num", "num_a" will be updated as well because they are actually the 
# same object with but different name. 
#
# (This is the feature of "mutable" objects, whose internal states can be changed.)
# 
num.append(1)
print('num.append(1):')
print('num   = ', num  )
print('num_a = ', num_a)
print('num_b = ', num_b)

#
# list comprehension
#     A list can be constructed with a concise statement.
#
even = [ x*2 for x in range(10)]
print(even)

ex = [(x, y) for x in [1,2,3] for y in [1,2,3] if x != y]
print(ex)

#
# equivalent to
# ex = []
# for x in [1,2,3]:
#     for y in [1,2,3]:
#         if x!= y:
#             ex.append((x,y))
#

ex2 = [x+1 for x in even if x<6 ]
print(ex2)
