# Tuple Datatype:
'''
- Tuples are sequence of collection of different data types.
- The items in the tuples are seperated by commas (,) and
delimited by parentheses(Parentheses is optional).
- Tuple object is immutable.
- Tuple object is iterable.
'''

# Empty Tuple:
'''
empty=()
print(empty, type(empty), len(empty))
'''

# Non-empty Tuple:
# Tuple having single value:

name= ('Aditya',)
#print(name, type(name), len(name))


# Tuple having multiple values:
detail=101,'Aditya','CBSE',88
#print(detail, type(detail), len(detail))
detail=(101,'Aditya','CBSE',88)
#print(detail, type(detail), len(detail))

# Access elements of Tuple:
# Indexing:
# Syntax: object[index]
'''
print(detail[0])
print(detail[-4])
'''

# Index Slicing:
# Syntax: object[start:stop:step]
'''
print(detail[::])
print(detail[1:3])
print(detail[::-1]) # Reverse of tuple
'''

# Operations on Tuple
# Assignment Operation: '='
#detail[0]= 102
# Error: 'tuple' object does not support item assignment
#print(detail)

# Concatenation: '+'
#conc= detail+name
#print(conc)

# Replication: '*'
#rep= name*4
#print(rep)

# count(): object.count(element)
#print(detail.count(101))

# Numeric Tuple:
marks= 50,80,80,67.5,50,70
# min(), max(), sum() are builtin functions to calculate
# minimum, maximum and total respectively.
print(min(marks))

print(max(marks))

print(sum(marks))


















