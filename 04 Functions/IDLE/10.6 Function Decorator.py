# First class function:
'''
A programming language is said to support first-class function
if it treats function as first class object.
'''
# First class objects:
'''
In python first class object means that it can be dynimically
created, stored in data structures, passed as an argument,
passed to a function, returned as a value or used in control
structures.
'''
############################################################
# Assigning function to a variable:
'''
def square(x):
    return x*x

sq = square(5)
print(square)
print(sq)
'''
#
'''
def square(x):
    return x*x

sq = square # assigning function to a variable
print(square)
print(sq)
print(sq(5))
'''

#########################################################
# Passing function as argument to other function:
'''
- Because functions are objects we can pass them as
arguments to other functions.
- Functions that can accept other functions as arguments are
also called higher-order functions.
- Eg. sort(), map(), reduce(), filter() etc.
'''
'''
def summation(nums): # Normal function
    return sum(nums)

def my_func(f, args): # higher order function
    result= f(args) # Calling normal function
    return result
    
print(my_func(summation, [1,2,3,4]))

#print(my_func(max, [1,2,3,4]))
'''
###########################################################
# WAF to build your own map function:
'''
def square(x):
    return x*x

def cube(x):
    return x*x*x

def my_map(func, arg_list):
    result=[]
    for i in arg_list:
        result.append(func(i))
    return result

lis = [1,2,3,4,5]
sq_ans = my_map(square, lis)
print(sq_ans)

cu_ans = my_map(cube, lis)
print(cu_ans)
'''

###########################################################
# Function as a return value:
'''
def add_two(x,y):
    return x+y

def add_three(x,y,z):
    return x+y+z

def add_any(*args):
    return sum(args)

def get_appropriate(num_len):
    if num_len==3:
        return add_three
    elif num_len==2:
        return add_two
    else:
        return add_any
    
args=[1,2,3,4]
result_func= get_appropriate(len(args))
print(result_func)
print(result_func(*args))

args=[1,2]
result_func= get_appropriate(len(args))
print(result_func)
print(result_func(*args))
'''

#########################################################
# Nested functions in Python:
'''
- A function which is defined inside another function is
known as nested function.
- Python allows a nested function to access the outer
scope of the enclosing function i.e, nested functions are
able to access variables of the enclosing scope.
-In Python, these non-local variables can be accessed only
within their scope and not outside their scope.

# NOTE: This is a critical concept in decorators -- this
pattern is known as a Closure.
'''
'''
def mathematics(x,y): # Enclosing Function
    z = 9 # Local variable of Enclosing function
    def add(x,y): # Nested Function
        return x+y+z # Accessing local variable of Enclosing function
    return add(x,y)

print(mathematics(5,6))
'''
#########################################################
# Python Closures:
'''
- A closure is a way of keeping alive a variable even when
the function has returned.
- So in a closure, a function is defined along the
environment. In python this is done by nesting a function
inside the encapsulating function and then returning the
underlying function.
'''

def greeting(name, gender):
    def salutation():
        if gender=='M':
            return f'Mr. {name}'
        elif gender=='F':
            return f'Ms. {name}'
        else:
            return name
    return salutation # NOTE: returning function without paranthesis

person1 = greeting('Aditya','M')
print(person1())

#person2 = greeting('Neha','F')
#print(person2())

#person3 = greeting('Neha','other')
#print(person3())


#########################################################
# Decorator:
'''
- A decorator is a design pattern in Python that allows a
user to add new functionality to an existing object
without modifying its structure.

- Decorators are usually called before the definition of
a function you want to decorate.

- In Decorators, functions are taken as the argument into
another function and then called inside the wrapper
function.
Decorator act as a wrapper for your original function.
'''
#######################################################
'''
def decorator(func):
    def wrapper():
        print('Hello')
        return func()
    return wrapper


def greeting():
    print("Welcome to Python class")

deco = decorator(greeting)
deco()
'''
# decorator implementation using @
'''
def decorator(func):
    def wrapper():
        print('Hello')
        return func()
    return wrapper

@decorator
def greeting():
    print("Welcome to Python class")

greeting()
'''
#######################################################
# More than one decorator: Uses bottom-up approach
'''
def decorator1(func):
    def wrapper():
        return func().upper()
    return wrapper

def decorator2(func):
    def wrapper():
        return func().split()
    return wrapper

@decorator2
@decorator1
def greeting():
    return "Welcome Everyone"

print(greeting())
'''
########################################################
# Real life implementation of decorator:
'''
def cal_sq(num):
    res=[]
    for i in num:
        res.append(i*i)
    return res

def cal_cu(num):
    res=[]
    for i in num:
        res.append(i*i*i)
    return res

arr = range(1,100000)
res_sq = cal_sq(arr)
res_cu = cal_sq(arr)
'''
# Now we want to calculate performance of functions
# Normal way:
'''
import time

def cal_sq(num):
    start= time.time() #epoch time- 1970, Jan 1
    res=[]
    for i in num:
        res.append(i*i)
    end= time.time()
    print(f'calculating sq took {(end-start)*1000} millsecond')
    return res

def cal_cu(num):
    start= time.time()
    res=[]
    for i in num:
        res.append(i*i*i)
    end= time.time()
    print(f'calculating cube took {(end-start)*1000} millsecond')
    return res

arr = range(1,1000000)
res_sq = cal_sq(arr)
res_cu = cal_cu(arr)
'''

# Using decorator:
'''
import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        start= time.time()
        result= func(*args, **kwargs)
        end= time.time()
        print(f'{func.__name__} took {(end-start)*1000} millsecond')
        return result
    return wrapper

@cal_time  # cal_time(cal_sq)      
def cal_sq(num):
    res=[]
    for i in num:
        res.append(i*i)
    return res

@cal_time
def cal_cu(num):
    res=[]
    for i in num:
        res.append(i*i*i)
    return res

arr = range(1,1000000)
cal_sq(arr)
cal_cu(arr)
'''


