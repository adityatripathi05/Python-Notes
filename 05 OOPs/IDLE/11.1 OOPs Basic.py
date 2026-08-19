#########
# OOPS: Object Oriented Programming Structure
'''
- It's a way to write code in more manageable format.
- It is very useful in creating real world programs.
- OOPS allow us to logically group our data and function
in a way that it is easy to reuse and also easy to
built-upon if needed.
- OOPS deals with declaring classes, creating objects
from them and interacting with the users.
'''

#########
# class:
'''
- Blueprint(prototype) for creating object.
- class defines a set of attributes(variable) and
methods(function) that characterizes any object of the class.
- In python, class is defined using 'class' keyword
followed by class name.
- Attributes and methods are accessed via dot notation.
'''
# Create Employee class with no attribute:
'''
class Employee:
    'Define an Employee class' # Doc-String
    pass
'''
print(Employee)
print(type(Employee))

# i.e, A class creates a new type where objects are
# instances of the class.

# Check attribute associated with class:
'''
- __dict__:
    - It provides the dictionary containing the
    information about the class namespace.

- __doc__:
    - It contains a string which has the class
    documentation.

- __name__:
    - It is used to access the class name.

- __module__:
    - It is used to access the module in which, this
    class is defined.

- __bases__:
    - It contains a tuple including all base classes.

- vars():
    - This function displays the attribute of an instance
    in the form of an dictionary.
    
- dir():
    - This function displays more attributes than vars(),
    as it is not limited to instance.
    - It displays the class attributes as well.
'''
#print(Employee.__doc__) # Read doc-string
#print(Employee.__dict__) #return dictionary of attr.
#print(vars(Employee)) #return dictionary of attr.
#print(dir(Employee)) # return list with detailed info.

##########
# object:
'''
- Every thing in python is object.
- object is real life entity of a class.
- An object is a unique instance of a data structure
that is defined by its class.
- Object is simply a collection of member data and
methods (functions) that act on those data.
- Process of creating instance of class is called
instantiation.
'''
# Create objects of Employee class:
#emp_1 = Employee()
#print(emp_1, type(emp_1))

#emp_2 = Employee()
#print(emp_2, type(emp_2)))

#print(dir(emp_1))

'''
- We haven't declared any members in Employee,
so where is the list coming from?
- This is because every class we create in Python
implicitly derives from class 'object'.
'''

#########
# Member Variable:
'''
- Variable that holds the data associated with a class
and its objects is called member variable.
- There are two types of member variables:
    - 1. instance Variable
    - 2. class Variable
'''

#########
# Instance Variable:
'''
- Variable contain data which are unique to each instance
of class.
- A instance variable defined inside a method, belongs
only to the current instance of a class.
'''

# Create and Assign attributes of object:
# Syntax: object.attribute=data
'''
emp_1.name = 'Jackie Chan'
emp_1.monthly= 18000
emp_1.post='Clerk'

emp_2.name = 'Bruce Lee'
emp_2.monthly= 22000
emp_2.post='Manager'
'''

# Check data associated with object of class:
#print(dir(emp_1))
#print(emp_1.__dict__)
#print(vars(emp_2))

'''
- i.e, Each instance have attributes that are unique to
that instance.
- Ideally we set all of this information for each user
automatically using 'constructor', instead of setting these
values manually.
'''

##########
# Constructor:
'''
- Constructor provide initial parameter to the object of
class.
- Constructor are of two types
    - Default constructor,
    - Parameterised constructor.
- In python, constructor is created using __init__().
- __init__() is automatically called during the process of
instantiation.
'''

# Default constructor:
'''
class Employee:
    def __init__(self):
        print("Constuctor invoked")

emp_1=Employee() #constructor get automatically called
emp_2=Employee()        
'''

# self:
'''
- 'self' parameter is a reference to the current instance
of class.
- By convention it is named as 'self'.
'''

# Create Parametrised constructor:
class Employee:
    def __init__(self, n, m, p):
        self.name = n
        self.monthly = m
        self.post = p
        
# Create objects of Employee class:
#emp_1 = Employee('Jackie Chan',18000,'Clerk')
#print(vars(emp_1))
#emp_2 = Employee('Bruce Lee',22000,'Manager')
#print(vars(emp_2))

