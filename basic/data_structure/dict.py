#!/usr/bin/env python3
#
# dictionary practice
# C. Lin, 2021 Oct 5
#
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
#

#
# dict(): constructs the key-value pairs
#
dict1 = {'a':1, 'b':2, 'c':3}
print('dict1 = ', dict1)

dict2 = dict([('a',1), ('b',2), ('c',3)])
print('dict2 = ', dict2)

#
# insert new key
# 
dict2['d'] = 4
print('dict2 = ', dict2)

#
# remove a key
#     - pop(key)
#     - del dict(key)
#     - remove last item: popitem()
#
dict2.pop('d')
print('dict2.pop(\'d\')')
print('dict2 = ', dict2)

del dict2['c']
print('del dict2[\'c\']')
print('dict2 = ', dict2)

print('Delete last item by popitem()')
dict2.popitem()
print('dict2 = ', dict2)

#
# extract the keys from dictionaries and contain them in list.
#     - list(dict)
#
list1 = list(dict1)
list2 = dict1.keys()
print('list(dict1) = ',list1)

#
# dict comprehensions
#
dict3 = dict(a=1, b=2, c=3)
print('dict3 = ',dict3)

dict4 = {x: x**2 for x in [1,2,3]}
print('dict4 = ', dict4)

#
# dict.item(): retrive a tuple for key-value pair
#
print('Demonstrate items() with "for"')
for k, v in dict1.items():
    print(k, v)

#
# dict.fromkeys(key_list, value): create a dictionary with key_list and values (or value list)
#
y = [1,2,3]
dict5 = dict.fromkeys(list1,y)
print('dict5 = dict.fromkeys(list1,y=1) : ', dict5)

