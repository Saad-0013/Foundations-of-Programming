# Object Oriented Programming in Python

## Types of Programming

1. Prodcedural Programming
    - Code as a sequence of steps
    - Mostly used for data analysis and scripts

2. Object Oriented Programming
    - Code as interaction of objects
    - Mostly for bulding frameworks and tools
    - More easy to maintain and reusable

# Chapter 1

## Objects v/s Classes

1. Objects as data structures

    - Data structure that encorporates information about
        - state
        - behavior

    - Customer Object
        - <b>can have - States</b> 
            - email 
            - phone number

        - <b>can perform the acts of - Behavior</b>
            - placing order
            - cancel order
        
    - <b><u>Example</u></b>
        - A button having a label (state) and pressing it can trigger an event (behavior). 

    - Everything in Python is an object.
    
2. Classes

<b>Classes</b> can be thought of as blueprints for objects outlining possible states and behavior.

Defining a class for a customer object, means each customer will have a phone number and an email. In this way we can talk about all the customers in a unified way.


## Encapsulation

For an object, <b>State</b> and <b>Behavior</b> are bundelled together. 

- A Customer Object has:
    - data
    - actions

Think of data and actions as a single unit representing a customer object. Not as seperate units.

The data describing the state of the object, should be bundled into the object. 

## ATTRIBUTES v/s METHODS

### Methods
Methods are function definitions within a <b>Class</b>.


<b>State</b> information is contained in <b>Attributes</b>.
<b>Behavior</b> information is contained in <b>Methods</b>.

### Examples
<b>Attribute:</b> a.shape
<b>Method:</b> a.reshape()

## Classes

Classes are templates. 
Class is a standing for the future object.

```Python
class Customer:
    # code for class goes here
    
    # declaring a method
    def identity(self, name):
        print('I am a customer' + name)
    pass
```

### Using the SELF argument

```Python     
cust = Customer.Identity("Laura")
Customer.identity(cust, "Laura")
```

## The __init__() Constructor

1. With one argument

The ```__init__()``` constructor is called every time an object is created.

<u>Example code</u>

```Python
class Person:
    def __init__(self, name):
        self.name = name
        print('The class has been declared and initialized!')

customer = Person('Ahmed')
```

2. With multiple arguments

We can also use the init constructor to initialize multiple attributes.
To give an attribute a default value, we need to pass the default value assigned to the attribute in the as an argument to the ```init``` constructor.

<b>Example code</b>

```python
class person:
    def __init__(self, name = "", age = 20):
        self.name = name
        self.age = 32 
```

# Chapter 2

Data can be split into two types.
- Instance level data
- Class level data

## Class level data

We can use class attributes as global constants related to that class that are same across all instances of that class.

### Class methods
Methods are better off to be bound to an instance than a class, as they have limited application scope. 

Class methods will not be able to use any instance level data.

<b>Why do we need class methods?</b>
Main use case: alternative constructor
Using a method would require an instance.

```python
class MyClass:

    # cls refers to class
    # you cannot refer to any instance attributes in this method
    @classmethod   # <-----decorator to declare a class method
    def my_class_method(cls, args...):
        # do stuff here 
        # CANNOT use any instance attributes
        pass

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            name = f.readline()
        
        # similar to MyClass(argument) when an instance is called 
        # since we are inside the class we are using cls
        # cls(...) will call __init__(...)
        return cls(name)
```

Using class notation to access the class method

```python
MyClass.my_class_method(args...)
```

Now we can also declare an instance without explicityly calling the class constructor.

```python
emp = MyClass.from_file("data.txt")
```

### Defining global variables inside classes

```Python
class Employee:
    # defining a global variable that is same for all instances of this class
    MIN_SALARY = 30000

    def __init__(self, name, salary):
        self.name = name

        if salary >=  Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALAR

employee_one = Employee('Ahmed', 50000)
employee_two = Employee('Ali', 60000)

# This statement will always return TRUE
print(employee_one.MIN_SALARY == employee_two.MIN_SALARY)
```

## Inheritance

Inheritance means to extend functionality of already written code.

OOP allows us to keep the interface consistent while customizing functionality.

It is always better to have a general structure.

