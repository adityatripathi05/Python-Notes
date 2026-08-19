# Dictionary Literal and Datatype:
'''
- Dictionary allow us to store data inform of key-value
pair.
- Dictionary is unordered, unindexed collection.
- Dictionary is delimited by curly braces {} and elements are
seperated by comma while key-value are seperated by colon
- LHS of colon is key and RHS of colon is value.
- Key must be of immutable datatype.
- Values can be of any datatype.
- All keys of dictionary must be unique.
- Dictionary is mutable.
- Dictionary is iterable.
'''

# Empty Dictionary:
data={}
#print(data, type(data), len(data))

# Non-Empty Dictionary:
detail={'roll':101,'name':'Aditya','sub':('P','C','M')}
#print(type(detail),len(detail))

# Access element of Dictionary
#print(detail['roll'])
#print(detail['sub'])

# passing a key which doesn't exist
#print(detail['age']) #KeyError

# Using get() to access value
#print(detail.get('sub')) # Since key exist return associated value
#print(detail.get('age'))
# Default value of a key which doesn't exist is 'None'.

#print(detail.get('age','Unknown Key'))
#print(detail.get('roll',0))

# Functions to access keys/value/pair:
# keys(): Return sequence of all keys of dictionary
#print(detail.keys())

# values(): Return sequence of all values of dictionary
#print(detail.values())

# items(): Return sequence of pairs as tuple of dictionary.
#print(detail.items())

# Access the pair from item() sequence:
#print(detail.items()[0]) # dict_items is not subscriptable
#print(list(detail.items())[0])

# Operations on Dictionary
# Assignment Operation:
#print(detail)
detail['roll']=102
#print(detail)

# Add a key-value pair:
#print(detail)
detail['age']=25
#print(detail)

# update(): Update Dictionary using Other Dictionary
'''
print(detail)
adhaar={'name':'Vivek','adno':12345}
detail.update(adhaar)
print(detail)
'''

# WAP to store Username and Password in Dictionary:
'''
data={}
print('----Sign up----')
name= input("Choose Username: ")
pwd= input("Choose Password: ")
if len(pwd)>=5:
    data[name]=pwd
    print('Account Created')
else:
    print('Read User Guideline')
print(data)
'''

# Membership Operator: in/not in
'''
print(detail)
print('age' in detail.keys())
print(25 in detail.values())
'''

# WAP store Username and Password in Dictionary only if
# username doesn't exist already
'''
data={'aditya':123445}
print('----Sign up----')
name= input("Choose Username: ")
if name not in data.keys():
    pwd= input("Choose Password: ")
    if len(pwd)>=5:
        data[name]=pwd
        print('Account Created')
    else:
        print('Read User Guideline')
else:
    print('Try Using different Username')
        
print(data)
'''

# WAP for Signup and Login:
'''
data={'aditya':123445}
print('Choose Option:\n1. Signup \n2.Login')
ch=int(input("Enter choice no.: "))
if ch==1:
    print('----Sign up----')
    name= input("Choose Username: ")
    if name not in data.keys():
        pwd= input("Choose Password: ")
        if len(pwd)>=5:
            data[name]=pwd
            print('Account Created')
        else:
            print('Read User Guidelines.')
    else:
        print('Try Using different Username')
elif ch==2:
    print("-------Login-------")
    name = input("Enter username: ")
    if name in data.keys():
        pwd = input("Enter password: ")
        if pwd==data[name]:
            print("Welcome, Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Unknown User")
else:
    print('Unknown Choice')
'''

# clear(): Empty the dictionary
#print(detail)
#print(detail.clear())

# pop(): It will remove the pair and also return value.
# Syntax: object.pop(key)
'''
print(detail)
temp = detail.pop('name')
print(detail)
print(temp)
'''

# popitem(): It will remove any arbitrary pair
#and also return it. It doesnot take any argument.
'''
print(detail)
temp = detail.popitem()
print(detail)
print(temp)
'''

# setdefault():
'''
- It return the value of a key, if the key is in dictionary
else it insert the key with a value in the dictionary
(Default value is None).
- Syntax: object.setdefault(key,value=None)
'''
'''
print(detail)
print(detail.setdefault('sub'))
print(detail.setdefault('perc'))
print(detail)
print(detail.setdefault('board','CBSE'))
print(detail)
print(detail.setdefault('perc','CBSE'))
print(detail)
'''

# Other Dictionary function:
# https://docs.python.org/3.8/library/stdtypes.html#mapping-types-dict










