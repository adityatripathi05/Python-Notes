#             M   
#           M   A   
#         M   A   C   
#       M   A   C   H   
#     M   A   C   H   I   
#   M   A   C   H   I   N   
# M   A   C   H   I   N   E

ip = input("Enter a string: ")
c = 2 * ( (len(ip)//2) + 1 )
for i in range(len(ip)):
    for j in range(0, c):
        print(" ", end=" ")
    for k in range(0, i+1):
        print(ip[k], " ", end=" ")
    print()
    c=c-1
