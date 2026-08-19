# Generator:
'''
- Generator are the simple way of creating iterators.
- A generator is a function that returns an object
(iterator) which we can iterate over (one value at a time).
- It is as easy as defining a normal function with
'yield' statement instead of a 'return' statement.
- Both yield and return will return some value from a
function.
- The difference is that,
    - while a 'return' statement terminates a function
    entirely,
    - yield statement pauses the function saving all its
    states and later continues from there on successive
    calls.
'''

#########
#Create generator with several yield statements.
'''
def seq_gen():
    yield 'Ducat'
    yield 'Py-DS-ML'
    yield 15000
    
g = seq_gen() # return iterator object, saving in g
print(next(g))
print(next(g))
print(next(g))
print(next(g)) # Stop Iteration
'''

#########
#yield statement pauses the function saving all its states
'''
def seq_gen():
    n=1
    print('state:', n)
    yield n
    n+=1
    print('state:', n)
    yield n
    n+=1
    print('state:', n)
    yield n
    
g = seq_gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
'''

###########
# Implementing using loop having a suitable terminating condition:
'''
def seq_gen():
    for i in range(1,4):
        print('state:', i)
        yield i
    
g = seq_gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
'''

##########
# Generators with for loops
'''
def generator_func():
    for i in range(1,4):
        print('state:', i)
        yield i
    
for g in generator_func():
    print(g)
'''

#########    
# WAP to print square of numbers from 1 to n:

# Normal Approach:
'''
n= int(input("Enter range: "))
sq_arr=[]
for i in range(n):
    sq_arr.append(i*i)
print(sq_arr)
'''

# Using generator:
'''
def sq_gen(n):
    num=1
    while True:
        yield num
        if num==n:
            return
        else:
            num +=1

n= int(input("Enter end of range: "))
sq_arr=[]
for i in sq_gen(n):
    sq_arr.append(i*i)
print(sq_arr)
'''

# Compare memory usage:
'''
import sys
n= int(input("Enter range: "))

#List Comprehension
arr_lc=[i*i for i in range(n)]
print(sys.getsizeof(arr_lc)) #bytes

#Geneartor Comprehension
arr_gc= (i*i for i in range(n))
print(sys.getsizeof(arr_gc))
'''
'''
- If the list is smaller than the running machine’s
available memory, then list comprehensions can be
faster to evaluate than the equivalent generator
expression.
'''
# Compare computation time:
'''
import timeit
print(timeit.timeit('a=[i*i for i in range(10000)]',
                    number=10000))

print(timeit.timeit('g=(i*i for i in range(10000))',
                    number=10000))
'''

# WAGF to print fibonacci series upto given no. of terms
# WAGF to calculate factorial of elements upto given range.
