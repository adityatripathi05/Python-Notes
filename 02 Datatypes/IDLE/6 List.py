# List Literal and Datatype:
'''
- List are sequence of collection of different data types.
- The items in the list are seperated by commas (,) and
delimited by square brackets [].
- List object is mutable.
- List object is iterable.
'''

# Empty List:
data= []
#print(data,type(data),len(data))

# Non-Empty List:
detail=[101,'Aditya',88.8,('P','C','M'),['Half','Final']]
#print(len(detail),type(detail))
#print(id(detail))

# Access the Elements of list:
# Indexing: object[index]
#print(detail[3]) #('P','C','M')
#print(detail[-2]) # ('P','C','M')
#print(detail[-1][1][1]) #['Half','Final']==>'Final'==>'i'

# Index Slicing: object[start:stop:step]
#print(detail[1:4])
#print(detail[-4:-1])
#print(detail[-2:-5:-1])
#print(detail[-1::-1])

# Operations on List:
# Assignment Operation:
detail[0]=102
#print(detail)
#print(id(detail))

# copy(): It creates a shallow copy of object at new memory address
'''
copy_detail= detail.copy()
print(copy_detail)
print(id(copy_detail))

copy_detail[1]='Vinay'
print(copy_detail)
print(detail)
'''

# Concatenation of list
loc= ['Delhi','U.P.']
new= detail+loc
#print(new)

# Replication:
#print(loc*2)

# count(): Return the no. of occurences
#print(detail.count('Aditya'))

# List Modification: add/remove elements from list
# append(): It adds an element at the end of list
# Syntax: object.append(element)
#print(detail)
detail.append(25)
#print(detail)

# extend():It adds multiple elements at the end of list iteratively.
# Syntax: object.extend(sequence)
#print(detail)
detail.extend('TIME')
#print(detail)
detail.extend(['Jan',1])
#print(detail)

# insert():It adds an element at given index.
# Syntax: object.insert(index, element)
#print(detail)
detail.insert(2,'Aditya')
#print(detail)

# remove():It remove the first occurence from left of
# given element from the list.
# Syntax: object.remove(element)
#print(detail)
detail.remove('Aditya')
#print(detail)
detail.remove(['Half', 'Final'])
#print(detail)

# pop(): It remove the element from given index.
# Syntax: object.pop(index)
# Default value of index is -1 i.e, last index element will get removed
#print(detail)
detail.pop()
#print(detail)
detail.pop(3)
#print(detail)

# pop() has an advantage that it return the element it remove
#print(detail)
temp=detail.pop(3)
#print(detail)
#print(temp)

# clear(): Empty the list
#print(detail)
detail.clear()
#print(detail)

# More functions on list:
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3.8/library/stdtypes.html#lists

# Array: Array is collection of data of similar datatype.
# Integer Array:
marks=[45,67,34,56,89]
#print(marks, type(marks))
#print(min(marks))
#print(max(marks))
#print(sum(marks))

# sort(): Arrange the array in order. Default in Ascending Order
#print(marks)
#marks.sort()
#print(marks)

# In descending
#print(marks)
#marks.sort(reverse=True)
#print(marks)

# array module:
# Create array:
'''
- Syntax: array.array(typecode,[initializers])
- Where typecode:
    - i - signed integer of size 2 bytes
    - f - float of size 4 bytes
    - d - floating point of size 8 bytes
    - c - character of size 1 byte
'''
import array
marks= array.array('i',[45,67,34,56,89])
#print(marks, type(marks))

# Indexing:
#print(marks[-2]) # 56

# Index Slicing:
#print(marks[::-1]) # reverse

# append()
marks.append(78)
#print(marks)

marks.extend([9,3])
#print(marks)

marks.insert(3,1)
#print(marks)

# Remove elements
marks.remove(3)
#print(marks)

# sum
#print(sum(marks))

# More on array Module:
# https://docs.python.org/3/library/array.html




