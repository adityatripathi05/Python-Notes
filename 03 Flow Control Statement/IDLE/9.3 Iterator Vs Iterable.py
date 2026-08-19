# Iteration Vs Iterator Vs Iterable:

# Iteration:
'''
It is the process of taking one element at a
time from a sequence of elements i.e, Any time you
use a loop, to go over a group of items is iteration.
'''
####################################################
# Iterable:
'''
- It is an object that has an iter() method which converts
iterable objects into an iterator object.
- So an iterable is an object that you can get an
iterator from.
- str object, tuple object, list object, dict object,
sets object, range object etc are all iterable objects.
'''
########################################################
# Iterator:
'''
- It is an object with a next() method.
- With the help of next() method we can access elements of
iterator object one-by-one.
- next(): returns the next value in the iteration.
    - updates the state to point at the next value.
    - signals when it is done by raising StopIteration
- map object, enumerate object, zip object etc are
all iterator object.
'''

