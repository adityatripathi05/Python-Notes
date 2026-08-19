# File:
'''
- File is a named location on disk to store related
information. 
- It is used to permanently store data in a non-volatile
memory. (e.g. hard disk).
'''

# File Handling:
'''
- In file handling, we perform Read and Write operation
on various types of file.
- File can be of any type. Some of which are
    - text file: To record text information
    - csv file: To record tabular data
    - json file
    - excel file
'''

# Steps in File Handling:
'''
1. Create/Open a file
2. Operation to Write on a file/Read from a file
3. Close the file
'''

# open():
'''
- It is a builtin function to Create/Open a file.
- Syntax: open(src path,mode='r')
- Mode: Available format to operate on file:
    'r'-read(default)|'rt'-read text|
    'w'-write|'wt'-write text|
    'rb'-read binary|'wb'-write binary|
    'r+'- read and write|'w+'-write and read
    'a'- write append| 'a+'- append and read
    'x'- write absolute| 'x+'- absolute and read
- open() return file object.
'''

# Descripter:
'''
- 'name', 'mode', 'closed' are data descripter to check
properties of file.
'''

#########
# Write on Text File: 'w'|'a'|'x'
# write():
'''
- This function perform write operation on file.
- It takes string as an argument.
'''

# Writing on file in simple 'w' mode:
'''
- 'w' general mode for writing on any file.
- 'wt' for writing on text format file only
- In 'w' mode if file doesn't exist already then first
it will create file then open it.
- But if file exist then the new content will overwrite
on the previously written data.
'''
'''
file=open('msg.txt','w')
print(file.name,'file is Open in', file.mode)
file.write('This is line 1.')
file.write('This is line 2.')
print('Written on file')
print(file.closed)
file.close() # must during write mode
print(file.closed)
'''

# overwriting:
'''
obj=open('msg.txt','w')
print(obj.name,'file is Open in', obj.mode)
obj.write('This is python.\n')
obj.write('This is Java.')
obj.write('\n')
print('Written on file')
print(obj.closed)
obj.close()
print(obj.closed)
'''

# Writing on file in append mode:
'''
- To avoid overwriting on previously written data, we use
append mode.
- 'a' for writing on file in append mode
- 'at' for writing on text format file only in append mode
- In 'a' mode if file doesn't exist already then first
it will create file then open it.
- But if file exist then the new content will be written
after the previously written data.
'''
'''
file=open('msg.txt','a')
print(file.name,'file is Open in', file.mode)
file.write('This is C.\n')
file.write('This is C++.')
file.write('\n')
print('Written on file')
file.close()
'''

# Writing on file in absolute mode:
'''
- 'x' for writing on file in absolute mode.
- 'xt' for writing on text format file only in absolute mode.
- In 'x' mode if file doesn't exist already then first
it will create file then open it.
- But if file exist will give FileExistError.
'''
'''
file=open('msg.txt','x')
print(file.name,'file is Open in', file.mode)
file.write('This is PHP.\n')
file.write('This is Excel.')
file.write('\n')
print('Written on file')
file.close()
'''

# File Handling using 'with' block:
'''
- Since in writing mode it is important to close file.
- To avoid any error we can use 'with' block then we do
not need to close the file explicitely.
'''
'''
with open('msg.txt','a') as file:
    print(file.name,'file is Open in', file.mode)
    file.write('This is PHP.\n')
    file.write('This is Excel.')
    file.write('\n')
    print('Written on file')
print(file.closed)
'''

# Read from Text File: 'r'
'''
- File need to exist before we read, otherwise throws error.
'''

# read(value):
'''
- This function will read data character by character from
cursor current position upto specified index or end
of file.
- It return the read data as a string.
'''
'''
file= open('msg.txt','r')
print(file.name,'file is Open in', file.mode)
print(file.read())
file.close()
'''

# store read data
'''
with open('msg.txt') as file:
    print(file.name,'file is Open in', file.mode)
    data= file.read()

print(data)
print(data.title())
'''

# seek() and tell()
'''
- seek(index) is used to place the cursor at specified
index.
- tell() return the current index of cursor.
'''

# read() with value
'''
with open('msg.txt') as file:
    print(file.name,'file is Open in', file.mode)
    print(file.tell())
    data= file.read(5)
    print(data)
    print(file.tell())
    data2= file.read(9)
    print(data2)
    print(file.tell())
'''

# readline(value):
'''
- This function will read text line by line from cursor
current position upto the specified index or to the end
of line.
- It will return string.
'''
'''
with open('msg.txt') as file:
    print(file.name,'file is Open in', file.mode)
    data= file.readline()
    print(data)
    data2= file.readline()
    print(data2)
    # read from starting again
    file.seek(0)
    data3=file.readline()
    print(data3)
'''

# If index is specified
'''
with open('msg.txt') as file:
    print(file.name,'file is Open in', file.mode)
    data= file.readline(4)
    print(data)
    data2= file.readline()
    print(data2)
'''

# readlines()
'''
- This function will read all lines from file at once.
- It return the lines as list. Each line of text will be
the element of list.
'''
'''
with open('msg.txt') as file:
    print(file.name,'file is Open in', file.mode)
    data= file.readlines()
print(data)
'''

# How many no. of characters present in text file?
'''
with open('msg.txt') as file:
    data= file.read()
noOfChar= len(data)
print(noOfChar)
'''

# How many no. of words present in text file?
'''
with open('msg.txt') as file:
    data= file.read()
words= data.split(' ')
print(words)
noOfWords= len(words)
print(noOfWords)
'''

# How many no. of lines present in text file?
'''
with open('msg.txt') as file:
    data= file.readlines()
print(len(data))
'''

# WAP to write some string on a file and the
# display all odd unicode characters read from that file.
print(ord('a')) # Return unicode value of a character
print(chr(65)) # Return character of a unicode value