# Access and Modify data associated with object:
# Get attribute of object:
#print(emp_1.name) #emp_1.__dict__[name]

# Set attribute of object:
#emp_1.name='Adarsh'
#print('Renamed')
#print(emp_1.name)
#print(emp_1.__dict__)

# Delete attribute of object:
#del emp_1.name
#print('name attribute deleted')
#print(emp_1.__dict__)

#########
# Builtin function to access and modify data associated
# with object:
'''
- getattr(obj,name,default):
    - It is used to access the attribute of the object.
    - Default argument is returned when the attribute
    doesn't exist.

- setattr(obj,name,value):
    - It is used to set a particular value to the specific
    attribute of an object.

- delattr(obj,name):
    - It is used to delete a specific attribute.

- hasattr(obj,name):
    - It returns true if the object contains some specific
    attribute.
'''
#print(getattr(emp_1,'name'))
#print(getattr(emp_1,'age','missing attribute'))
#print(getattr(emp_1,'age',None))
#print(getattr(emp_1,'name',None))

#print(hasattr(emp_1,'name'))
#print(hasattr(emp_1,'age'))

#print(vars(emp_1))
#setattr(emp_1,'name','Adarsh')
#print(vars(emp_1))

#delattr(emp_1,'name')
#print(hasattr(emp_1,'name'))

#########
# Method:
'''
- Function defined within a class is called Method.
- There can be 3 types of methods defined python class:
    - instance method
    - class method
    - static method
'''

#########
# Instance Method:
'''
- Instance method are methods which require an object of
its class to be created before it can be called.
- The first parameter of instance method must be object
itself i.e, 'self' parameter.
'''
#
'''
marks=[10,20,30] # marks=list((10,20,30))
marks.append(10)
print(marks)

name=list(('A','B','C'))
list.append(name,'D')
print(name)
'''

# Create instance method 'annual':
'''
class Employee:
    def __init__(self,name,monthly,post):
        self.name = name
        self.monthly = monthly
        self.post = post
        self.salary = 0
        
    def annual(self):
        self.salary = self.monthly*12

    def display(self):
        return f'{self.name} has CTC of Rs.{self.salary}'
            
#print(Employee.__dict__)

emp_1=Employee('Aditya',12000,'Clerk')
Employee.annual(emp_1) # Accessing instance method using class name
print(Employee.display(emp_1))

emp_2=Employee('Yash',21000,'Manager')
emp_2.annual() # Accessing instance method using instance name=> More appropriate
print(emp_2.display())
'''

# Create instance method to get and set 'salary' attribute:
'''
class Employee:
    def __init__(self,name,monthly,post):
        self.name = name
        self.monthly = monthly
        self.post = post
        
    def getMonthly(self):
        return f'{self.name} salary is Rs.{self.monthly}pm'
        
    def setMonthly(self,value):
        if self.post=='Manager':
            print('New pm salary is set to',value)
            self.monthly= value
        else:
            print('Access Restricted')
            
emp_1 = Employee('Jackie Chan',18000,'Clerk')
print(emp_1.getMonthly())
emp_1.setMonthly(20000)
print(emp_1.getMonthly())

#But,
print(emp_1.monthly)
emp_1.monthly=50000
print(emp_1.monthly)

setattr(emp_1,'monthly',56000)
print(getattr(emp_1,'monthly'))
'''
#Can't regulate the access and modification of 'name' everytime.

##########
# Inheritance:
'''
- Inheritance is a concept that models a 'is a'
relationship between classes.
- Inheritance enable us to define a class(child) that
takes(inherits) attributes and methods from another(parent
) class and allows us to add more.
- It provides code reusability.
- Inheritance are of different types:
    - Single Level Inheritance
    - Hierarchial Inherictance
    - Multilevel Inheritance
    - Multiple Inheritance
    - Hybrid Inheritance
'''

###########
# Single Level Inheritance:
'''
- Syntax:
class Base:
    pass
    
class Derived(Base):
    pass
'''

