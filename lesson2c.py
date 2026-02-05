# A dictionary is a data type that stores data in term of key-value pairs
# it is introduced using curly braces {}
# the values in a dictionary can be of any data type and they can be duplicated
# To access the values in a dictionary we use the keys


phonebook= {
    "John": "0712345678",
    "Mary": "0723456789",
    "Peter": "0734567890"
}

# showing the dictionary
print(phonebook)
print(type(phonebook))

#printing the value of a specific key
print(phonebook["John"])