#getting started
print("Hello World!")

# Python Keywords and Identifiers
# Python Statements, Indentation,Comments
apples = 4
price_per_apple = 20
total_cost_of_apples = apples * price_per_apple
print("Total cost of apples is: ", total_cost_of_apples)

letter_to_friend = "Hello friend, it's been long since we met each other"
print(letter_to_friend)
first_part_of_letter = letter_to_friend[:18]
print(first_part_of_letter)

is_male = False
if is_male:
    print("You are a guy.")
else:
    print("You are a girl.")

# We can write single line comments using # at the beginning of statement
"""
Multi line comments are written using """ """ quotes.
It's fun to learn python.
The line can extend how much ever we want.
"""


"""
Indentation is the key in python as we do not have opening and closing brackets
like C, C++, Javascript. So code within a code block like function, if..else
construct is defined by indenting within the code block
"""

def add_a_b(a, b):
    #here indentation needs to be used to enclose below lines into the function block
    result = a + b #local variable result, this line is also a statement
    return result


# Docstring
def square(num):
    ''' Takes in a number num, returns the square of num '''
    return n**2

# Here the string ''' Takes in a number num, returns the square of num ''' is a docstring
# because it comes just after function defenition. Python docstring can be accessed by using __doc__ attribute of function
def square(num):
    ''' Takes in a number num, returns the square of num '''
    return n**2
print(square.__doc__)


# Python Variable, constant and literal
# variables
numberic_variable = 25.77
string_variable = "This is my home"
boolean_variable = True
a, b, c = 4, 4.5, "Hello"
print(a, b, c)

# constant
import constant
print(constant.PI)
print(constant.GRAVITY)
print(constant.SPEED_OF_LIGHT)

#literals are raw data given in variable or constant
#numeric literals
# they are immutable
a = 0b1010 #Binary Literals
b = 1908 #decimal literal
c = 0o310 #octal literal
d = 0x12cde #Hexadecimal literal

#Float literal
float_1 = 10.5
float_2 = 1.53e4

#complex_literal
x = 2.44j
y = 1.16 + 7.2j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
print(y, y.imag, y.real)


#string literals
my_str = "This is my lamp"
char = "c"
multiline_str = """
                This string can extend to multiple lines.
                Haha.
                """
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string" # \n is not processed here

print(my_str)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#boolean literals
x = (1 == True)
y = (1 == False)
a = True + 8
b = False + 11

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Python Data Type
a = 10
print(a, "is of type", type(a))

b = 5.6
print(b, "is of type", type(b))

c = 5 + 6j
print(c, "is a complex number?", isinstance(c, complex))


# Python Data Types in details (List, Dictionary, Tuple, Set, Strings)
#list
my_list = ["apples", 4, "banana", 6, "mango", 8]
print("mylist[2]:", my_list[2])

print("mylist[0:3]:", my_list[0:3])

print("mylist[2:]", my_list[2:])

#tuple
#tuples are immutable

my_tuple = (22, "jump street", 78 + 8j)
print("my_tuple[1]:", my_tuple[1])
print("my_tuple[1:]:", my_tuple[1:])


#strings
#strings are immutable
my_string = "They may be on a plane"
print("my_string[4]:", my_string[4])
print("my_string[6:11]:", my_string[6:11])

#set
#it is an unordered collection of unique items
my_set = {5, 2, 88, 109, 229}
print("my_set =", my_set)
print(type(my_set))
print(my_set[2]) # output: set object is not scriptable

a = {1, 2, 2, 3, 3, 4, 4, 4}
print(a) #output: {1, 2, 3, 3}

#dictionary
# it is an unordered collection of key-value pairs
my_dict = {
    1: 'value',
    'key': 2
}
print(type(my_dict))
print("my_dict[1]:", my_dict[1]) # op: value
print("my_dict['key']:", my_dict['key']) # op: 2



# Python Type Conversion and Type casting
#explicit type conversion (type casting)
print(float(57)) # op: 57.0
print(int(10.8890)) # op: 10
print(int(-10.780)) # op: -10
print(float('2.77')) # op: 2.77
print(str(66800)) # op: '66800'

print(set([1, 2, 3])) # op: {1, 2, 3}
print(tuple({5, 6, 7})) # op: (5, 6, 7)
print(list('hello')) # op: ['h', 'e', 'l', 'l', 'o']
print(dict([[1, 'apple'], [2, 'banana']])) # op: {1: 'apple', 2: 'banana'}
print(dict([(3, 11), (4, 22)])) # op: {3: 11, 4: 22}

