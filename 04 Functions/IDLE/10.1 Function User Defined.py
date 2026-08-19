# Functions:
'''
- It is a named block of non-self execulable code.
- The idea is to put some common or repeatedly done
task together and make a function, so that instead of
writing the same code again and again for different
inputs, we can call the function.
- In python we have some builtin functions such as print(),
max(), min(), count() etc and also we can create our own
functions known as User defined function.
'''

# Syntax:
'''
def fun_name(parameter):
    'Doc-String'
    block statement
    return statement

fun_name(arguments)
'''

# Create Function without parameter:
'''
def greeting():  
    'Prints a Hello statement.'
    print("Hello")
    print('Welcome to class')

#print(greeting.__doc__)
greeting()
greeting()
'''
########################################################
# Create Function with parameter:
'''
- We can define function with parameters in three types:
    - Parameters with non-default value
    - Parameters with default value
    - Variable no. of Parameters
''' 
# Parameter with Non-Default value:
'''
def greeting(name):
    print('Hello '+name)
    print('Welcome to class')

#greeting()#TypeError: Missing 1 argument
#greeting('Aditya')
#greeting('Preeti')
#greeting('Akshay','Jay')#TypeError:Only 1 argument is req
'''

# Parameter with Some Default value:
'''
def greeting(name='Everyone'):
    print('Hello '+name)
    print('Welcome to class')

#greeting()
#greeting('Sneha')
#greeting('Akshay','Jay')#TypeError:Atmost 1 argument is req
'''

# Parameter with both Non-Default and Default value
# Non-default parameter follows default parameter
'''
def greeting(salutation,name='Everyone'):
    print(salutation)
    print('Hello',name)
    print('Welcome to class')

#greeting('Good Morning')
greeting('Good Evening','Aditya')
'''
######################################################
# Passing Arguments to Function:
'''
- We can pass arguments to function in two ways:
    - As Positional Arguments
    - As Keyword Arguments
'''
# As Positional Arguments:
'''
def display(name, std, marks='passing'):
    print(f'{name} got {marks} marks in class {std}.')

#display('Aditya',12)
#display('Aditya',12,467)
#display(456,'Jay',8)# Desired result is not obtained
'''
# So while passing arguments as positional argument,
# we must pass values in the order of parameter in function definition.

# As keyword Arguments:
'''
def display(name, std, marks='passing'):
    print(f'{name} got {marks} marks in class {std}.')

#display(name='Aditya',std=12)
#display(name='Aditya',std=12, marks=477)
display(marks=456,name='Jay',std=8)
'''
#So while passing arguments as keyword argument, We can
#call functions in such a way that the order of the
#arguments can be changed.
###################################################

# Defining Function for Arbitrary no. Arguments:
'''
- Packing: When we do not know in advance the number of
arguments that will be passed into a function.
    - * is used to pack arguments as tuple.
    - ** is used to pack arguments as dictionary.
'''
# As Tuple:
# * packs positional arguments into a tuple before
# being passed into the function.
'''
def add(*args):
    print('Tuple',args)
    s=0
    for i in args:
        s+=i
    print('Sum',s)

#add(5)
#add(4,5,6)
#add(4,5,6,7,8)
'''

# As Dictionary
# ** packs keyword arguments into a dictionary before
# being passed into the function.
'''
def add(**kwargs):
    print('Dictionary',kwargs)
    s=0
    for i in kwargs.values():
        s+=i
    print('Sum',s)

#add(x=5)
add(x=4,y=5,z=6)
'''

# Function with all types of Parameter:
'''
def func(name,age,*args, **kwargs):
    print('Normal:',name,age)
    print('Tuple:',args)
    print('Dictionary:',kwargs)
    
func('Ben',30, 2,4,6, a=10, b=20)
'''
######################################################
# Function with return statement
'''
- return statement is optional in python and if not
written then default handled by interpreter.
- we want to reuse the result after execution of function
in the program further then use return statement.
- return type of function is the type of value it return.
    - Implicit return type of function NoneType and
    returned value will be None.
'''
'''
def add(a,b):
    s=a+b
    print(s)
    return s

data= add(2,3)
print(data, type(data))
if data%2==0:
    print("Even")
else:
    print("Odd")
'''
# Implicit return statement
'''
def add(a,b):
    s=a+b
    print(s)

add(2,3)
print(temp, type(temp))
'''

