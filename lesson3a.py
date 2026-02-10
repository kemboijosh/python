# Boolean - is a data type that evaluates either it is true or false

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))

# Comparison operators - are used to compare values and they return a boolean value

number1 = 2
number2 = 5

print("Is number1 greater than number2?", number1 > number2)
print("Is number1 less than number2?", number1 < number2)
print("Is number1 greater than or equal to number2?", number1 >= number2)
print("Is number1 less than or equal to number2?", number1 <= number2)
print("Is number1 equal to number2?", number1 == number2)
print("Is number1 not equal to number2?", number1 != number2)

# Logical operators - are used to combine conditional statements and they return a boolean value
# logical AND - it returns true

print((3 > 1) and (7 < 6 ))  # True because both conditions are true

# logical or
# it evaluates to true if one of the conditions is true
print((3 > 1) or (7 < 6 ))  # True because one of the conditions is true

# logical not
# it returns the opposite of the condition
print(not(90 > 70))  # False because the condition is true