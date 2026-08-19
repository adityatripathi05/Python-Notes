##########
# Error:
'''
- Error is an illegal operation performed by the programmer/
user which results in abnormal working of the program.
'''

#########
# Error Types:
'''
- Syntax Error or Parsing Error or Compilation Error
- Logical Error 
- Run-time Error
'''

# Ex. Syntax Error:
'''
print('Start')
print('Hello) # Syntax Error
print('End')
'''

# Ex. Logical Error:
'''
n = int(input("Enter a no. "))
if n%2==0:
    print("Odd")
else:
    print("Even")
'''

# Ex. Run-time Error:
'''
print('Start')
n1 = int(input("Enter a no. "))
n2 = int(input("Enter a no. "))
div = n1/n2  # May Raise ZeroDivision Exception
print(div)
print('End')
'''

##########
# Error Handling:
'''
- Syntax Error and Logical Error can only be handled by
programmer.
- But Run-time Error can be handled by either programmer
or PVM.
'''

##########
# Exceptions:
'''
- Errors detected during execution are called exceptions.
- An exception can be defined as an abnormal condition in
a program resulting in the disruption in the flow of the
program.
- Whenever an exception occurs, the program halts the
execution, and thus the further code is not executed.
Therefore, an exception is the error which python script
is unable to tackle completely.
'''

############
# Handle Exception:
'''
- Python provides us with the way to handle the Exception
using try-except-else-finally-raise statement.
- We want to handle the Exception so that the other part
of the code can be executed without any disruption.
- However, if we do not handle the Exception, the PVM
handles the Exception but then it doesn't execute all the
code that exists after the statement which Raised
Exception.
'''

#############
# Examples of Exception:
#print(1/0) #ZeroDivisionError

#print(x) #NameError

#marks=[50,60,40]
#print(marks[6]) #IndexError

#open('error.txt') #FileNotFoundError

#age= int(input("Enter age: ")) #ValueError
#print(age

#print(4+' runs') #TypeError

#d={'name':'aditya'}
#print(d['age']) #KeyError

##############
# Exception class Hierarchy
'''
import builtins
print(help(builtins))
'''

#############
#try-except-else-finally statement:
'''
- Syntax:
try:
    block of code  #doubtful code
except Exception_class1:
    block of code  #executes if exception occurs in the try block 
except Exception_class2: 
    block of code  #executes if first except block was unable to handled the exception    
else:  
    block of code #executes only if no exception occurs in the try block
finally:
    block of code  #will always be executed   
other code
'''

# Summary:
'''
- 1) The try block lets you test a block of code for
errors.
- 2) The except block lets you handle the error.
We can declare multiple except statement.
- 3) The else block run if no exception occurs.
- 4) The finally block lets you execute code, regardless
of the result of the try and except blocks.
'''

###########
# Handling ZeroDivisionError:
'''
print('Start')
nr=int(input("Enter numerator: "))
dr=int(input("Enter denominator: "))
try:
    div=nr/dr #Exception
except ZeroDivisionError as e:
    print(e)
else:
    print(div)
finally:
    print('End')
'''

############
# Handle Multiple Exception using multiple except:
'''
print('Start')
try:
    nr=int(input("Enter numerator: "))
    dr=int(input("Enter denominator: "))
    div=nr/dr
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print(div)
finally:
    print('End')
'''

###############
# Handle Multiple Error using single except statement:
'''
print('Start')
try:
    nr=int(input("Enter numerator: "))
    dr=int(input("Enter denominator: "))
    div=nr/dr
except (ZeroDivisionError,ValueError) as e:
    print(e)
else:
    print(div)
finally:
    print('End')
'''

###############
# Handle Exceptions with 'Exception' class
'''
print('Start')
try:
    nr=int(input("Enter numerator: "))
    dr=int(input("Enter denominator: "))
    div=nr/dr
except Exception as e:
    print(e)
else:
    print(div)
finally:
    print('End')
'''

###############
# Handle Exception Gracefully:
'''
print('Start')
try:
    nr=int(input("Enter numerator: "))
    dr=int(input("Enter denominator: "))
    div=nr/dr
except (ZeroDivisionError,ValueError):
    print('Please input carefully')
else:
    print(div)
finally:
    print('End')
'''
##############
# Assert Statement: For debuging
'''
- Syntax: assert condition
'''
'''
try:
    age=int(input("enter age: "))
    assert age>0
except AssertionError:
    print('Age can\'t be negative')
else:
    print('Your age is',age)
'''

############
# Raising Exception:
'''
- In python we can raise an exception explicitely using
'raise' keyword.
- The raise statement allows the programmer to force a
specific exception to occur.
'''

# Custom exception class:
'''
class AgeNegativeError(Exception):
    def __init__(self,msg):
        self.message=msg

def checkAge(a):
    if a<0:
        raise AgeNegativeError('Age can\'t be negative')
try:
    age=int(input("enter age: "))
    checkAge(age)
except AgeNegativeError as e:
    print(e.message)
else:
    print('Your age is',age)
'''
