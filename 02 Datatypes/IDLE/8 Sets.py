# Sets Literal and Datatype:
'''
- Sets are unordered, unindexed collection datatype
that has no duplicate elements.
- The items in set are separated by commas (,) and
enclosed within curly braces {}.
- Sets object are mutable.
- Sets object are iterable.
'''

# Empty sets:
s0=set()
#print(s0,type(s0),len(s0))

# Non-Empty sets:
s1={34,67,'Hello',45.6,67,'hi'} # Duplicate element will be taken once only
#print(s1, type(s1), len(s1))

# Access sets element:
#print(s1[0]) # Error: Unsubscriptable

# Membership Operator: in/not in
#print(3 in s1) # False
#print(67 in s1) # True
#print(88 not in s1) # True

# Mathematical Operations on Sets:
s2={'hi',67,90,88.8}

#union(): Return new set with elements from both s1 and s2
#print(s1.union(s2))

#intersection(): Return new set with elements common to
# s1 and s2
#print(s1.intersection(s2))

#difference(): Return new set with elements in s1 but
#not in s2
'''
print(s1)
print(s1.difference(s2)) # Return elements of s1 excluding common element in s2
print(s2)
print(s2.difference(s1))
'''

# Symmetric Difference:
#Return new set with elements in either s1 or s2 but not both
#print(s1.symmetric_difference(s2))

# add(): Adds an element to sets
'''
print(s1)
s1.add('bye')
print(s1)
'''

# update():
'''
print(s1)
s1.update(s2)
print(s1)
'''

# remove():
'''
print(s1)
s1.remove('hi')
print(s1)
'''

# pop(): remove an arbitrary element and return it also.
'''
print(s1)
temp= s1.pop()
print(temp)
print(s1)
'''

# Other sets function:
# https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset





