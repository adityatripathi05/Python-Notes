##########
# OOPs Features:
'''
- Polymorphism
- Encapsulation
- Abstraction
- Inheritance
'''

##########
# Polymorphism: poly-many | morph-forms
'''
- Polymorphism means the ability to take various forms.
- In Python, Polymorphism allows an object to come in
many forms.
- To achieve polymorphism:
    - 1) Method Overloading: Here methods have same name
    but have different signature (parameters).
        - It is not possible in Python.
    - 2) Method Overriding: Here method in base class and
    derived class have same name but different
    functionality.
'''

#############
# Method Overloading:
'''
class Maths:
    def add(self,x,y):
        return x+y

    def add(self,x,y,z):
        return x+y+z

m=Maths()
print(m.add(2,3,4))
print(m.add(2,3)) # Error
'''

############
# Operator Overloading:
'''
- It enables us to use mathematical, logical and bitwise
operators on python objects just like any primitive data
type.
'''
# __ methods are known as magic method.

# Create a class to perform '+' operator overloading for
# 2D-coordinates. Ex. (2,3) & (4,5)==> (6,8)
'''
class Coordinate:
    def __init__(self,n1,n2):
        self.x=n1
        self.y=n2

c1= Coordinate(2,3)
print(c1)
print(type(c1))
'''
# Better representation of object
'''
class Coordinate:
    def __init__(self,n1,n2):
        self.x=n1
        self.y=n2
    def __str__(self):
        return f'({self.x},{self.y})'
    
c1= Coordinate(2,3)
print(c1)
'''

# Adding two coordinates
'''
class Coordinate:
    def __init__(self,n1,n2):
        self.x=n1
        self.y=n2
        
    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __add__(self, other): # Equivalent to +
        x= self.x+other.x
        y= self.y+other.y
        return Coordinate(x,y)
    
c1= Coordinate(2,3)
print(c1)
c2= Coordinate(4,5)
print(c2)
c3= c1+c2 #c1.__add__(c2)
print(c3)
'''

# Relational '>' Operators Overloading
# Create a class to perform '>' operator overloading for
# 2D-coordinates. Ex. (2,3) > (4,5)==> False
'''
class GridPoint:  
    def __init__(self,n1,n2):  
        self.x=n1  
        self.y=n2  
  
    def __gt__(self, other):
        self_mag = (self.x**2) + (self.y**2) #compare the magnitude of these points from the origin
        other_mag = (other.x**2) + (other.y**2)
        return self_mag > other_mag
  
    def __str__(self):
        return f'({self.x},{self.y})'

c1 = GridPoint(3, 5)  
c2 = GridPoint(-1, 4)  
if c1 > c2:
    print('point1 is greater than point2')  
else:  
    print('point1 is not greater than point2')
'''

##############
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

#############
# Single Level Inheritance:
'''
- Syntax:
class Base:
    pass
class Derived(Base):
    pass
'''
# Define a class Polygon

class Polygon:
    def __init__(self,no_of_sides):
        self.n= no_of_sides
        self.sides=[0 for i in range(self.n)]

    def inputSides(self):
        self.sides=[float(input(f"Enter dim of side{i+1}: ")) for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n):
            print(f'Dimension of side {i+1} is {self.sides[i]}cm')

rectangle=Polygon(4)
#print(rectangle.n)
#print(rectangle.sides)
#rectangle.inputSides()
#rectangle.displaySides()

# Create a Triangle class
'''
class Triangle:
    def __init__(self):
        self.n=3
        self.sides=[0 for i in range(self.n)]

    def inputSides(self):
        self.sides=[float(input(f"Enter dim of side{i+1}: ")) for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n):
            print(f'Dimension of side {i+1} is {self.sides[i]}cm')

    def perimeter(self):
        a,b,c=self.sides
        peri= a+b+c
        return f'Perimeter is {peri}cm'

equi= Triangle()
print(equi.n)
print(equi.sides)
equi.inputSides()
equi.displaySides()
print(equi.perimeter())
'''

# Better approach will be to Inherit Polygon class inside Triangle class

class Triangle(Polygon): #Triangle 'is a' Polygon
    def __init__(self):
        Polygon.__init__(self,3)
    
    def perimeter(self):
        a,b,c=self.sides
        peri= a+b+c
        return f'Perimeter is {peri}cm'

equi= Triangle()
#print(equi.n)
#print(equi.sides)
#equi.inputSides()
#equi.displaySides()
#print(equi.perimeter())

############
# Two builtin functions check relationships:
# isinstance(obj,class):
'''
- Checks the relationship between the objects and classes.
    - Returns True if the obj is an instance of the
    class or other classes derived from it.
- Each and every class in Python inherits from the base
class object.
'''
#print(isinstance(rectangle,Polygon))
#print(isinstance(equi,Triangle))
#print(isinstance(equi,Polygon))
#print(isinstance(rectangle,Triangle))
#print(isinstance(rectangle,object))
#print(isinstance(equi,object))

# issubclass(sub,sup):
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

#############
# Method Overriding in Single Level Inheritance:
'''
class Base: 
    def func(self): 
        print('Method of Base class')
        
class Child(Base): 
    def func(self): 
        print('Method of Child class')
        super(Child, self).func()

obj= Child()
obj.func()
'''

###########
# Data Encapsulation and Data Abstraction:
'''
- Data encapsulation describes the idea of wrapping data
and the methods that work on data within one unit.
- This puts restrictions on accessing variables and
methods directly and can prevent the accidental
modification of data.
'''

# Create a Base class with protected memebers
'''
class A:
    def __init__(self):
        self._var=5 # protected memeber
        
    def _sq(self): # protected memeber
        return self._var**2 #Access protected memeber within base class
    
    def cube(self):
        return self._sq()*self._var #Access protected memeber within base class

# Create a Derived class of A
class B(A): # B is a A
    def sq_perimeter(self):
        return 4*self._var #Access protected memeber in derived class
    def sq_area(self):
        return self._sq() #Access protected memeber in derived class
        
objA= A()
# print(objA.var) # Access Denied
# objA.sq() # Access Denied
print(objA.cube())

objB= B()
print(objB.sq_perimeter())
print(objB.sq_area())
'''

# Create Base class with private member:
'''
class A:
    def __init__(self):
        self.__var=5 # private memeber
        
    def __sq(self): # private memeber
        return self.__var**2 #Access private memeber within base class
    
    def cube(self):
        return self.__sq()*self.__var #Access private memeber within base class

# Create a Derived class of A
class B(A): # B is a A
    def sq_perimeter(self):
        return 4*self.__var #Trying to Access private memeber in derived class
    def sq_area(self):
        return self.__sq() #Trying Access private memeber in derived class
objA= A()
# print(objA.var) # Access Denied
# objA.sq() # Access Denied
print(objA.cube())

objB= B()
# print(objB.sq_perimeter()) # Access Denied
# print(objB.sq_area())  # Access Denied
'''

############
# Hierarchial Inheritance:
'''
- Syntax:
class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Base):
    pass
'''

# Create Rectangle class
class Rectangle(Polygon): #Rectangle 'is a' Polygon
    def __init__(self):
        super().__init__(4)
    
    def perimeter(self):
        a,b,c,d=self.sides
        peri= a+b+c+d
        return f'Perimeter is {peri}cm'

#rect= Rectangle()
#rect.displaySides()
#rect.inputSides()
#rect.displaySides()
#print(rect.perimeter())

############
# Multilevel Inheritance:
'''
- Syntax:
class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Derived1):
    pass
'''

# Create class Equilateral
class Equilateral(Triangle):
    def __init__(self):
        super().__init__()

    def area(self):
        a,b,c=self.sides
        ar=((1/3)*0.5)*(a**2)
        return f'Area is {ar}sqcm'

equi= Equilateral()
#print(equi.area())
#print(equi.perimeter())
#equi.inputSides()
#print(equi.area())