# Returning multiple Values:
'''
def display(P,C,M,first,last):
    total=P+C+M
    return total
    fullname= first+' '+last
    return fullname

data= display(67,78,67,'Aditya','Tripathi')
print(data)
'''
'''
- As soon as a return statement is reached in a function,
the function stops executing. Then, the next statement
after the function call is executed.
- We can't write multiple return statement as above for
returning multiple values
'''
# Returning multiple value as tuple
'''
def display(P,C,M,first,last):
    total=P+C+M
    fullname= first+' '+last
    return (total,fullname)

data= display(67,78,67,'Aditya','Tripathi')
print(data,type(data))
print(data[0]) # Access 0th index value inside tuple
print(data[1]) # Access 1st index value inside tuple
'''

# Returning multiple value as list
'''
def display(P,C,M,first,last):
    total=P+C+M
    fullname= first+' '+last
    return [total,fullname]

data= display(67,78,67,'Aditya','Tripathi')
print(data,type(data))
print(data[0]) # Access 0th index value inside list
print(data[1]) # Access 1st index value inside list
'''

# Returning multiple value as dictionary
'''
def display(P,C,M,first,last):
    total=P+C+M
    fullname= first+' '+last
    return {'total':total,'name':fullname}

data= display(67,78,67,'Aditya','Tripathi')
print(data,type(data))
print(data['total']) 
print(data['name'])
'''
#####################################################
# Scope of a Variable:
'''
- Scope of a variable is the portion of a program where
the variable is recognized. 
- The scope for a variable depend on whether it is inside
a function or outside.
- Scope of a variable can be either local or global.
    - 'Global variables' are the one that are defined
    and declared outside a function.
        - We can use them anywhere inside program.
    - 'Local variables' are the one that are defined
    and declared inside a function.
        - We can use them inside function scope only.
'''
# Define local variable:
'''
def cal_mean(a,b):
    total=a+b #a,b,total are local variable
    mean=total/2 # mean is local variable
    print('inside',total)
    return mean

data= cal_mean(4,6)
print(data)
#print(mean) #NameError: Since local variable
#print(total) #NameError: Since local variable
'''

# Define global variable
'''
x=45 #x is global variable
def cal_mean(a,b):
    print('inside',x)
    total=a+b+x 
    mean=total/2
    print('inside',total)
    return mean

data= cal_mean(4,6) #data is global variable
print('outside',data)
print('outside',x)
'''
# Modify global variable inside function definition
'''
x=45
def cal_mean(a,b):
    print('inside',x)
    x=x+2 # Trying to modify x #UnboundLocalError
    total=a+b+x 
    mean=total/2
    print('inside',total)
    return mean

data= cal_mean(4,6)
print('outside',data)
print('outside',x)
'''
# We can’t change the value of global variable from inside
# a function. 
# To do so, we must declare it global inside the function,
# using the ‘global’ keyword.

# Defining global variable inside function:
'''
x=45 #x is global variable
def cal_mean(a,b):
    global x
    print('inside',x) # inside 45
    x=x+2 # Trying to modify x 
    total=a+b+x 
    mean=total/2
    print('inside',total) # inside 57
    return mean

data= cal_mean(4,6)
print('outside',data) #outside 28.5
print('outside',x) # outside 47
'''
'''
- If global variable is defined inside function then
if it's value will change inside function then will
also get change outside the function definition.
'''
# Defining global and local varaible with same name'
'''
- If two variables are defined with the same name
with the two different scopes, i.e, local and global,
then the priority will always be given to the local
variable inside function.
'''
'''
x=45# global variable x
def cal_mean(a,b):
    x=2 # local variable x
    total= a+b+x
    print(total)
    mean= total/3
    return mean

data= cal_mean(4,6)
print(data)
'''
######################################################
# Delete a function: del destructor
'''
def display(name):
    print('Hello',name)

display('Aditya')
del display
#display('Neetu') #NameError
'''
######################################################
# Anonymous Function: lambda expression
'''
- lambda keyword is used to create anonymous functions.
    - lambda exp. is not declared by 'def' keyword.
    - lambda exp. can have any no. of parameters but
    return one value for the expression we have defined it.
    - lambda exp. has no name but it can be called
    through the variable it is assigned to.
- Syntax: lambda parameters : expression
'''
# Program for addition of two no.
# Using normal function
'''
def add(a,b):
    return a+b

total= add(5,7)
print(total)
'''
# Using lambda expression:
'''
add= lambda a,b: a+b
total= add(5,7)
print(total)
'''

# Program to check whether no. is even or not.
# Using normal function
'''
def even(n):
    return n%2==0

result= even(16)
print(result)
'''
# Using lambda expression:
'''
even= lambda n: n%2==0
result= even(16)
print(result)
'''
# lambda expression with conditional statement
# Program to find a no. is even or odd.
# Using normal function:
'''
def even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

result=even_odd(7)
print(result)
'''
# Using lambda expression:
'''
even_odd= lambda n: "Even" if n%2==0 else "Odd"
result=even_odd(7)
print(result)
'''








