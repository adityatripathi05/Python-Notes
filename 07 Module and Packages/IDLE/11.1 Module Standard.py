# Module:
'''
- Each module is a Python program that contains a related
group of functions that can be embedded in our programs.
'''

# Types of Module:
'''
There are two types of module in Python:
1) Standard Library Modules: Some of them are as follows:
math, random , threading , collections , os etc.
2) User Defined Modules
'''

# Use a module:
'''
- Before we can use the functions in a module, we must
load that module in our python code.
- Two types of statements to load a module:
    - 1) import statement:
        - Used to import all the functionality of one
        module.
        - Syntax: import module1,module2,..., module n

    - 2) from-import statement:
        - Instead of importing the whole module into the
        namespace, python provides the flexibility to
        import only the specific attributes of a module.
        - Syntax: from <module-name> import <attr1>, <attr2>..,<attr n>
'''

# Renaming a module:
'''
- We can create an alias when we import a module, by
using the 'as' keyword.
- Syntax: import <module-name> as <specific-name>
'''

# Standard Library Modules:
# sys Module:
import sys
#print(sys.__doc__)

# sys.version: displays version number of the current
# Python interpreter.
#print(sys.version)

# sys.path: A list specifies the search path for modules.
#print(sys.path)

# sys.stdout: Standard output
#sys.stdout.write('Hello')

# sys.getsizeof: Return the size of an object in bytes.
#name='Aditya'
#print(sys.getsizeof(name))

# sys.exit(): Exit from Python
#sys.exit()
#####################################################

# statistic Module:
import statistic as stat
#print(stat.__doc__)

marks=[56,78,96,78,67]

#statistics.mean(): Returns the arithmetic mean of the
# numbers in a list.
#print(stat.mean(marks))

#statistics.median(): Returns the middle value of numeric
#data in a list.
#print(stat.median(marks)) # Odd no. of elements

#statistics.mode(): Returns the most common data point in the list.
#print(stat.mode(marks))

######################################################

# os Module:
import os
#print(os.__doc__)

#getcwd(): Get current working directory
#print(os.getcwd())

# mkdir(): make directory, A new directory corresponding
# to the path, given as string argument, will be created.
os.mkdir(r'C:\Users\Aditya\Documents\Ducat Classes\Batch\temp')

# listdir(): returns the list of all files and directories in the specified directory.
#print(os.listdir(r'C:\Users\Aditya\Documents\Ducat Classes\Batch'))

#chdir(): Changing the Current Working Directory
os.chdir(r'C:\Users\Aditya\Documents\Ducat Classes\Batch\temp')
#print(os.getcwd())

#os.remove: Remove (delete) the file
'''
file=open('sample1.txt','w')
file.close()
print(os.listdir())
os.remove('sample1.txt')
print(os.listdir())
'''

#os.path.isfile(): Return True if the entry is a file
'''
file=open('sample1.txt','w')
file.close()
print(os.path.isfile('sample1.txt'))
'''

#os.path.isdir(): Return True if the entry is a directory
'''
os.mkdir('Scratch')
print(os.listdir())
print(os.path.isdir('Scratch'))
'''

#os.rename(src,dst): Rename the file or directory
'''
print(os.listdir())
os.rename('sample1.txt','new.txt')
print(os.listdir())
os.rename('Scratch','Folder')
print(os.listdir())
'''

#rmdir(): Removes the specified empty directory either
#with an absolute or relative path.
'''
print(os.listdir())
os.rmdir('Folder')
print(os.listdir())
'''
# os.rmdir(r'C:\Users\Aditya\Documents\Ducat Classes\Batch\temp')
# Error since non-empty folder

# shutil Module
#shutil.rmtree(r'C:\Users\Aditya\Documents\Ducat Classes\Batch\temp')
#print(os.listdir(r'C:\Users\Aditya\Documents\Ducat Classes\Batch')

##########################################################

# time Module:
from time import time,asctime,localtime,sleep

#time.time(): Measures the passage of time(in sec) since
#epoch time (January 1, 1970 UTC, Coordinated Universal Time)
#print(time())

#time.asctime(): Convert the Python time elapsed in seconds
#since the epoch, to a string.
#print(time.asctime())

#time.localtime(): Provide local time from the number of
#seconds elapsed since the epoch.
#print(time.localtime())

#time.sleep(n): Pause the process thread for n seconds
#print('Welcome')
#time.sleep(3)
#print('Welcome again after 3 seconds')
