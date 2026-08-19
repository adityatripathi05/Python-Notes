# Loop Control Statement: break, continue, pass
# break statement:
'''
- With the 'break' statement we can stop the
loop even if the decision statement is satisfied
and passes the control to the statement following
immediately after loop.
'''
'''
i = 1
while(i<6):
    if i==3:
        break
    print(i)
    i += 1
print('End')
'''
print('-----------------------------------------')
'''
for i in range(1,6):
    if i==3:
        break
    print(i)
print('End')
'''
print('-----------------------------------------')
# continue statement
'''
- With the 'continue' statement we can skip
the current itertion of loop even if the decision
statement is satisfied and passes the control for
next iteration.
'''
'''
i = 0
while(i<5):
    i += 1
    if i==3:
        continue
    print(i)
print('End')
'''
print('-----------------------------------------')
'''
for i in range(1,6):
    if i==3:
        continue
    print(i)
'''
print('-----------------------------------------')
'''
num = int(input("Enter number: "))
lis= []
for i in range(-3,3):
    if i==0:
        continue
    lis.append(num/i)
print(lis)
'''
print('-----------------------------------------')
# pass
'''
The 'pass' statement is a null operation,
nothing happens when it executes.
- Generally used in place of block statement.
'''
'''
for i in range(10):
    pass
'''
print('------------------------------------------')
'''
i = 1
while i<10:
    pass
'''
print('------------------------------------------')
'''
s = 'India'
for i in s:
    if i=='d':
        pass
'''
        
