from pyIn import pyIn


## string input

name = pyIn("%s", "Enter a name: ")
print("Hello", name)

## integer input

age = pyIn("%i", "Enter your age: ")
print("Your Age Is: ", age)


## float input

weight = pyIn("%f", "Enter your weight: ")

print("Your Weight is: ", weight )