# WAP to check whether a no. is even or odd
'''
n= int(input("Enter a no.: "))
if n%2==0:
    print(n,'is even')
else:
    print(n,'is odd')
'''

# WAP to check for leap year
'''
- In the Gregorian calendar three criteria must be taken
into account to identify leap years:
- The year can be evenly divided by 4, is a leap year,
unless:
    - The year can be evenly divided by 100, it is NOT a
    leap year, unless:
        - The year is also evenly divisible by 400.
        Then it is a leap year.

- This means that in the Gregorian calendar, the years
2000 and 2400 are leap years, while 1800, 1900, 2100,
2200, 2300 and 2500 are NOT leap years.
'''
'''
yr= int(input('Enter your year: '))
if (yr % 4 == 0): # evenly divided by 4 is leap unless
    if (yr % 100 == 0): # evenly divided by 100 is leap unless
        if (yr % 400 == 0): # evenly divided by 400 also 
            print(f'{yr} is a leap year')
        else: # not evenly divided by 100 is not leap
            print('% d is a non leap year' %yr)
    else: # is a leap if not evenly divided by 100
        print(yr, ' is a leap year')
else:
    print('{} is a non leap year'.format(yr))
'''

