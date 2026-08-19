# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         *

# Using for
'''
n = int(input("Enter rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(' ', end=' ')
    for k in range((n+1)-i):
        print('*', end=' ')
    print()
'''
print('--------------------------------------------')
# using while
'''
n = int(input('Enter number of rows: '))
i= 1
while (i < n+1):
    j= 1
    while (j < i):
        print(" ",end =" ")
        j = j+1
    k = 1
    while (k < (n+1)-i):
        print('*', end =' ')
        k = k+1
    print()
    i = i+1
'''



