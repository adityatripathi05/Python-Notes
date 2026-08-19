# Access element of a sequence one-by-one
'''
num=[33,56,77,78,56]
#list,tuple,string,dictionary,sets etc are all iterable objects.
#print(dir(num))
#dir() is a builtins module function, returns an object’s attributes.

next_num=iter(num)
#An iterable object have a method iter(), which converts
# an iterable object into iterator object.

#print(dir(next_num))
print(next(next_num))
#An iterator object have a method next(), with the
#help of which we can access elements of iterator object
#one-by-one.
print(next(next_num))
print(next(next_num))
print(next(next_num))
print(next(next_num))
#print(next(next_num)) # Raise StopIteration Error
'''

# 'for' loop is an easy implementation to access elements
# of sequence one-by-one
'''
num=[33,56,77,78,56]
even=[]
for i in num:
    if i%2==0:
        even.append(i)
print(even)
'''

# Sequence as tuple:
'''
num=(33,56,77,78,56)
even=[]
for i in num:
    if i%2==0:
        even.append(i)
print(even)
'''

# Sequence as string:
'''
text='MaChInE'
for ch in text:
    print(ch)
'''

# Count no. of vowels in a string
'''
text=input("Enter a string: ")
vowels='aeiou'
count=0
for char in text.lower():
    if char in vowels:
        count+=1
print(count)
'''

# Sequence as dictionary:
data= {'t1':-30,'t2':-20,'t3':-10,'t4':0} # temp in Fahrenheit
'''
for i in data:
    print(i)
'''
# seq of keys:
'''
for i in data.keys():
    print(i)
'''

# seq of values:
'''
for i in data.values():
    print(i)
'''

# seq of pair:
'''
for i in data.items():
    print(i)
'''

# multiple variable assignment
'''
name,age='Aditya',25
print(name)
print(age)
'''
# tuple:
'''
multi='Aditya',25
print(multi)
'''

# placing multiple loop variable
'''
for i,j in data.items():
    print(i,'-->',j)
'''

# Convert Fahrenheit temp. to Celcius and return as dictionary
'''
print(data)
celcius={}
for k,v in data.items():
    celcius[k]= round((v-32)*(5/9),2)
    
print(celcius)
'''

#range():
'''
- range() is a builtins module function.
- It generates a sequence of Integer.
- Syntax: range(start,stop,step)
    - start,step are optional, with default value 0, 1 respectively.
    - stop is mendatory and is exclusive in sequence.
- range() return range object.
- range object is an iterable object.
'''
# sequence upto 10
'''
seq=range(11)
print(seq)
print(list(seq))
'''

# sequence from 3 to 10
'''
seq= range(3,11)
print(list(seq))
'''

# sequence from 3 to 15 with step 2
'''
seq= range(3,16,2)
print(list(seq))
'''

# sequence from -3 to 3 with step 1
'''
seq= range(-3,4)
print(list(seq))
'''

# sequence from 3 to -3 with step -1
'''
seq= range(3,-4,-1)
print(list(seq))
'''

# Print table of n in format 2x3=6
'''
n= int(input("Enter a no.: "))
for i in range(1,11):
    print(f'{n}x{i}={n*i}')
'''

# Assignment: Using for loop
#1) WAP to count how many times a given number can be
#divided by 2 before it is less than or equal to 1.

#2) WAP to print seperate list of even and odd natural
#number between inputed range of numbers

#3) WAP to find factorial of a no. n
# Eg. 5!=120

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

#10) WAP which take a number from user and calculate its
# sum of digits



