# Leave 2 lines at the beggining

def my_function(str1, str2):  # use snake case to define functions
    print(str1)
    print(str2)


my_function("This is argument 1",
            "This is the second argument which is also a string.")

# DEFAULT ARGUMENTS
def print_something(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)


print_something("Nick", 27)
print_something("Nick")
print_something()
# PARAMETER AS KEY
print_something(age=27, name="Nick")
print_something(age=27)

# INFINITE ARGUMENTS
def print_people(*people):
    for person in people:
        print("This person is",person)


print_people("Nick","Dan","Jack","King","Smiley")

# RETURN VALUES
def do_math(num1,num2):
    return num1 + num2

math1 = do_math(5,7)
math2 = do_math(11,34)

print("First sum is",math1,"and the second sum is",math2)
