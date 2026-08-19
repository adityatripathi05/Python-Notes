# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 
n = int(input('Enter number of rows: '))
for k in range(1,n+1):
    for d in range(1,k+1):
        print(k, end=' ')
    print()
