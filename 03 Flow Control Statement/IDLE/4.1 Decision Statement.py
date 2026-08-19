# Flow Control Statement:
'''
- We'll control the flow of execution. Can be done by:
- 1. Decision Statement:
    - 1.1 if statement
    - 1.2 if-else statement
    - 1.3 if-elif-else statement
- 2. Loop Statement:
    - 2.1 while loop statement
    - 2.2 for loop statement
- 3. Loop Control Statement:
    - 3.1 break statement
    - 3.2 continue statement
'''

# Decision Statement:
'''
print('----Signup-----')
name= input("Choose Username: ")
pwd= input("Choose Password: ")
print('Credentials stored')
print('Account Created')
print('Thankyou')
'''

# 'if' statement:
'''
- An 'if' statement's clause(block following the if statement)
will execute if the statement's condition is True.
- The clause is skipped if the condition is False.
'''
# Condition: Store credentials on when the pwd length is
# greater than or equal to 5.
'''
print('----Signup-----')
name= input("Choose Username: ")
pwd= input("Choose Password: ")
if len(pwd)>=5:
    print('Credentials stored')
    print('Account Created')
print('Thankyou')
'''

# whitespace is called indentation and is used to define
# block statement or block of code.

# if-else statement:
'''
- An 'if' clause can optionally be followed by an 'else'
statement.
- The 'else' clause will execute only when the 'if' statement
condition is False.
'''
'''
print('----Signup-----')
name= input("Choose Username: ")
pwd= input("Choose Password: ")
if len(pwd)>=5:
    print('Credentials stored')
    print('Account Created')
else:
    print('Check User Guideline')
print('Thankyou')
'''

# if-elif-else statement:
'''
- While only one of the if or else clauses will execute,
we may have cases where we want one of many possible
clauses to execute. For that we use 'elif' statement.
- The 'elif' statement is an 'else if' statement that always
follows an 'if' statement.
- It provides another condition that is checked only 'if'
all of the previous conditions are False.
- We can have multiple 'elif' statement.
'''

# WAP to get greatest of 3 no.
# a,b,c
# a---> a>b and a>c
# b---> b>a and b>c
# c---> c>a and c>b
'''
a= int(input("Enter 1st: "))
b= int(input("Enter 2nd: "))
c= int(input("Enter 3rd: "))
if a>b and a>c:
    print(a,'is greatest')
elif b>a and b>c:
    print(b,'is greatest')
else:
    print(c,'is greatest')
'''

# Nested decision statements:
# WAP to check whether a number is even and
# divisible by 5:
'''
n = int(input("number: "))
if n%2==0:
    if n%5==0:
        print(f"{n} is even and divisible by 5")
    else:
        print(f'{n} is even but not divisible by 5')
else:
    print(f"{n} is not my required no.")
print("Found")



