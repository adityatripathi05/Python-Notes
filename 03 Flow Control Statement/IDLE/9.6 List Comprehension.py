# Comprehension:
# List Comprehension:
name=['Ravi','Neha','Priya','Vijay']
# Using for loop:
'''
greeting=[]
for n in name:
    greeting.append('Hello '+n)
print(greeting)
'''
# Using list Comprehension:
'''
greeting=['Hello '+n for n in name]
print(greeting)
'''

# WAP to get square of no. from 1 to 10.
'''
sq=[i**2 for i in range(1,11)]
print(sq)
'''

# WAP to get square of odd no.s from 1 to 10.
# Using for loop
'''
sq=[]
for i in range(1,11):
    if i%2:
        sq.append(i**2)
print(sq)
'''
# Syntax: sequence= [expression(element) for element in iterable if condition]
# Using list comprehension:
'''
sq=[i**2 for i in range(1,11) if i%2]
print(sq)
'''
# WAP to get sq. of all even no. and negative of all odd no.
# from 1 to 10.
# Using for loop
'''
seq=[]
for i in range(1,11):
    if i%2==0:
        seq.append(i**2)
    else:
        seq.append(-i)
print(seq)
'''
# Using list comprehension
'''
sq=[i**2 if i%2==0 else -i for i in range(1,11)]
print(sq)
'''

