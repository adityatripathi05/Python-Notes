# String Literal and Datatype:
'''
- Strings in Python are a sequence of collection
unicode characters delimited by single, double or tripple
quotes.
- Strings are used in Python to record text information,
such as name.
- Python strings are immutable i.e, operations performed on
string will not change the orginal string.
- Python strings are iterable.
'''
# ord(): Return unicode value of a character
'''
print(ord('a'))
print(ord('A'))
print(ord('0'))
print(ord('9'))
print(ord('.'))
print(ord('न'))
'''
# chr(): Return character for given unicode value
'''
print(chr(2344))
print(chr(27)) # Esc
'''

# Empty String:
'''
st=''
print(st)
print(type(st))
print(len(st))
'''

# Non-Empty String:
# Static input:
a,b,c,d= 'bye',"HELLO",'1234','Py381'
para='''welcome to Ducat.
this is Machine Learning.'''
#print(type(a))
#print(type(b))
#print(type(para))

# Dynamic string input: input()
# Syntax: input(prompt) #prompt/msg is optional
'''
name= input("Enter your name: ")
print(name)
print(type(name))
'''
'''
age= input("Enter your age: ")
print(age)
print(type(age))
'''
# NOTE: input() return type is string.

# Output Statement: print()
# Syntax: print(value1,value2,...,sep=' ',end='\n', file=sys.stdout)
'''
print(a,b,end='_')
print(a,b,sep='.')
'''
'''
import sys
sys.stdout.write(a)
'''

# Access String Elements:
# Indexing: Access single character of string
# Syntax: object[index]
'''
- Python support forward indexing: start with 0
- Python support backward indexing: start with -1
'''
'''
print(b[4])
print(b[-1])
print(para[-1])
'''
# Index Slicing: Access Multiple elements
'''
- Syntax: object[start:stop:step]
- Properties of arguments:
    1. All three are optional.
    2. Default value of start, stop, step is 0,len(object)
    ,1 (during forward index slicing) respectively.
    3. Stop Index is exclusive.
'''

#print(b[::])
#print(b[1::])
#print(b[1:])
#print(b[1:3])
#print(b[-4:-2])
#print(b[::2])
#print(b[-1::-1])
#print(b[::-1])


# Operators:
'''
- Operators are used to perform some operations on
operands.
- Arithmetic, Assignment, Conditional, Logical, Bitwise,
Identity, Membership Operators
'''

# Operations on string:

# Assignment Operation: '=' Operator
#b[0]='X'#Assignment Error since Immutable object
#print(b)

# Concatenation Operation: '+' Operator
'''
first=input("Enter 1st name: ")
last=input("Enter last name: ")
full= first+' '+last
print(full)
'''

# Replication Operation: '*' Operator
#print(a*3)
#print('-'*7)

# Identity Operator: Compares memory address of object.
# 'is' 'is not' are identity operator
# This statement return boolean value.
'''
x='Hello'
y='Hello'
print(id(x), id(y))
print(id(x)==id(y)) #'==' comparison operator
print(x is y)
print(x is b)

print(id(x)!=id(b))
print(x is not b)
'''

# Membership Operator:
'''
- The membership operators in python are used to test
for membership of values or variables in sequences
- 'in' 'not in' are membership operators.
- This statement return boolean value.
'''
'''
print('m' in para)
print('Mac' in para)
print('Py' in para)
print('Py' not in para)
'''

# Builtin functions of string:
'''
- upper(): Convert all lower alphabet character
elements of the string to upper case.
- lower(): Convert all upper alphabet character
elements of the string to lower case.
'''
#print(a.upper(), d.upper())
#print(b.lower(), d.lower())

'''
- isupper(): Check whether all characters of string
are in upper-case only.

- islower(): Check whether all characters of string
are in lower-case only.

- isdigit(): Check whether all characters of string
are numeric only

- isalpha(): Check whether all characters of string
are alphabet only

- isalnum(): Check whether all characters of string
are either alphabetic or numeric only.
'''
#print(b.islower(), d.islower(), a.islower())
#print(b.isupper(), d.isupper(), a.isupper())
#print(c.isdigit(), d.isdigit())
#print(a.isalpha(), d.isalpha())
#print(c.isalnum(), d.isalnum(),a.isalnum())
#print(para.isalnum())

#count(): No. of occurence of an substring
#print(b.count('LL'))
#print(para.count(' '))

#find(): Return index of first occurence from left of string.
#print(b.find('LL'))
#print(b.rfind('L'))

#replace():
'''
- It returns copy of string where all occurrences
of 'old substring' have been replaced by 'new substring'.
- Syntax: str.replace(old,new,-1)
- -1 denote all occurences of 'old' will be replaced by 'new'.
'''
#print(id(b))
#new_b= b.replace('L','n',1)
#print(new_b, id(new_b))

#capitalize():Return copy of string, converting the
# first alphabetic character if present to upper case,
#and rest alphabetic character to lower case.
'''
print(a.capitalize())
print(b.capitalize())
print(para.capitalize())
temp='23NumBER'
print(temp.capitalize())
'''

#title(): Return copy of string, converting the
# first alphabetic character of each word if present
# to upper case, and rest alphabetic character to lower
# case.
#print(a.title())
#print(b.title())
#print(para.title())

#strip():Remove character from leading and trailing.
# Default charcater is space.
'''
text='   Hello   '
print(text)
print(text.strip())
#lstrip() and rstrip()
print(text.lstrip())
print(text.rstrip())
'''
name='aditya'
#print(name.strip('a'))
#print(name.lstrip('a'))
#print(name.rstrip('a'))

# Other string Operations:
# https://docs.python.org/2.4/lib/string-methods.html

# String Formatting: Dynamic Data inclusion
#print('Python language')

#version=float(input("Enter version: "))
#print('Python version language')

#print('Python %.2f language'%version)
# %f- float value
# %d- integer value
# %s- string value

#feature=input("Enter feature: ")
#print('Python %.2f language is %s'%(version,feature))

# After Py3.5
#print(f'Python {version} language is {feature}')

'''
first=input("Enter 1st: ")
last=input("Enter last: ")
name=f'{first} {last}'
print(name)
'''