Inheritance allows us to code 'IS-A' relationships between classes.
```python
class MyParent():
    ...
    pass

class MyChild(MyParent):
    ...
    pass
```

<b>Example</b>

```python
class Counter:
    def __init__(self, count):
       self.count = count

    def add_counts(self, n):
       self.count += n

class Indexer(Counter):
   pass
```
Running the code ```ind = Indexer()``` will cause an error.

As the Indexer class is inherited from Counter and doesn't have its own constructor, it will attempt to use the Counter's constructor. But the Counter's constructor accepts an additional argument count, which was not passed to Indexer()

### Constructors for inherited classes

<b>The parent class</b>

```python
class BankAccount():
    def __init__(self, balance):
        self.balance = balance
```

<b>The inherited class</b>

```python
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        BankAccount.__init__(self, balance)

```

The inherited class ```SavingsAccount``` has an additional parameter.

Instances of a subclass are also instances of the parent class.

<b>Class Attributes in inherited classes</b>

Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class

# Chapter 3

## Operator Overloading

Python does not compare two class objects as the same even if they have the same data.

```python
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

person_one = Person('Ahmed', 1)
person_two = Person('Ahmed', 1)

print(person_one == person_two)
```
<b>Output:</b> <u>False</u>

When an object is created, a chunk of memory is allocated to the variable name. The variable now references that chunk of memory. Two class objects therefore can never be the same because the comparison is being made between memory spaces. 

However we see that two numpy arrays, or data frames with the same data will return true if they contain the same information.

To implement this functionality in our own classes we make use of the ```def __eq__(self, other)```  function. 

```python
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __eq__(self, other):
        return (self.id == other.id) and \
               (self.name == other.name)
```

Python allows us to implement other operators as well.

```python
== __eq__()
!= __ne__()
>= __ge__()
<= __le__()
>  __gt__()
<  __lt__()
```

There is also a ```def __hash__(self, other)``` function that can be used to check if two objects are the same. Equal objects will have equal hash values

### checking the type()

It is good practise to check the ```type()``` of the objects in the ```__eq__()``` function.

<b>For Example</b>

Consider two different classes with the same attribute name

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

class Customer:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

Here ```customer == person``` will return ```True```.

To prevent this from happening we need to modify the ```__eq__()``` function.

```python
def __eq__(self, other):
    return (self.name == other.name) and \
        (type(self) == type(other))
```

<u>Note:</u>
When using the operations, the operator function of the later object is called.

```python
p = Parent()
c = Child()
```

```p == c``` calls the __eq__() function of c. 

## Printable classes

Printing a class returns a memory address, however printing something such as a numpy.array returns the data present inside of that array.

We can implement a similar functionality with our classes using the following methods:
1. ```__str__()```
2. ```__repr__()```

### Example of ```__str__()``` method
Informal representation suitable for end user

- ```print(np.array([1,2,3]))```
output: [1,2,3]

- ```str(np.array([1,2,3]))```
output: [1,2,3]

### Example of ```__repr__()``` method
Formal and more reproducible representation

- ```repr(np.array([1,2,3]))```
output: array([1,2,3])

#### Code

```python
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        # tripple quotes are used for multi line strings
        cust_str = """
        Customer:
            name: {name}
            balance: {balance}
        """.format(name = self.name, \
                    balance = self.balance)
        
        return cust_str

    def __repr__(self):
        return "Customer('{name}, {balance}')".format(name = self.name, balance = self.balance)
```

### Exceptions

Errors in pythons are called exceptions 
If exceptions are not handled correctly they will stop the execution of the entire program.

To catch an exception use the ```try - except - finally```

```python
try:
    # try to run this piece of code
    print(0/1)
except ExceptionNameHere:
    # Run this code if the ExceptionNameHere happens
except SecondExceptionNameHere:
    # Run this code if the SecondExceptionNameHere happens
finally: # <- optional
    # Run this code no matter what
    # Example: close files that were opened up in earlier conditions
```

#### Raising Exceptions

```python
def check(length):
    if length < 0:
        raise ValueError('Invalid Length!)
    return -1*length
```

#### Defining Custom Exception

