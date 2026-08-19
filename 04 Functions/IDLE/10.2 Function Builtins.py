# map():
'''
- It's a builtins module function.
- Executes a specified function for each item in a
iterable sequence.
- Syntax: map(function, iterable)
- map() return iterator map object.
- NOTE: We can pass one or more iterable to the map().
'''

# WAP to calculate length of all names
names=['Ravi','Rohan','Shivam','Pi']
# Using simple for
'''
length=[]
for n in names:
    length.append(len(n))
print(length)
'''
# Using list comprehension
'''
length=[len(n) for n in names]
print(length)
'''
# Using map():
'''
length= map(len,names) # return iterator object
for l in length:
    print(l)
'''

# Create user defined 1-D integer Array:
# Simple logic
'''
n= input("Enter comma seperated values: ").split(',')
print(n, type(n))
arr=[]
for i in n:
    arr.append(int(i))
print(arr)
'''
# Using map():
'''
arr=list(map(int,input("Enter comma seperated values: ").split(',')))
print(arr)
'''

# WAP to square all even no. and negative of odd no.
# of array input by user.
# Normal logic:
'''
arr=list(map(int,input().split(',')))
res=[]
for n in arr:
    if n%2==0:
        res.append(n*n)
    else:
        res.append(-n)
print(res)
'''
# Using map function:
'''
arr=list(map(int,input().split(',')))
def func(n):
    if n%2==0:
        return n*n
    else:
        return -n

res= list(map(func,arr))
print(res)
'''
# Using map() and lambda expression
'''
arr=list(map(int,input().split(',')))
func=lambda n: n*n if n%2==0 else -n
res= list(map(func,arr))
print(res)
'''

# WAP to calculate percentage marks obtained in each subject
# after half and final exam.
'''
half=[89,56,76,67,78]
final=[56,78,67,77,87]
res=list(map(lambda x,y:((x+y)/200)*100,half,final))
print(res)
'''
 
# List of strings
'''
l = ['sat', 'bat', 'cat'] 
test = list(map(list, l)) 
print(test)
'''

# 2-D Squared Array from user:
'''
n = int(input("Enter number of rows: "))  # i/p number of rows
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))  # i/p space seperated values
print(arr)
'''

#######################################################
# filter():
'''
- It's a builtins module function.
- Constructs an iterator from elements of an iterable
for which a function returns True.
- Syntax: filter(function, iterable)
'''
# WAP to filter all even no. from array
# Normal logic:
'''
arr=list(map(int,input().split()))
even_filter=[]
for n in arr:
    if n%2==0:
        even_filter.append(n)
print(even_filter)
'''
# Using filter()
'''
arr=list(map(int,input().split()))
even_filter=list(filter(lambda n: n%2==0,arr))
print(even_filter)
'''
#######################################################

# reduce():
'''
- Used to apply a particular function to all of the
elements of iterable.
- This function is defined in “functools” module.
- Syntax: functools.reduce(function, iterable)
'''

# WAP to calculate cumulative frequency.
'''
import functools
freq = [11, 2, 23, 14, 8]
cum = functools.reduce(lambda x, y: x*y, lst)
print(cum)
'''
