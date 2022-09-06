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

# Python Operators
# Python namespace
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

# Python break, continue and pass
# Functions
# Return statement
# Function Arguments (Default, keyword, arbitrary)
# Inbuilt functions
# Python Anonymous/ Lambda Function
# Filters, map functions
# Local, Global variables
# Python Data Types in details (List, Dictionary, Tuple, Set, Strings)




