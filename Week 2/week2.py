# Additional helpful things for loops
i = 0
while True: # Loop that runs forever
    if i == 15:
        break # Terminates the loop, will 'break' out of the loop
    i+=1
    if i == 6:
        continue # Skips everything after the loop and starts over the loop
    print(i)

# Additional helpful things for strings
"sheep sheep sheep".count("sheep") # Counts the number of occurances in a string
"sheep".find("e") # Finds where something shows up in a string first, else -1 if it can't find anything
"sheep".find("e", 3) # Second parameter is starting position from the string, finding from there
"sheep".index("e") # Similar to find, but throws an error when something can't be found

# Data structures
# Instead of initializing a ton of variables, you can use a list

# List - stores a 'list' of values, which can be retrieved 
hello = [] # Intialized with square brackets, with nothing, list is empty

# Many ways of adding items to a list
hello = ["hello", "bye", "good morning"] # Items intialized with the list
hello.append("good riddance") # Adds item to the list of list

# Can get items from list at index, like a string
hello[0] # Gets the first item, starts counting from 0
hello[3] # Gets the 3rd position
hello[0] = "bonjour" # Can also replace items at index
hello[0] # Is now "bonjour"
hello.pop() # Removes the last index, and returns the removed value
hello.pop(1) # Removes the 1st position (2nd value) from the list, and returns the removed value
hello.index("bonjour") # Same as index with strings, finds first index on a value in a list, or throws error
hello.append("bonjour")
# hello.index("bonjour", 1, 1) # Same as index with strings, finds first index of value between 1st position and 1st position, throws error
hello.remove("bonjour") # Removes the first occurance based of it's value
del hello[0] # Removes at index, but doesn't return

# Sorting lists
hello = [5, 67, 3, 1, 6, 2]
hello.sort() # Sorts the list in-place (sorts the list, and replaces the list), in asscending order
hello.sort(reverse = True) # Same as sort previously, but reversed (so descending now)
sorted(hello) # Sorts the list, but doesn't override the list, returns a sorted list
sorted(hello, reverse=True) # Same as sorted earlier, but now reverses the sorted list

# Reversing lists
hello.reverse() # Reverses the list in-place (reverses and overrides the list)
list(reversed(hello)) # Reverses the list, but doesn't override the original  list (you need to include list() as it reversed() doesn't return a list)

# Splitting strings
"Hello My Name Is David".split(" ") # Splits a string by a value, and puts split values into list, can split by any character
list("Hello My Name Is David") # Splits the string by all the characters

# List comprehension
# Instead of making a for loop to append to a list, you can do it in one line
nums = [i + 1 for i in range(10)] # Adds a list of numbers from 1 to 10, syntax starts with the value you want to add, and a loop
nums = [word for word in input().split()] # Adds all the words in input of string

# Dictionary - similar to list, but can be referred by any key (any immuatable/non-editable value) instead of index
testd = {
    "David": 17,
    "Sat": 16,
    "Kevin": 17
} # Intialized with curly brackets {}, with keys first, followed by colon, and the value
testd[5] = 15 # Adding to the dictionary or reassigning in a dictionary
# Similar to a real life dictionary
# Values in a dictionary don't all have to be the same, anything could be included

# Another way of creating a dictionary
dict(David = [17, 1, 2, 34], Sat = 16, Kevin = 17)

testd["David"] # Getting values in a dictionary
testd.get("David") # Getting values in a dictionary (either one works)
del testd["Kevin"] # Deletes from a dictionary at a key
testd.pop("David") # Same as deleting from a list, returns the deleted value
testd.clear() # Clears the whole dictionary