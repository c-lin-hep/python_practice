# python3
# basic practice
# (1) print function
# (2) type of variables
# (3) input
# (4) if else

####
# print section
print('How python prints the words.')

####
# fundamental type
a=1
print('type of a : ', type(a))

b=1.0
print('type of b : ', type(b))

c='1'
print('type of c : ', type(c))

####
# input method
name = input('Hello, what is your name?  ')
print('Hello, ',name, '!')

####
# The input variable is in string type by default. 
# A conversion to the float type can be achieved by "float()" function. 
# Same logic applies for "int()" and "str()"
#
grade = float(input('Input your grade: '))

# TIPS
#
# 1. Every "if", "elif" (equivalent with else if in c++), and "else" need a colon ":".
# 2. Condition does not need a parathensis ().
# 3. The scope of a conditioning statement is governed by the "indentation".
#    The indentation level needs to be identical for the entire scope.
    
if grade >= 80:
    print('Perfect')
elif grade >= 60:
    print('Good')
else:
    print('Bad')

#####
# multiple conditions
#
x = 10
y = -5
if x > 0 and y < 0 :
   print('Third quant!')
if x > 0 or y < 0 :
   print('Not second quant!')
if not x < 0:
   print('First and second quant!')

