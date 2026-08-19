# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# Using for
'''
n = int(input('Enter number of rows: '))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=' ')        
    print()
'''
print('--------------------------------------------')
# using while
'''
n = int(input('Enter number of rows: '))
i = n
while i>0:
    j = 0
    while j<i:
        print("*",end=' ')
        j += 1
    print()
    i -= 1
'''

