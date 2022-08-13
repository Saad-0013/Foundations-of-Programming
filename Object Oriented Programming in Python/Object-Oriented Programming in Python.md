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


## Polymorphism

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

### Printable classes

Printing a class returns a memory address, however printing something such as a numpy.array returns the data present inside of that array.

We can implement a similar functionality with our classes using the following methods:
1. ```__str__()```
2. ```__repr__()```

#### Example of ```__str__()``` method
Informal representation suitable for end user

- ```print(np.array([1,2,3]))```
output: [1,2,3]

- ```str(np.array([1,2,3]))```
output: [1,2,3]

##### Code

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

#### Example of ```__repr__()``` method
Formal and more reproducible representation

- ```repr(np.array([1,2,3]))```
output: array([1,2,3])

# Chapter 4

## Designing Classes

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





