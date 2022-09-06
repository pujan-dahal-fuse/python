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


# Python Type Conversion and Type casting
# Python input, output and import
# Python Operators
# Python namespace
# Python Flow Control ( if else )
# Python Loop (for, while)
# Python break, continue and pass
# Functions
# Return statement
# Function Arguments (Default, keyword, arbitrary)
# Inbuilt functions
# Python Anonymous/ Lambda Function
# Filters, map functions
# Local, Global variables
# Python Data Types in details (List, Dictionary, Tuple, Set, Strings)




