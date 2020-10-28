print("Hello World!") # Outputs "Hello World!"

# Variables - stores information
# Stored with name, but with restrictions (any letters, numbers, and underscore)
# Variables cannot start with numbers, but shouldn't start with underscore
# Example of invalid variable: 1234abc
# Variables are also case sensitive: abc is different ABC

# Example of assigning variables
stringVariable = "string variable" # Use double or single quote
numberVariable = 123 # No set largest number
floatVariable = 3.1415 # Decimals

# Comparison - Comparing variables, returns boolean (True or False)
1 == 1 # Equality - compares if 2 things are equal
1 != 1 # Not equality - compares if 2 things aren't equal
1 <= 1 # Less than or equal to
1 >= 1 # Greater than or equal to
1 < 2 # Less than
1 > 2 # Greater than
1 >= 0.3 # Can also mix types

# == only checks if properties are equal, not the same
1 is 1 # Checks if both are the same

# Strings can be used in comparison
# Each character is connected to a number, which allows comparison
"Hello" > "Apple" # True, as Hello is further down than Apple in a dictionary
"Apple" == "apple" # False, letters case sensitive, and each number share different values
ord("A") # Gets the number of letter A, which is 65
ord("a") # Gets the letter of letter a, which is 97

# Operations
test = True # Variable that stores True
test = not test # Inverts the variable, which is now false

# String operations
# Use square brackets []
test = "massey"
test[1] # Gets character at 1st position, starts counting at 0 rather than 1, value is 'a'
test[0:2] # Gets characters from 0th position up to, but not including the 2nd position, value is 'ma'
test[3:] # Gets from 3rd position to the end, value is 'sey'
test[:3] # Gets from the beginning, up to, but not including the 3rd position, value is 'mas'
test[::2] # Starts beginning to end, but only grabs every other letter, value is 'mse'
# Syntax: test[start:end:step]

# Can also go backwards in string operation
test[-1] # Gets character at the end, value is 'y'
test[-1:-5:-1] # Gets from the end, up to, but not including the 5th character from the end, with a step going backwards, value is 'yess'
test[::-1] # Goes from beginning to end, but goes backwards, value is 'yessam'

# Input - gets input from the user
test = input() # Gets input from user, as a string
print(test * 5) # Gets the input, but 5 times, can multiply strings, but it appears 5 times
# Can cast variables, which changes it, e.g. int() to int, float() to float, or bool() to boolean
print(int(test) * 5) # Converts test into an integer, and multiplies it by 5

# Input gets the whole line, rather than seperating by space
line1 = input() # Gets input in line 1
line2 = input() # Gets input in line 2 (you cannot go backwards to get data)

# You can also add a prompt in input (DO NOT USE DURING CONTESTS)
input("Enter a prompt in here")

# Loops
times = int(input("How many times would you like to multiply?"))
number = 10

# Example of a for loop
for i in range(times): # i is your counter, that goes through range(), which goes through a range of values
    number = number * 10 # Reassigns number to 10 times number
    number *= 10 # Same as doing number = number * 10

    number = number + 10 # Reassigns number to 10 + number
    number += 10 # Same as doing number = number + 10

range(0, times, 2) # Similar to string splicing, where you have start, stop, step

# Example of a while loop, not all information is given, rather just a condition
number = 0
while number != 10: # Will constantly run, while the number isn't 10
    print("hello")
    number = int(input("Enter a number"))

# Commenting
# Ignored by the computer
# This is a single line comment
'''This is a
multiline
comment'''