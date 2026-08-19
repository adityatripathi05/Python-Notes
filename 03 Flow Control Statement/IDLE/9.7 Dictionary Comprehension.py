# Dictionary Comprehension:
'''
- Use {} instead of [] in list comprehension.
'''

# Create a dictionary of sq. no. from 1 to 10:
# Using loop
'''
sq={}
for i in range(1,11):
    sq[i]=i**2
print(sq)
'''
# Using Dictionary Comprehension:
'''
sq={i:i**2 for i in range(1,11)}
print(sq)
'''
# Using Sets Comprehension:
'''
sq={i**2 for i in range(1,11)}
print(sq)
'''

# WAP to get details of students scored more than 72
'''
record={'Navin':78,'Roshan':56,'Divya':74,'Sapna':65}
more72= {k:v for k,v in record.items() if v>72}
print(more72)
'''
'''
# Multiple variable assignment:
name,age='Aditya',75

# Tuple
data='Aditya',75

# items()
#print(record.items())

# Loop on Seq
for i,j in record.items():
    print(i,'--->',j)
'''

# WAP to assign '1st' who got more than 75 and
# '2nd' whole got less than 75 percent as value.
'''
record={'Navin':78,'Roshan':56,'Divya':74,'Sapna':65}
division={k:('1st' if v>=75 else '2nd')
          for k,v in record.items()}
print(division)
'''

# WAP to convert temp. in fahrenheit to celsius in dictionary
fahren= {'t1':-30, 't2':-20, 't3':-10, 't4':0}