#implicit type conversion
a = 12
b = 22.6
result = a + b
print("type of a:", type(a)) # int
print("type of b:", type(b)) # float
print("type of result:", type(result)) # float

# Python input, output and import
# output
print("Hello user")
my_var = 100
print("Value of my var is: " + str(my_var))

print(1, 2, 3, 4, sep = '*') # op: 1*2*3*4
print(1, 2, 3, 4, sep = '#', end = '%') # op: 1#2#3#4%

print("My title of book is \"War and Peace\"") # op: My title of book is "War and Peace"

#formatting outputs
print("I love {} and {}".format("mango", "pineapple"))
#op: I love mango and pineapple
print("I love {1} and {0}".format("mango", "pineapple"))
# op: I love pineapple and mango

pi = 3.1415869
print("The value of pi is %3.2f" %pi)
# op: The value of pi is 3.14
print("The value of pi is %3.4f" %pi)
# op: The value of pi is 3.1416

x = 11
y = 22
print(f"The value of x is {x} and y is {y}")
# op: The value of x is 11 and y is 22

#input
age = input("Enter your age: ")
print(f"You are {age} years old")
# op: Enter your age: 23
# You are 23 years old

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("The sum is: {}".format(x+y))
# Enter x: 11
# Enter y: 33
# The sum is: 44

#import
# used when program grows bigger, so we divide code into different modules
import math
print(math.pi) # 3.141592653589793


