# WAP for signup and login with 3 attemps to input
# right password if input password is wrong.

import sys
acc_detail={'aditya':'123456'}
print('1. Signup','2. Login','3. Exit', sep='\n')
ch= int(input("Enter choice no.: "))
if ch==1:
    print('-----------Signup---------')
    while True:
        name=input("Create Username: ")
        if name not in acc_detail.keys():
            pwd= input("Create Password: ")
            if len(pwd)>6:
                acc_detail[name]=pwd
                print(acc_detail)
                break
            else:
                print("Read Guidelines")
        else:
            print("Try using different username")

elif ch==2:
    print('-----------Login---------')
    name=input("Enter Username: ")
    if name in acc_detail.keys():
        attempt=1
        while attempt<4:
            pwd= input("Enter Password: ")
            if pwd==acc_detail[name]:
                print(f'Welcome {name}!')
                break
            else:
                print(f"Wrong Password,{3-attempt} attempt left")
            attempt+=1
    else:
        print("Unknown User")

elif ch==3:
    sys.exit()
else:
    print("Invalid Choice")
