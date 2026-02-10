# Python functions
# They are a block of code that performs a specific task. They are reusable and perform a different task than the main program. They can take input and return output.
# Function are defined using the def keyword (define)
# We have two types of functions: built-in functions and user-defined functions
# Built-in functions are functions that are already defined in Python and can be used without importing any module. Examples of built-in functions are print(), input(), len(), etc.
# User-defined functions are functions that are defined by the user and can be used in the program. They are defined using the def keyword followed by the function name and parentheses. The code block within every function starts with a colon (:) and is indented.
# to define a function, we need to give it a name and specify the parameters (if any) that it takes. 
# for the function it is usually indented and to invoke the function, we need to call it by its name followed by parentheses. 

def greetings():
    print("Hello, how are you?")

# below is how to call the function
greetings()

print("=========================================")

# addition function
def addition():
    num1 = 40
    num2 = 60
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)

addition()

print("=========================================")
# create a function that is able to multiply three values
def multiplication():
    num1 = 10
    num2 = 20
    num3 = 30
    product = num1 * num2 * num3
    print("The product of numbers", num1, ",", num2, "and", num3, "is", product)

multiplication()

print("=========================================")
# division function
def divide():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    quotient = num1 / num2
    print("The answer is", quotient)
divide()

for function in range(3):
    print(function)


 

