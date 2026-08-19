# Recursion:
'''
- Recursion is a method in which a function calls itself one or
more times in its body.
- If a function definition satisfies the condition of recursion,
we call this function a recursive function.
- Recursion works like loop but sometimes it makes more sense
to use recursion than loop.
We can convert any loop to recursion.

# How recursion works?
- A recursive function calls itself.
- As we would imagine such a process would repeat indefinitely
if not stopped by some condition.
This condition is known as base condition.
A base condition is must in every recursive programs otherwise
it will continue to execute forever like an infinite loop.

Step1. Recursive function is called by some external code.
Step2. If the base condition is met then the program do
something meaningful and exits.
Otherwise, function does some required processing and then
call itself to continue recursion.
'''
########################################################
# factorial:
'''
def fact(num):
    var = 1
    for i in range(num,0,-1):
        var = var * i
    return var

print(fact(5))
'''
# Through recursion:
'''
def factR(num):
    if (num==0 or num== 1): # Base condition
        return 1
    return num*factR(num-1) # Split case

print(factR(4))
'''
# Working Mechanism:
'''
factR(4)              # 1st call with 4
4 * factR(3)          # 2nd call with 3
4 * 3 * factR(2)      # 3rd call with 2
4 * 3 * 2 * factR(1)  # 4th call with 1
4 * 3 * 2 * 1         # return from 4th call as number=1
4 * 3 * 2             # return from 3rd call
4 * 6                 # return from 2nd call
24                    # return from 1st call
'''
############################################################
# Fabonacci: 0 1 1 2 3 5 8....

def fabo(num):
    pos1 = 0
    pos2 = 1
    if (num == 1):
        print(pos1)
    elif (num == 2):
        print(pos1, pos2)
    else:
        print(pos1, pos2, end=' ')
        for i in range(num-2):
            pos3 = pos1 + pos2
            pos1 = pos2
            pos2 = pos3
            print(pos3, end=' ')

n = int(input("Enter length of fabonacci: "))
fabo(n)

#### Through Recursion:
'''
def faboR(num):
    if (num==1 or num==2):
        return num-1
    return (faboR(num-2) + faboR(num-1))

for i in range(1,10):
    print(faboR(i), end=' ')
'''
############################################################
# Convert Decimal to Binary no. using recursion:
'''
def dec_bin(num):
    if (num>1):
        dec_bin(num//2)
    print(num%2, end='')

deci = int(input('Enter a decimal no.: '))
dec_bin(deci)
'''
############################################################

















    
    





        

