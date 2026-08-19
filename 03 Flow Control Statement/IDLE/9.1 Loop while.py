# Flow Control Statement continues...
# Loop
'''
- While programming, you will encounter many situations
when you need to execute block of code repeatedly.
- Instead of writing those statements again and again
we use to loops over statement.
- Python supports two types of loops: ‘for’ and ‘while’.
'''
# 'while' Loop:
'''
- The code in a 'while clause' will be executed as long
as the 'while' statement's condition is True.
'''
# Working of 'while' loop
'''
- The 'while' statement condition is checked first
and if it returns True, the block of code inside the
'while' loop is executed.
- At the end of a while clause, the program execution
jumps back to the start of the while statement.
- If the 'while' statement condition still returns True,
then the statements are executed again.
- If the test expression is False, the 'while' loop is
terminated.
'''
# if-statement
''''
print('Start')
spam=0
if spam <5:
    print('Hello World')
    spam=spam+1
print('End')
'''

# while-statement
'''
print('Start')
spam=0
while spam<5:
    print('Hello World')
    spam=spam+1
print('End')
'''

#Using while, WAP to return list of sq. of elements upto 5.
'''
n=1
sq=[]
while n<6:
    sq.append(n*n)
    n+=1 #n=n+1
print(sq)
'''

# Using while, WAP to find factorial of a no.
# 5!=1x2x3x4x5=120
'''
n=int(input('Enter a no.: '))
fac=1
i=1
while i<n+1:
    fac*=i #fac=fac*i
    i+=1 #i=i+1
print(f'Factorial of {n} is {fac}.')
'''

# Assignment: Using while loop
#1) WAP to count how many times a given number can be
#divided by 2 before it is less than or equal to 1.

#2) WAP to print seperate list of even and odd natural
#number between inputed range of numbers

#3) WAP to print table in format: 2 x 3 = 6

#4) WAP to find multiples/factors of a no. n
# Eg. factors of 12 are 1,2,3,4,6,12

#5) WAP to find HCF of two no.s.
# Eg. HCF of 8,12 is 4.

#6) WAP to check whether a no. n is prime or not.

#7) WAP to return a list of all prime no. between inputed
# range of numbers

#8) WAP to check whether a 3 digit no. is Armstrong number or not.
#i.e, summation of cube of each digit is equal to no. itself.
# Eg. 371 is armstrong since (3**3+7**3+1**3)=371

#9) WAP to print fibonacci series upto n no. of terms.
# Eg. Series upto 5 terms is 0 1 1 2 3








