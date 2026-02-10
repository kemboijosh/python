# functions with parameters
# parameters are values that are passed into a function when it is called

def greetings(name):
    print(f"{name} Hello, how are you?")
greetings("Joshua")
greetings("Alice")
greetings("Moses")


print("=========================================")
def message(names):
    print(f"{names}  We shall be having a party on Saturday")
   
message("Joshua")
message("Alice")

# create a function that accepts parameters to add  two numbers
def add_numbers(x, y):
    sum = x + y
    print("The sum of numbers is", sum)
add_numbers(10, 20)




