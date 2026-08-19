import common
print(common.__doc__)

print(common.name)

data1= common.is_even_odd(56)
print(data1)

data2= common.is_prime(56)
print(data2)

new_path=r'C:\Users\Aditya\Documents\My Final\Python\07 Module and Packages\IDLE\Sample Mod'
import sys
if new_path not in sys.path:
    sys.path.append(new_path)

from uncommon import is_prime
print(is_prime(19))



  
