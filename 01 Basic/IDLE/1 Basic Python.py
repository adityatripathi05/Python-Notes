# Comments:
'''
- Comments in program are written to make program
more readable.
- These lines are ignored by the interpreter.
- Use # symbol for single line comment.
- For multiline comment use either tripple single or double
quotes at start and end of lines.
'''

# Statement:
'''
- Statements are the instructions that a python interpreter
can execute.
'''
'''
print("Hello World") # Single line statement
a=10; # Use of semicolon is optional
print(a)
b=20;print(a+b)
'''

# For multiline statement
# optn1: Use escape character i.e, \ (line continuation charcater)
'''
c=10+20\
+30+40\
+50
print(c)
'''
# optn2: Use paranthesis ()
'''
d= (10+20
+30+40)
print(d)
'''

# Tokens:
'''
- Token is the smallest unit inside the given program.
- Python breaks each logical line into a sequence of
elementary lexical components known as tokens.
- The normal token types are keywords, identifiers, 
operators, delimiters, and literals.
'''

# Keywords:
'''
- Python keywords are the reserved words in python.
- These keywords have a special meaning to python
interpreter.
- Keywords are case sensitive.
    - Keywords contain lowercase letters only.
- We cannot use keywords as regular identifiers.
'''
'''
import keyword
# keyword is python module
kw= keyword.kwlist
# kwlist is attribute of keyword module which return list
print(kw)
length= len(kw)
#len() is a builtin module function to calculate length of
# sequence
print(length)
'''

# Identifiers:
'''
- An identifier is a name used to identify a variable,
function, class, module, or other object etc.
- It helps in differentiating one entity from another.
'''
# Writing rule for Identifier:
'''
- An identifier starts with a letter (A to Z or a to z)
or an underscore (_) followed by zero or more letters,
underscores, and digits (0 to 9).
- An identifier cannot be started with a digit character.
- Case is significant in Python: lowercase and uppercase
letters are distinct.
- Python keywords are not allowed to be used as identifiers.
- Python does not allow punctuation characters such
as @, $, % etc within identifiers.
Eg.
    a=10 (Valid)
    _var=10 (valid)
    9var=10 (Invalid)
    for=10 (Invalid)
    first name='Aditya' (Invalid)
    fi@st='Aditya' (Invalid)
'''
#check= 'fi@st'.isidentifier()
#print(check)

# Literals: (Kya store karna hai)
'''
- Literals can be defined as a data that is given in a
variable or constant.
- Python support following literals:
    - 1. Numeric Literal
    - 2. String Literal
    - 3. Boolean Literal
    - 4. Special Literal. Eg. None
    - 5. Collection Literal
'''

# Variable/Ref Variable: (Kaha store karna hai)
'''
- In python variables is an entity which stores(in stack
memory) the memory address of referenced value(object)
stored inside memory(heap memory).
    - Similar to pointers in C, variables in Python r
    efer to values (or objects) stored somewhere in
    memory.
'''

# Datatype/Data Structure: (Kaise Store karna hai)
'''
- Python is a dynamically typed language hence we need
not define the type of the variable while declaring it.
The interpreter implicitly binds the value with its type
during runtime.
- Basic Datatype used by python are:
    - Numeric
    - String
    - Tuple
    - List
    - Dictionary
    - Sets
    - Array
    - Boolean
    - etc
'''
# Variable Assignment:
'''
- '=' assignment operator is used for assignment.
'''

# Single variable Assignment
'''
name='Aditya'
age=25
type1= type(name)
# type() is a builtin function to check the datatype of variable
print(type1)
print(type(age))
'''
'''
import sys
print(sys.getsizeof(name)) # Return bytes of memory consumed
print(sys.getsizeof(age))
'''
# Multiple Variable Assignment:
'''
sub, marks= 'Hindi', 45
print(sub)
print(marks)

phy=chem=76
print(phy)
print(chem)
'''

# Automatic Memory Management:
'''
sub1= 78
print(id(sub1))
# id() is a builtin module function to return memeory address
# stored by variable.
sub2= 78
print(id(sub2))

sub1= sub1+1
print(id(sub1))

sub3=78
print(id(sub3))
'''
