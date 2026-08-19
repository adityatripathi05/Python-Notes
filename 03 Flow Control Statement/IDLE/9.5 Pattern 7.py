#   *@@@@@@@*
#   *       *
#   *       *
#   *       *
#   *       *
# @@@@@   @@@@@
#  @@@     @@@
#   @       @
# Pattern must print for odd rows input only

n = int(input("Enter row: "))
if n%2:
    loop1 = loop2 = n
    print(' '*(n//2),'*','@'*(n+2),'*',sep='')
    for i in range(1, n):
        print(' '*(n//2),'*',' '*(n+2),'*',sep='')
    for j in range(1, n):
        for k in range(1, j):
            print(' ',end ='',sep='')
        for l in range(1, loop1+1):
            print('@',end='')
        loop1 = loop1-2
        for m in range(1, j):
            print(' ',end ='',sep='')
        for n in range(1, 4):
            print(' ',sep='',end='')
        for o in range(1, j):
            print(' ',end ='',sep='')
        for p in range(1, loop2+1):
            print('@',end='')
        loop2 = loop2-2
        print()