Define a class that inherits from the exception class or any one of its subclasses. The class itself may be empty, it just needs to inherit from the exception class.

```python
class DefineException(Exception):
    pass
```

To use this newly defined exception class we just have to call the class name inside of another class.

```python
class Customer:
    def __init__(self, name, balance):
        if self.balance < 0:
            raise DefineException('Balance can not be a negative number!')
        else:
            self.name, self.balance = name, balance
```

Using the exception method the constructor terminates and the object is not created at all. 

To deal with this the user may use the ```try - except``` method to deal with the exception.

```python
try:
    customer = Customer('Ahmed', -100)
except DefineException:
    customer = Customer('Ahmed', 0)
```

<b>Note:</b>
It's better to include an except block for a child exception before the block for a parent exception, otherwise the child exceptions will be always be caught in the parent block, and the except block for the child will never be executed.




# Chapter 4

## Designing Classes

### Designing for Inheritance and Polymorphism

#### Polymorphism

Using a unified interface to operate on objects of different classes.

##### Liskov Substitution Principle

Base class should be interchangeable with any of its subclasses without altering any properties of the surrounding program.

#### Managing data access

All class data is public in python. This is by design.

##### Naming convention

- Using a single leading underscore that is not part of the public interface. Attributes that start with '_' should not be changed. This naming convention is used for internal implementation and helper functions.

- Using a double underscore means that the attribute is private and will not be oonventionally inherited by child classes.

    - Name Mangling: an attribute named as ```obj.__attr_name``` is interpreted as ```obj._MyClass__attr_name```. 
    
    - This principle is used to prevent name clashed in inherited classes. 

    - It is possible that someone who has used your class as a parent class, they may introduce an attribute name that is similar to the one used in the parent class. To prevent this we make use of the double underscore '__' . This methods helps to protect important attributes.

- Leading AND trailing underscores are only used for python built in functions - such as ```__init__()``` .

#### Accessing class attributes

We first declare a class and define class attributes.

```python
class BetterDate:
    # class attributes
    _MAX_DAYS = 30
    _MAX_MONTHS = 12
    
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
```

To access the class attributes. inside of the respective class, we will use the ```ClassName.attribute_name``` syntax.

```python
    def _is_valid(self):
        if self.day <= BetterDate._MAX_DAYS and self.month <= BetterDate._MAX_MONTHS:
            return True
        else:
            return False
```

#### Properties

We set and use certain class properties to check the validity of certain attributes, for example in an employee class, we can set employee.salary to anything using a simple assignment operator. This should not be the case. 

We can also use properties to make certain attributes read only as well.

For added security we define read/write access for attributes using the ```@property``` decorator.

1. Use protected attribute with a leading '_' to store the data.

```python
class Company:
    def __init__(self, name, new_salary):
        self._salary = new_salary
        ...
```

2. Now we need to define a function, headed with the ```@property``` decorator. The name of the function should be exactly the same as the attribute.

```python
class Company:
    def __init__(self, name, new_salary):
        self._salary = new_salary
        ...

    @property
    def salary(self):
        return self._salary
```

3. To customize how the salary is set, we need to implement a seperate method. The setter needs to be headed with ```@attr_name.setter```.

```python
class Company:
    def __init__(self, name, new_salary):
        self._salary = new_salary
        ...

    @property
    def salary(self):
        return self._salary
        
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError('Salary cannot be a negative number!')
        
        else:
            self._salary = new_salary
```

<b>Importance</b>

Now the class defined above behaves as if a normal class object. However if we choose not define a setter method for the attribute the salary attribute will be a read only.

##### Code

```python
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")

cust = Customer('Belinda Lutz', 2000)
cust.balance = 3000
print(cust.balance)
```
Other Property attributes: <br>
- ```@attr.setter``` <br>
- ```@attr.getter``` <br>
- ```@attr.deleter``` <br>

# Good coding practices
- Use camel case for class names
- Use lower case and underscores for methods
- The below written code is correct, but it is not recommended. 
- Attributes should be always defined with the init construtor. This helps the code to be more maintained and more readable.
```python
def __init__(kitty, name):
    kitty.name = name
```
- Use doc strings to add meaningful comments to classes, which can be accessed using the help function.