#############
# Method Overriding in Multilevel Inheritance:
'''
class Base: 
    def func(self): 
        print('Method of Base class')
        
class Child(Base): 
    def func(self): 
        print('Method of Child class')
        super(Child, self).func()
        
class NextChild(Child): 
    def func(self): 
        print('Method of NextChild class')
        super(NextChild, self).func()

obj= NextChild()
#print(NextChild.__mro__) #Method Resolution Order
obj.func()
'''

#mro: Method Resolution Order
'''
- MRO is the order in which Python looks for a method in
a hierarchy of classes.
'''

#############
# Multiple Inheritance:
'''
- Syntax:
class Base1:
    pass
class Base2:
    pass
class Derived(Base1,Base2):
    pass
'''

# Create a class Person
'''
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def perDisplay(self):
        return f'Name and Age is {self.name},{self.age}'

# Create a class Student
class Student:
    def __init__(self,Id):
        self.Id= Id
    def stuDisplay(self):
        return f'Rollno is {self.Id}'

# Create a class Resident:
class Resident(Person,Student):
    def __init__(self,name,age,Id,rno):
        Person.__init__(self,name,age)
        Student.__init__(self,Id)
        self.flat=rno
    def addressData(self):
        return f'{self.name} of {self.flat} has {self.Id} in which his age is {self.age}'

obj= Resident('Aditya',25,101,302)
print(obj.addressData())
print(obj.stuDisplay())
print(obj.perDisplay())
'''

#############
# Method Overriding in Multiple Inheritance:
'''
class A:
    def __init__(self):
        self.name='Roshan'
        self.age= 56
    def showName(self):
        print(self.name)

class B:
    def __init__(self):
        self.name='Preeti'
        self.age= 28
    def showName(self):
        print(self.name)

class C(B,A):
    def __init__(self):
        super().__init__()
       
obj= C()
obj.showName()
print(C.__mro__)
'''

#mro in multiple Inheritance
'''
- In multiple inheritances, the methods are executed
based on the order specified while inheriting the classes.
- In the multiple inheritance scenario, any specified
attribute is searched first in the current class.
- If not found, the search continues into parent classes
in Depth-First, Left-Right(DLR) fashion without searching
same class twice.
'''

# Complex Inheritance:
'''
class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass

m=M()
print(M.__mro__)
#<class '__main__.M'>,
#<class '__main__.B'>,
#<class '__main__.A'>,
#<class '__main__.X'>,
#<class '__main__.Y'>,
#<class '__main__.Z'>,
#<class 'object'>
'''

#############
# Data Abstraction:
'''
- Abstraction is used to hide internal details and show
only functionalities.
- In Python, Data Abstraction is implemented using
Abstract class.
- An abstract class can be considered as a blueprint for
other classes, allows you to create a set of methods
that must be created within any child classes built from
your abstract class.
'''
'''
class Shape:
    def area(self):
        pass
    def perimeter(Self):
        pass

class Square(Shape):
    def __init__(self,dim):
        self.side=dim

sh= Shape()
'''
# We require:
'''
- We don't want to allow other users to create instance
of Shape class, since it is a template for Square class.
- We want that any class which inherit Shape class must
implement area and perimeter methods inside the subclass.
- To fulfill the requirement we define Abstract class
'''
# Create abstract class
'''
from abc import ABC,abstractmethod
class Shape(ABC): # Shape class now act as abstract class
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(Self):
        pass

class Square(Shape):
    def __init__(self,dim):
        self.side= dim

#sh=Shape() # Error: Can't instantiate Abstract class
#sq=Square(10) # Error: Can't instantiate since not implemented area and perimeter
'''

# Implement Abstract class
'''
from abc import ABC,abstractmethod
class Shape(ABC): 
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(Self):
        pass

class Square(Shape):
    def __init__(self,dim):
        self.side=dim
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side
    def DisplaySide(self):
        return f'Side of square is {self.side}cm'

sq=Square(10)
print(sq.DisplaySide())
print(sq.area())
print(sq.perimeter())
'''