# Python Operators
x = 59
y = 11
print("x + y =", x+y)
print("x - y =", x-y)
print("x * y =", x*y)
print("x / y =", x/y)
print("x // y =", x//y)
print("x ** y =", x**y)

x = 59
y = 11
print("x + y =", x+y)
print("x - y =", x-y)
print("x * y =", x*y)
print("x / y =", x/y)
print("x // y =", x//y)
print("x ** y =", x**y)
# x + y = 70
# x - y = 48
# x * y = 649
# x / y = 5.363636363636363
# x // y = 5
# x ** y = 30155888444737842659

print("x + y =", x+y)
print("x - y =", x-y)
print("x * y =", x*y)
print("x / y =", x/y)
print("x // y =", x//y)
print("x ** y =", x**y)
# x + y = 70
# x - y = 48
# x * y = 649
# x / y = 5.363636363636363
# x // y = 5
# x ** y = 30155888444737842659

# logical operators
print('x > y is',x>y)
print('x < y is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)
# x > y is True
# x < y is False
# x == y is False
# x != y is True
# x >= y is True
# x <= y is False

#bitwise operators
x = 0b1100 # 12
y = 0b1001 # 9

print("x & y = ", bin(x & y))
print("x | y = ", bin(x | y))
print("~x = ", bin(~x))
print("x ^ y = ", bin(x ^ y))
print("x >> 2 = ", bin(x >> 2))
print("x << 2 = ", bin(x << 1))
# x & y =  0b1000
# x | y =  0b1101
# ~x =  -0b1101
# x ^ y =  0b101
# x >> 2 =  0b11
# x << 2 =  0b11000


# membership operators
# in returns true if value/variable is found in the sequence
# not in returns true if value/variable is not found in the sequence

x = "Hello world"
y = {1: "a", 2: "b"}

print("H" in x) # true
print("hello" not in x) # true
print(1 in y) # true
print("a" in y) # false


# Python namespace
# Local, Global variables
# namespace is mapping of names to corresponding objects
def outer_func():
    a = 30
    b = 20  # local variable in outer_function namespace
    def inner_func():
        a = 100
        c = 10
        b = 10# local variable in inner_function namespace
        print(b)
    inner_func()
    print(b)
a = 10 # global variable in global namespace
outer_func()
print(a) # 10

# defining a as global
def outer_func():
    global a
    a = 100 # a is now global variable in global namespace
    print(a) # 100
    def inner_func():
        global a
        a = 200 # a is global variable in global namespace
        print(a) # 200

    inner_func()
    print(a) # 200

a = 10
outer_func()
print(a) # 200



# Python Flow Control ( if else )
age = 22
if age < 18:
    print("You cannot vote !")
else:
    print("You can vote !")

score = 77
if (score >= 40) and (score < 55):
    print("Third division")
elif (score >= 55) and (score < 65):
    print("Second division")
elif (score >= 65) and (score < 80):
    print("First division")
elif (score >= 80) and (score <= 100):
    print("Distinction")
else:
    print("Failed")
# op: First division


# Python Loop (for, while)
# for loop
inventory = ["apple", "oranges", "mangoes"]
for item in inventory:
    print(item)

for i in range(1, 6):
    print(i * '*')

result = 0
for i in range(1, 11):
    result += i
print("Sum of digits from 1 to 10 is:", result)

my_list = [i for i in range(1, 11)]
print(my_list)

# for loop with else
digits = [1, 4, 6, 10]
for num in digits:
    print(num)
else:
    print("No digits left")
# 1
# 4
# 6
# 10
# No digits left

# while loop
# table of a digit
num = 9
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1

# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90

num = int(input("Enter a number: "))
# sum from 0 to n
result = 0
i = 1
while i <= num:
    result = result + i
    i += 1
print("The sum from 0 to {} is:".format(num), result)
# Enter a number: 10
# The sum from 0 to 10 is: 55

# Python break, continue and pass
my_list = [i for i in range(1, 11)]
for num in my_list:
    if num == 7:
        continue
    print(num, end=' ')
# op: 1 2 3 4 5 6 8 9 10

my_list = [i for i in range(1, 11)]
for num in my_list:
    if num == 7:
        break
    print(num, end=' ')
# op: 1 2 3 4 5 6

# pass is a null statement, it results in no operation
# pass is generally used as a placeholder
my_list = [i for i in range(1, 11)]
for num in my_list:
    if num == 7:
        pass
    print(num, end=' ')

# op: 1 2 3 4 5 6 7 8 9 10

def square(num):
    pass # pass is used as a placeholder for future statements at this place


# Functions
# Return statement
import math
def area_of_triangle(a, b, c):
    s = (a + b + c)/2 # semi-perimeter
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

print("Area of triangle with sides 3, 4, 5 is: {}".format(area_of_triangle(3, 4, 5)))

# Area of triangle with sides 3, 4, 5 is: 6.0

def greet(name):
    """
    This function greets to the person passed in as a parameter
    """
    print("Hello, {}. Good morning !".format(name))

greet("Pujan")
# Hello, Pujan. Good morning !

def absolute_val(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute_val(-77)) # 77
print(absolute_val(66)) # 66

# Function Arguments (Default, keyword, arbitrary)
def greet(name, msg):
    print(f"Hello {name}, {msg}!")

greet("Pujan", "Goodnight")
# Hello Pujan, Goodnight!

# non default arguments cannot follow default arguments
def greet(name, msg = "Good morning"): # default msg is Good morning
    print(f"Hello {name}, {msg}!")

greet("Pujan")
greet("Pujan", "Good night")
# Hello Pujan, Good morning!
# Hello Pujan, Good night!

#keyword arguments
greet(msg = "Having fun", name = "Hari")
# Hello Hari, Having fun!

#arbitrary arguments
def greet(*names):
    for name in names:
        print(f"Hello {name}")

greet("Ram", "Shyam", "Hari", "Mohan", "Krishna")
# Hello Ram
# Hello Shyam
# Hello Hari
# Hello Mohan
# Hello Krishna



# Inbuilt functions
my_list = ["Ram", "Shyam", "Hari", "Bishal", "Mohan"]
print(len(my_list)) # 5
print(abs(-234)) # 234
print(bin(18)) # 0b10010

print(bool(0)) # false
print(bool(1)) # true

val = dict([[1, "apple"], [2, "banana"]])
print(val) # {1: 'apple', 2: 'banana'}
print('id(val): {}'.format(id(val))) # id(val): 140245695846400
print(max(my_list)) # Shyam
print(min(my_list)) # Bishal
print(round(1.569902, 2)) # 1.57

new_list = [1, 4, 5, 6]
print(sum(new_list)) # 16


# Python Anonymous/ Lambda Function
# these are anonymous functions that can take any number of arguments but have
# only one expression
double = lambda n:n*2

print(double(10)) # 20

add = lambda a, b: a+b
print(add(10, 20)) # 30

larger = lambda a, b: a if a>b else b
print(larger(10, 46))

# sorting in order of length of name
names = ['Alan', 'Rick', 'Morty', 'William', 'Jackobson']
names.sort(key = lambda x:len(x))
print(names)

def my_func(n):
    return lambda a:a*n

my_doubler = my_func(2)
my_tripler = my_func(3)

print(my_doubler(11)) # 22
print(my_tripler(11)) # 33


# Filters, map functions