# Create a class 'Polygon'
class Polygon:
    def __init__(self,no_of_sides):
        self.n= no_of_sides
        self.sides=[0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides=[float(input(f'Enter dim of side {i+1}: ')) for i in range(self.n)]

rect=Polygon(4)
#print(rect.n)
#print(rect.sides)
#rect.inputSides()
#print(rect.sides)

# Create a class Triangle:
'''
class Triangle:
    def __init__(self):
        self.n=3
        self.sides=[0 for i in range(self.n)]
    def inputSides(self):
        self.sides=[float(input(f'Enter dim of side {i+1}: ')) for i in range(self.n)]
    def perimeter(self):
        a,b,c=self.sides
        peri=3*a
        return f'Perimeter is {peri}cm'
equi=Triangle()
print(equi.n)
print(equi.sides)
equi.inputSides()
print(equi.sides)
print(equi.perimeter())
'''

# Create Inherited class Triangle from Polygon:
class Triangle(Polygon): #Triangle 'is a' Polygon
    def __init__(self):
        #polygon.__init__(self,3)
        super().__init__(3)
    def perimeter(self):
        a,b,c=self.sides
        peri=3*a
        return f'Perimeter is {peri}cm'
    
equi=Triangle()
#print(equi.n) # Parent Member
#print(equi.sides) # Parent Member
#equi.inputSides() # Parent Member
#print(equi.sides)
#print(equi.perimeter())

##########
# Builtin functions to find relationships:
# isinstance(obj,class):
'''
- Checks the relationship between the objects and classes.
    - Returns True if the obj is an instance of the
    class or other classes derived from it.
- Each and every class in Python inherits from the base
class object.
'''
#print(isinstance(rect,Polygon))
#print(isinstance(equi,Triangle))
#print(isinstance(equi,Polygon))
#print(isinstance(rect,Triangle))
#print(isinstance(equi,object))
#print(isinstance(rect,object))

# issubclass(first,second):
'''
- Checks the relationships between the specified classes.
- Returns True if the first class is the subclass of
the second class, and False otherwise.
- Each and every class in Python inherits from the base
class object.
'''
#print(issubclass(Triangle,Polygon))
#print(issubclass(Polygon,Triangle))
#print(issubclass(Polygon,object))
#print(issubclass(Triangle,object))

###########
# Data Encapsulation:
'''
- Data encapsulation describes the idea of wrapping data
and the methods(that work on data) within one unit.
- This puts restrictions on accessing variables and
methods directly and can prevent the accidental
modification of data.
'''

# Access Modifiers:
'''
- Access modifiers puts restrictions on accessing
variables and methods directly.
- Python doesn't have any mechanism that effectively
restricts access of attributes.
- Types of Access Modifiers:
    - Public
    - Protected
    - Private 
'''

########
# Public Members:
'''
- Public members are accessible within class, in subclass
and also outside the class.
- All members in a Python class are public by default.
'''
'''
class A:
    def __init__(self,n):
        self.var=n # public variable
    def sq(self): # public method
        return self.var**2
    def cube(self):
        return self.sq()*self.var

obj=A(2)
print(obj.var) # access
obj.var=7 # modify
print(obj.sq())
'''

##########
# Protected Member:
'''
- Protected members are accessible within class, in
subclass and but not outside the class.
- To accomplish this in Python, just follow the convention
by prefixing the name of the member by a single underscore
`_`.
'''
# Create a Protected Member class:
'''
class A:
    def __init__(self,n):
        self._var=n # protected variable
    def _sq(self): # protected method
        return self._var**2
    def cube(self):
        return self._sq()*self._var
obj1=A(2)    
#print(obj1.var) #Access Denied
#print(obj1.sq()) #Access Denied
#print(obj1.cube())

class B(A):
    def perimeter(self):
        return 4*self._var
    def area(self):
        return self._sq()

obj2=B(2)
#print(obj2.perimeter())
#print(obj2.area())
'''

###########
# Private Members:
'''
- Private members are accessible only within class
but neither in subclass nor outside the class.
- To define a private member, prefix the member name
with double underscore `__`.
'''
# Create a Private Member Class:
'''
class A:
    def __init__(self,n):
        self.__var=n # private variable
    def __sq(self): # private method
        return self.__var**2
    def cube(self):
        return self.__sq()*self.__var
obj1=A(2)    
#print(obj1.var) #Access Denied
#print(obj1.sq()) #Access Denied
#print(obj1.cube())

class B(A):
    def perimeter(self):
        return 4*self.__var
    def area(self):
        return self.__sq()

obj2=B(2)
#print(obj2.perimeter()) #Access Denied
#print(obj2.area()) #Access Denied
'''

#########
# Modifying the access and modification of 'salary' attribute.
'''
- Make salary protected attribute.
- Create getter, setter, and deleter methods inside
class for salary.
'''
'''
class Employee:
    def __init__(self,name,monthly,post):
        self.name = name
        self._monthly = monthly
        self.post = post
        
    def getMonthly(self):
        return f'{self.name} salary is Rs.{self._monthly}pm'
        
    def setMonthly(self,value):
        if self.post=='Manager':
            print('New pm salary is set to',value)
            self._monthly= value
        else:
            print('Access Restricted')

    def delMonthly(self):
        if self.post=='Manager':
            print('Deleting salary attribute')
            del self._monthly
        else:
            print('Access Restricted')
            
emp_1 = Employee('Jackie Chan',18000,'Clerk')
print(emp_1.getMonthly())
emp_1.setMonthly(20000)
print(emp_1.getMonthly())

# Restricted access through these methods
# print(emp_1.monthly) # Access Denied
# emp_1.monthly=50000 #Inappropriate Operation
# print(vars(emp_1))

# setattr(emp_1,'monthly',56000) #Inappropriate Operation
# print(vars(emp_1))
# print(getattr(emp_1,'monthly')) # Access Denied
'''

#NOTE:
'''
- Our new update was not backward compatible:
- The big problem with the above update is that, all the
clients who implemented our previous class in their
program have to modify their code:
    - from `obj.monthly` to `obj.getMonthly()` and 
    - all assignments like `obj.monthly = val` to
    `obj.setMonthly(val)`
- This is where builtin property() comes to rescue.
'''

#########
# Method as property:
'''
- The property() method in Python provides an interface
to instance attributes.
- property() returns the property attribute from the given
getter, setter, and deleter.
- Syntax: property(fget=None, fset=None, fdel=None, doc=None)
'''
#Create class with getter, setter, and deleter methods as property
'''
class Employee:
    def __init__(self,name,monthly,post):
        self.name = name
        self._monthly = monthly
        self.post = post
        
    def getMonthly(self):
        return f'{self.name} salary is Rs.{self._monthly}pm'
        
    def setMonthly(self,value):
        if self.post=='Manager':
            print('New pm salary is set to',value)
            self._monthly= value
        else:
            print('Access Restricted')

    def delMonthly(self):
        if self.post=='Manager':
            print('Deleting salary attribute')
            del self._monthly
        else:
            print('Access Restricted')
        
    # Set property
    monthly = property(getMonthly,setMonthly,
                        delMonthly,'monthly property')
    
emp_1 = Employee('Jackie Chan',18000,'Clerk')
print(emp_1.monthly)
emp_1.monthly=50000
print(vars(emp_1))

setattr(emp_1,'monthly',56000)
print(vars(emp_1))
print(getattr(emp_1,'monthly'))
'''

# Using @property decorator
'''
- Instead of using property(), we can use the Python
decorator @property to assign the getter, setter, and
deleter.
'''
'''
class Employee:
    def __init__(self,name,monthly,post):
        self.name = name
        self._monthly = monthly
        self.post = post
    @property    
    def monthly(self):
        return f'{self.name} salary is Rs.{self._monthly}pm'
    @monthly.setter    
    def monthly(self,value):
        if self.post=='Manager':
            print('New pm salary is set to',value)
            self._monthly= value
        else:
            print('Access Restricted')
    @monthly.deleter
    def monthly(self):
        if self.post=='Manager':
            print('Deleting salary attribute')
            del self._monthly
        else:
            print('Access Restricted')
            
emp_1 = Employee('Jackie Chan',18000,'Clerk')
print(emp_1.monthly)
emp_1.monthly=50000
print(vars(emp_1))

setattr(emp_1,'monthly',56000)
print(vars(emp_1))
print(getattr(emp_1,'monthly'))
'''

#########
# class variable:
'''
- Variable that belong to the class itself and is shared
by all instances of a class. 
- class variables are defined within a class but outside
any of the classes methods.
- Changing class variable using the class name will be
reflected for all the instances of a class.
- Changing the class variable using the instance will
not reflect elsewhere. It will affect only that
particular instance.
'''
# create class variable 'increment' of Employee class
'''
class Employee:
    increment=1.08 #class variable
    def __init__(self,n,m):
        self.name=n
        self.monthly=m

    def annual(self):
        self.salary= self.monthly*12

    def pay_raise(self):
        self.salary=self.salary*self.increment

    def display(self):
        print(f'{self.name} has Rs.{self.salary} CTC')

#print(Employee.__dict__)
Employee.increment=1.15 #modifying class variable using class name
#print(Employee.__dict__)
emp_1= Employee('Yogesh',18000)
emp_1.annual()
emp_1.display()
emp_1.pay_raise()
emp_1.display()

emp_2= Employee('Satish',18000)
emp_2.annual()
emp_2.display()
emp_2.pay_raise()
emp_2.display()
print(emp_2.__dict__)

emp_3= Employee('Adarsh',18000)
emp_3.increment=1.50 #modifying class variable using instance name
emp_3.annual()
emp_3.display()
emp_3.pay_raise()
emp_3.display()
print(emp_3.__dict__)
'''

# NOTE:
'''
- If we try to change class variable via instance name,
a new instance (or non-static) variable for that particular
object is created and this variable shadows the class
variables.
'''

############
# class method:
'''
- A class method is bound to the class and not the object
of the class.
- Builtin function classmethod() or decorator @classmethod
can be applied on any method of a class.
- This decorator will allow us to call that method using
the class name instead of the object.

- First argument of class method is class itself,
named as 'cls' by convention.
- They have the access to the state of the class.
- It can modify a class state that would apply across
all the instances of the class.
'''
# Need
'''
class Employee:
    def __init__(self,n,m):
        self.name=n
        self.monthly=m
    
emp_1=Employee('Yogesh',18000)
print(emp_1.name)
emp_2=Employee('Satish',21000)
print(emp_2.name)

# Suppose data is read from database or csv file
data1='Adarsh,25000'
data2='Aditya,15000'

d1n,d1m= data1.split(',')#==>['Adarsh',25000]
emp_3=Employee(d1n,d1m)
print(emp_3.name)

d2n,d2m= data2.split(',')#==>['Aditya',15000]
emp_4=Employee(d2n,d2m)
print(emp_4.name)
'''

# create classmethod 'ipdata'
'''
class Employee:
    def __init__(self,n,m):
        self.name=n
        self.monthly=m
        
    @classmethod
    def ipdata(cls,data): # classmethod as alternative constructor
        dn,dm=data.split(',')
        return cls(dn,dm)

data1='Adarsh,25000'
data2='Aditya,15000'

emp_1= Employee.ipdata(data1)
print(emp_1.name)

emp_2= Employee.ipdata(data2)
print(emp_2.name)

emp_3=Employee('Yogesh',18000)
print(emp_3.name)
'''

##########
# static method:
'''
- It is a method which is part of a class definition,
but is not part of the objects of class.
- static method is defined using builtin function
staticmethod() or using decorator @staticmethod.
- A static method needs no specific 1st parameters.
- A static method can’t access or modify class state.
- These methods are used to do some utility tasks by
taking some parameters.
'''
#create staticmethod 'isWorkDay'
'''
from datetime import date
class Employee:
    def __init__(self,n,m):
        self.name=name
        self.monthly=monthly

    @staticmethod
    def isWorkDay(day):
        if (day.weekday()==5 or day.weekday()==6): # for sat,sun
            return False
        return True

d=date(2020,4,14)
print(Employee.isWorkDay(d))

emp_1= Employee('Bruce Lee',18000)
print(emp_1.isWorkDay(d))
'''

'''
- A static method doesn't receive any reference argument
whether it is called by an instance of a class or by the
class itself.
'''

