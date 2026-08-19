# Numeric Datatype and literal:
'''
- Used to store numeric data.
- Integer, float, complex
'''

# Static numeric input:
marks,perc,coor=480,0.85,4+5j #j is sq.root of -1
#print(type(marks))
#print(type(perc))
#print(type(coor))

# Dynamic Numeric Input: Use Typecasting with input()
#age=input("Enter age: ")
#print(age, type(age))

#age=int(input("Enter age: "))
#print(age, type(age))

#weight=float(input("Enter weight: "))
#print(weight, type(weight))

'''
data= '1234'
print(data, type(data))
temp= int(data)
print(temp, type(temp))
'''

# eval(): typecast data according to their type
#data=eval(input("Enter something: "))
#print(data, type(data))


# Mathematical Operations:
# Arithmetic Operators:
'''
- + (Addition)
- - (Subtraction)
- * (Multiplication)
- / (Division): Return quotient of division
- % (modulo): Return remainder of division
- //(floor): Return largest integer smaller than the
quotient of division.
- **(power): Return raise to the power.
'''
'''
a= int(input("Enter 1st: "))
b= int(input("Enter 2nd: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)
'''
#print(-11//2)

# Conditional (Relational) Operator:
'''
- Compare the values on either sides and decide relation
among them.
- == (Equal to)
- != (Doesnot equal to)
- > (Greater than)
- >= (Greater than equal to)
- < (less than)
- <= (less than equal to)
- Expression return boolean value.
'''
'''
a= int(input("Enter 1st: "))
b= int(input("Enter 2nd: "))
print(a<b)
'''

# Logical Operator:
'''
- Allow us to combine two or more conditional operations.
- 'and' 'or' 'not'
- Expression return boolean value.
'''
'''
print(20==3 and 20>3)
print(20==3 or 20>3)
print(not(20==3))
'''

# Decimal No. to Binary No. system: bin()
#print(bin(7))
#print(bin(5))

# Binary to Decimal:
#print(int(0b101))

#In binary with a zero b prefix
#In octal with a zero o prefix
# In hexadecimal with a zero x prefix

#print(int(0b10000))
#print(int(0o20))
#print(int(0x10))

#WAP to take Principal amount, rate of interest and time
#from user then calculate Simple Interest and Compound Interest.
'''
p=float(input("Enter Principal Amount: "))
r=float(input("Enter RoI in %: "))
t=float(input("Enter Time in yr: "))
# Simple Interest
si= (p*r*t)/100
print('Interest',si)

# Future Value:the total amount payable including principal and interest
FV= p+si
print('Total amount',FV)

# Compound Interest:
a = p*pow((1+(r/100)),t)
print('Amount',a)
print('Compount Interest',a-p)
'''

# Precision Handling: Roundoff of floating point no.
import math
p= math.pi
print(p) #3.141592653589793

# round(value,ndigit):
# It's a builtin module function for round off
# round-off after 2 places of decimal.
#print(round(p,2)) # 3.14
# round-off after 3 places of decimal.
#print(round(p,3)) # 3.142
# round-off after 4 places of decimal.
#print(round(p,4)) # 3.1416

marks=78
# round-off marks after 2 places of decimal i.e, 78.00
#print(round(marks,2)) # desired no. of 'ndigits' are required

#print('%.2f'%marks)

# functions inside math module for precision handling
# math.trunc(): Return integer part of float type value
#print(math.trunc(p)) # 3

# math.ceil(): Return smallest integer greater than
#float type value.
#print(math.ceil(p)) #3.14-->4,5,6,..-->4

# math.floor(): Return largest integer smaller than
#float type value.
#print(math.floor(p)) #3.14-->3,2,1,...-->3

# Other math module functions:
# math.factorial()
#print(math.factorial(5)) # 120

# math.log()
#print(math.log(1))

# math.exp()
#print(math.exp(0))

# trigo func
#print(math.sin(2)) # 2 in radian

#Other math module function:
#https://docs.python.org/3/library/math.html













