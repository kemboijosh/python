cars = ["BMW","Benze","Hiance", "Range", "probox", "Lexus", "subaru"]
print(cars)
print(type(cars))

print(cars[2])
print("The car on index 4 is", cars[4])

print(cars[4:])
print(cars[:4])

#from index 1 to index 3
print(cars[1:4])

# list mutability
# we use the function append to add an element to the end of a list
cars.append("mercedes")
print(cars)

cars.append("subaru")
print(cars)

# we use the pop function to remove the last element of a list
cars.pop()
print(cars)

# we can use an index to add items at a specific location
cars[5] = "pajero"
print(cars)

# we use sort to sort the list in alphabetical order
cars.sort(reverse=True)
print(cars)

cars.pop(3)
print(cars)

del cars[0]
print(cars)

cars.remove("Hiance")
print(cars)