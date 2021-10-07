#!/usr/bin/env python3
#
# string practice
# C. Lin, 2021 Oct 2
#
# Reference: https://docs.python.org/3/tutorial/introduction.html#
#            https://www.w3schools.com/python/python_ref_string.asp
# 

###########################
# I. print string method.
#
# \n means break a line.
# add "r" before string for the "raw string"
#
print('path is \yes\no.')
print(r'path is \yes\no')

#
# a long sentence can be splitted into multiple lines.
#
print("A long sentence can be splitted"
      "into multiple lines.")


#
# Use """ to include the line break as the content.
# the symbol "\" means not to perform the line break.
#
print("""\
usage:
	- f: force
	- r: recursive
""")

#######################
# II. string operators 
#
# + and *
#
print('very '*3 + 'hungry.')

#
# index operator
#
word='python'
print('test pattern: ', word)
print('word[0]: ', word[0])

#
# index can be negative
# it will be counted from right
# word[a:b] a: included, b: excluded
#
print('word[-1] and word[-2]: ',word[-1], word[-2])

#
# slicing can be achieved by colons.  
#
print('word[1:3]: ', word[1:3])
print('word[1:] : ', word[1:] )
print('word[:3] : ', word[:3] )
print('word[-2:]: ', word[-2:])

# 
# index error can be circumvented by slicing operator
# i.e. word[10]: this is syntax error
#      word[10:]: shows ''
#
print('word[10:]:', word[10:])

#
# len(s): length operator
#
print('len(): ', len(word))


#######################
# III. string functions
#

#
# str.replace(old_val, new_val, count)
#
str_a = 'Replace apple with orange. I like orange.'
print('str_a: ', str_a)
print("str_a.replace('orange','banana') : ",str_a.replace('orange','banana'))
print("str_a.replace('orange','banana',1) : ",str_a.replace('orange','banana',1))

#
# ASC code translation
#
asc_code =  ord('A')
print('ASC code of \'A\'', asc_code)
print('ASC code = ', asc_code, " represents ", chr(asc_code))

#
# str.count('word',start,end): the count of word that appears in 'str'.
#
str_b = 'This is a book and that is a pencil.'
print('str_b = ', str_b)
print('str_b.count(\'a\') ', str_b.count('a') )
print('str_b.count(\'a\',0,10)', str_b.count('a',0,10))

