print("1->###############################   Welocome to NHK   ###############################");

for left in range(7):
    for right in range (left,7):
        print("[" +  str(left)   +   "|" + str(right) + "]" , end=" ")
    print()

################################################################################ recursion
print("2->###############################");
print(" recursion");


def factorial(n):
    if n<2:
        return 1;
    return n*factorial(n-1); # base case

print(factorial(8));



#########################################################################################
print("###############################");
print(" is_power_of");


def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    if (number==1):
        return number==1
    return number==1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print (is_power_of(9,2) );


#--8,2
#--4,2
#--2,2
#--1,2


################################################################################################

print("###############################");
print(" factorial_loop");


def factorial(n):
    result = n
    start = n
    n -= 1
    while n>0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -=1 # Decrement the appropriate variable by -1
    return result

print(factorial(5))

#################################################################################################

print("###############################");
print(" rows_asterisks");


def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(6):
        # Complete the inner loop range to control the number of
        # asterisks per row
        for y in range(x):
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above
################################################################################################

#   str can converted number to str
print("###############################");
print(" countdown_loop");

def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >0: # Complete the while loop
            return_string += str(x) # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x-=1 # Decrement the appropriate variable
        return_string += str(0)
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
print(countdown(0)) # Should be "Cannot count down to 0"
#####################################################################################################

print("###############################");
print(" all_numbers_loop");

def all_numbers(minimum, maximum):

    return_string = " " # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # numbers up to and including the "maximum" value.
    for number in range(minimum,maximum+1):

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(number)
        return_string += " "


    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0
####################################################################################################

# String in python are imutable
# string starts with index 0
# In Python, strings are immutable. This means that they can't be modified. So if we wanted to fix a typo in a string, 
# we can't simply modify the wrong character. We would have to create a new string with the typo corrected. 
# We can also assign a new value to the variable holding our string.

# methods
	#upper
	#isnumeric
	#strip
	#lstrip
	#join
	#split
	#count can be used to return the number of times a substring appears in a string
	#If you wanted to check if a string ends with a given substring, you can use the method endswith.
	#" ".join(["This","is","a","sentence"]) would return the string "This is a sentence".

print("###############################");
print(" string format ,format expression and place holder");	
	
def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)
	#return "{name} recevied {grade}% on the exam".format(name=name,grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


#STRING FORMATTING


#You can use the format method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, {}, as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters. The variables passed to the method will then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us. 

#If the curly brackets are empty, they’ll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. This allows for more easily readable code, and for more flexibility with the order of variables.

#You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.

######################################################################################################################################################

#String Reference Guide

#In Python, there are a lot of things you can do with strings. In this guide, you’ll find the most common string operations and string methods.

#String operations

#len(string) - Returns the length of the string

#for character in string - Iterates over each character in the string

#if substring in string - Checks whether the substring is part of the string

#str_object[start_pos:end_pos:step]

#string[i] - Accesses the character at index i of the string, starting at zero

#string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, the value will default to len(string).

#String methods
#string.lower() - Returns a copy of the string with all lowercase characters

#string.upper() - Returns a copy of the string with all uppercase characters

#string.lstrip() - Returns a copy of the string with the left-side whitespace removed

#string.rstrip() - Returns a copy of the string with the right-side whitespace removed

#string.strip() - Returns a copy of the string with both the left and right-side whitespace removed

#string.count(substring) - Returns the number of times substring is present in the string

#string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.

#string.isalpha() - Returns True if there are only alphabetic characters in the string. If not, returns False.

#string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)

#string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter

#string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.

#delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter 

#Check out the official documentation for 
#all available String methods.  https://docs.python.org/3/library/stdtypes.html#string-methods

######################################################################################################################################################


#FORMATTING STRINGS GUIDE
#
#Python offers different ways to format strings. In the video, we explained the format() method. In this reading, we'll highlight three different ways of formatting strings. For this course you only need to know the format() method. But on the internet, you might find any of the three, so it's a good idea to know that the others exist.
#
#Using the format() method
#The format method returns a copy of the string where the {} placeholders have been replaced with the values of the variables. These variables are converted to strings if they weren't strings already. Empty placeholders are replaced by the variables passed to format in the same order.
#
#
## "base string with {} placeholders".format(variables)
#
#example = "format() method"
#
#formatted_string = "this is an example of using the {} on a string".format(example)
#
#print(formatted_string)
#
#"""Outputs:
#this is an example of using the format() method on a string
#"""
#
#If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).
#
## "{0} {1}".format(first, second)
#
#first = "apple"
#second = "banana"
#third = "carrot"
#
#formatted_string = "{0} {2} {1}".format(first, second, third)
#
#print(formatted_string)
#
#"""Outputs:
#apple carrot banana
#"""
#
#If the placeholders indicate a field name, they’re replaced by the variable corresponding to that field name. This means that parameters to format need to be passed indicating the field name.
#
#"{:exp1} {:exp2}".format(value1, value2)
#
#If the placeholders include a colon, what comes after the colon is a formatting expression. See below for the expression reference.
#
#Formatting expressions
#Expr
#
#Meaning
#
#Example
#
#{:d}
#
#integer value
#
#'{:d}'.format(10.5) → '10'
#
#{:.2f}
#
#floating point with that many decimals
#
#'{:.2f}'.format(0.5) → '0.50'
#
#{:.2s}
#
#string with that many characters
#
#'{:.2s}'.format('Python') → 'Py'
#
#{:<6s}
#
#string aligned to the left that many spaces
#
#'{:<6s}'.format('Py') → 'Py    '
#
#{:>6s}
#
#string aligned to the right that many spaces
#
#'{:>6s}'.format('Py') → '    Py'
#
#{:^6s}
#
#string centered in that many spaces
#
#'{:^6s}'.format('Py') → '  Py  '
################################################################

# Reverse a String using Slicing

print("###############################");
print(" Reverse a String using Slicing");	

test= "this is the string";
test_1= test[::-1];
test_2='';

count = len(test);
print(count);



print(test_2)
######################################################

print("###############################");
print("is_palindrome");	
	

def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""


    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":

            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string =new_string + letter
            reverse_string =letter + reverse_string

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code. 


    if new_string.upper()==reverse_string.upper():

        # If True, the "input_string" contains a palindrome.
        return True
		
    # Otherwise, return False.
    return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

######################################################

print("###############################");
print("format 1 decimal");	


def convert_distance(miles):
    km = miles * 1.6 
    result = "{:6.1f} miles equals {:12.5f} km".format(miles,km)
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

######################################################

print("###############################");
print("string slicing");	

string = 'Rainfall is wet'

convert_string = string[::-1]

print(string);
print(" ");
print(convert_string);


######################################################

print("###############################");
print("replace string at the end by list method");
print(" ")


def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    str = sentence.split();

# i think we have converted string into list that is why the assignment is possible

    if old == str[-1]:
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        str[-1] = new 
        str_test = ""
        for i in str:
            # print(i);
            # print(" ")
            str_test = str_test + i + " "
        # print(str_test)
        

        # here last substring in string is calculated by str[-1:] 
        # print(str); #["It's", 'raining', 'cats', 'and', 'cats']
        # print(str[-1]); #cats last string


        new_sentence = str_test
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
#  Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
#  Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


# string_test = "It's raining cats and cats";

# print(string_test.split()) ;

# print(string_test.replace("cats", "dogs"));


######################################################

print("###############################");
print("replace string at the end by Naive Method");
print(" ")


def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 


# i think we have converted string into list that is why the assignment is possible

    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        
        i = len(old)

        new_sentence = sentence[:-i] + new
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
#  Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
#  Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


# string_test = "It's raining cats and cats";

# print(string_test.split()) ;

# print(string_test.replace("cats", "dogs"));



# Modifying Lists
# While lists and strings are both sequences, a big difference between them is that lists are mutable. This means that the contents 
# of the list can be changed, unlike strings, which are immutable.
#  You can add, remove, or modify elements in a list.

# You can add elements to the end of a list using the append method. You call this method on a list using dot notation, 
# and pass in the element to be added as a parameter. For example, list.append("New data") would add the string "New data" 
# to the end of the list called list.

# If you want to add an element to a list in a specific position, you can use the method insert. The method takes two parameters:
# the first specifies the index in the list, and the second is the element to be added to the list. So list.insert(0, "New data")
#  would add the string "New data" to the front of the list. This wouldn't overwrite the existing element at the start of the list.
#  It would just shift all the other elements by one. If you specify an index that’s larger than the length of the list,
#  the element will simply be added to the end of the list.

# You can remove elements from the list using the remove method. This method takes an element as a parameter, and removes the first 
# occurrence of the element. If the element isn’t found in the list, you’ll get a ValueError error explaining that the element 
# was not found in the list.

# You can also remove elements from a list using the pop method. This method differs from the remove method in that it takes
#  an index as a parameter, and returns the element that was removed. This can be useful if you don't know what the value is, 
# but you know where it’s located. This can also be useful when you need to access the data and also want to remove it from 
# the list.

# Finally, you can change an element in a list by using indexing to overwrite the value stored at the specified index.
#  For example, you can enter list[0] = "Old data" to overwrite the first element in a list with the new string "Old data".




# As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable.
# Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, 
# since they can contain elements of any data type. But unlike lists, tuples are immutable. They’re specified using parentheses 
# instead of square brackets.

# You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when we need to ensure that an element is in a certain position and will not change. Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking. 
# This allows you to take multiple returned values from a function and store each value in its own variable.




# list append in python

######################################################

print("###############################");
print("Complete the skip_elements function to return every other element from the list");
print(" ")



def skip_elements(elements):
    # code goes here
    list = [] 
    for i,element in enumerate(elements):
        if(i%2==0):
            list.append(elements[i])
    return list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


# Iterating Over Lists Using Enumerate
# When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, 
# exposing the element to the for loop as a variable. But what if you want to access the elements in a list, along with 
# the index of the element in question? You can do this using the enumerate() function. The enumerate() function takes 
# a list as a parameter and returns a tuple for each element in the list. 
# The first value of the tuple is the index and the second value is the element itself.

# List Comprehension with Conditional Statement
    
# [ x for x in range(1,101) if x % 10 == 0 ] generates a new list containing all the integers divisible by 10 from 1 to 100. 


# Knowledge
# Common sequence operations
# Lists and tuples are both sequences and they share a number of sequence operations. The following common sequence operations
#  are used by both lists and tuples:

# len(sequence) - Returns the length of the sequence.

# for element in sequence - Iterates over each element in the sequence.

# if element in sequence - Checks whether the element is part of the sequence.

# sequence[x] - Accesses the element at index [x] of the sequence, starting at zero

# sequence[x:y] - Accesses a slice starting at index [x], ending at index [y-1]. If [x] is omitted, the index will start at 0 by default. If [y] is omitted, the len(sequence) will set the ending index position by default.

# for index, element in enumerate(sequence) - Iterates over both the indices and the elements in the sequence at the same time.

# List-specific operations and methods
# One major difference between lists and tuples is that lists are mutable (changeable) and tuples are immutable (not changeable). 
# There are a few operations and methods that are specific to changing data within lists:

# list[index] = x - Replaces the element at index [n] with x.

# list.append(x) - Appends x to the end of the list.

# list.insert(index, x) - Inserts x at index position [index].

# list.pop(index) - Returns the element at [index] and removes it from the list. If [index] position is not in the list,
#  the last element in the list is returned and removed.

# list.remove(x) - Removes the first occurrence of x in the list.

# list.sort() - Sorts the items in the list.

# list.reverse() - Reverses the order of items of the list.

# list.clear() - Deletes all items in the list.

# list.copy() - Creates a copy of the list.

# list.extend(other_list) - Appends all the elements of other_list at the end of list

# List comprehensions
# A list comprehension is an efficient method for creating a new list from a sequence or a range in a single line of code. 
# It is a best practice to add descriptive comments about any list comprehensions used in your code, as their purpose can
#  be difficult to interpret by other coders.

# [expression for variable in sequence] - Creates a new list based on the given sequence. Each element in the new list is the result of the given expression.

# Example: my_list = [ x*2 for x in range(1,11) ]

# [expression for variable in sequence if condition] - Creates a new list based on a specified sequence. Each element is the result of the given expression; elements are added only if the specified condition is true. 

# Example: my_list = [ x for x in range(1,101) if x % 10 == 0 ]

# Use the list.append(old,new) method.

# Use the string.endswith() and string.replace()

# string.split()  given_string.split()

#  string.join()   ", ".join(elements)



######################################################

print("###############################");
print("replace hpp with h");
print(" ")


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
 
newfilenames =[] ;

temp = [] ;

temp_string =" ";

count = 0 ;

for element in filenames:
    
    temp = element.split(".");  #returns the list

    if( temp[1] =='hpp' ):
        
        temp[1] = 'h'
        
        temp_string = temp[0]+'.'+temp[1];
        
        newfilenames.append(temp_string)
    
    else:
        newfilenames.append(element) 
        
        
        
print(newfilenames) 

        
       
# for i,element in enumerate(filenames):
#             print(i)
#             newfilenames.append(filenames[i])


# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "v.out"]


######################################################

print("###############################");
print("pig_latin");
print(" ")


def pig_latin(text):
  
  say = "" ;
  # Separate the text into words

  words = text.split();

  temp = [];

  str_test = "" ;

  for word in words:
    # Create the pig latin word and add it to the list
    say = word[1:] + word[0] + "ay"
    temp.append(say)

  str_test = " ".join(temp) # converting list back to string by joining
 

#   print(str_test)
    
    
    # Turn the list back into a phrase
  return str_test
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



######################################################

print("###############################");
print("list string");
print(" ")

def group_list(group, users):
#   list = []
#   list = users.split()
# can not use that as split function  works on string not list
# but in ear;ier query we have join list back to string
#   temp_str ="";
#   temp_str = ",".join(users);  #list to string vi join it works

  members = group + ": "+", ".join(users);
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"



######################################################

print("###############################");
print("list string  list of the tuple");
print(" ")

def guest_list(guests):
    for element in guests:
        print("{0} is {1} years old and work as {2}".format(element[0],element[1],element[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""


# Iterating Over Dictionaries
# You can iterate over dictionaries using a for loop, just like with strings, lists, 
# and tuples. This will iterate over the sequence of keys in the dictionary. If you want to access the corresponding values 
# associated with the keys, you could use the keys as indexes. Or you can use the items method on the dictionary, like dictionary.
# items(). This method returns a tuple for each element in the dictionary, where the first element in the tuple is the key and 
# the second is the value.

# If you only wanted to access the keys in a dictionary, you could use the keys() 
# method on the dictionary: dictionary.keys(). If you only wanted the values, you could use the values() method: dictionary.values()




# Python dictionaries are used to organize elements into collections. Dictionaries include one or more keys, with one or more 
# values associated with each key. 

# my_dictionary = {keyA:value1,value2, keyB:value3,value4}


# len(dictionary) - Returns the number of items in a dictionary.

# for key, in dictionary - Iterates over each key in a dictionary.

# for key, value in dictionary.items() - Iterates over each key,value pair in a dictionary.

# if key in dictionary - Checks whether a key is in a dictionary.

# dictionary[key] - Accesses a value using the associated key from a dictionary.

# dictionary[key] = value - Sets a value associated with a key.

# del dictionary[key] - Removes a value using the associated key from a dictionary.


# Methods
# dictionary.get(key, default) - Returns the value corresponding to a key, or the default value if the specified key is not present.

# dictionary.keys() - Returns a sequence containing the keys in a dictionary.

# dictionary.values() - Returns a sequence containing the values in a dictionary.

# dictionary[key].append(value) - Appends a new value for an existing key.

# dictionary.update(other_dictionary) - Updates a dictionary with the items from another dictionary. Existing entries are updated; new entries are added.

# dictionary.clear() - Deletes all items from a dictionary.

# dictionary.copy() - Makes a copy of a dictionary.



# Dictionaries versus Lists 
# Dictionaries are similar to lists, but there are a few differences:

# Both dictionaries and lists:
# are used to organize elements into collections;

# are used to initialize a new dictionary or list, use empty brackets;

# can iterate through the items or elements in the collection; and

# can use a variety of methods and operations to create and change the collections, like removing and inserting items or elements.

# Dictionaries only:
# are unordered sets;

# have keys that can be a variety of data types, including strings, integers, floats, tuples;.

# can access dictionary values by keys;

# use square brackets inside curly brackets { [ ] };

# use colons between the key and the value(s);

# use commas to separate each key group and each value within a key group;

# make it quicker and easier for a Python interpreter to find specific elements, as compared to a list.

# Dictionary Example:
# 123456
# pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  


# print(pet_dictionary.get("dogs", 0))
# # Should print ['Yorkie', 'Collie', 'Bulldog']

# Reset
# Lists only:
# are ordered sets;

# access list elements by index positions;

# require that these indices be integers;

# use square brackets [ ];

# use commas to separate each list element.

######################################################

print("###############################");
print("dict domian and email key value pair");
print(" ")

def email_list(domains): # domains is dict 
    emails = []
    for key, value in domains.items():
            # print("Key")
            # print(key)
            # print(domains[key]) # accessing value in dict through key ALL values for certain key
            # print(domains[key][0]) # accessing first value of each key in dict
            # print(" ")
            # print(" ")
        # for element in domains[key]:# iterating over all values for each individual 
        #     print(element)
            users = domains[key]
            for user in users:  # iterating over all values for each individual 
                # print(user)
                # print(user+"@"+key)
                emails.append(user+"@"+key)
    return (emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

######################################################

print("###############################");
print("dict reversing key value");
print(" ")

def groups_per_user(group_dictionary):
    user_groups = {};
    for key , value  in group_dictionary.items():
        # print(key)
        # print(group_dictionary[key])  # same as print(value)
        # print(group_dictionary.keys())
        # user_groups[value] = key # unhashable type: 'list'
        
        print(key,value) # prints key value pair

        for element in value:
            # print(" ")
            # print(element) # value is list 

            # adding new key value to dict
            # user_groups[element] = []
            

            if element in user_groups:
                print('yes')
                print(element)
                user_groups[element].append(key)  #Appends a new value for an existing key.
                print('')

            if element not in user_groups:
                user_groups[element] = [key]
            
            print(user_groups)
            print(" ")
        # user_groups[element].append(key) #str' object has no attribute 'append
            
        print(" ")
    print("test")
    print(user_groups)




	# return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))



print("###############################");
print("dict reversing key value group and user easy version");
print(" ")

def groups_per_user(group_dictionary):
    user_groups = {};
    for key , value  in group_dictionary.items():
        # print(key,value) # prints key value pair

        for element in value:

            if element in user_groups:
                user_groups[element].append(key)  #Appends a new value for an existing key.

            if element not in user_groups:
                user_groups[element] = [key]
             
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))





# dictionary.update(other_dictionary) - 
# Updates a dictionary with the items from another dictionary. Existing entries are updated; new entries are added.
print("###############################");
print("dictionary.update");
print(" ")
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

# {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}


# It’s quicker and easier to find a specific element in a dictionary


# Study Guide: Week 4 Graded Quiz
#  It is time to prepare for the Week 4 Graded Quiz. Please review the following items from this module before
#  beginning the quiz. If you would like to refresh your memory on these materials, please also revisit the Study 
# Guides located before each practice quiz in Week 4: 
# Study Guide: Strings
# ,  
# Study Guide: Lists Operations and Methods
# , and 
# Study Guide: Dictionary Methods
# .


# Knowledge
# How to output a list of the keys in a Python dictionary. 

# How to determine the output of a string index range used on a string.

# Determine what a list should contain after the .insert() method is used on the list.

# How to replace a specific word in a sentence with the same word in all uppercase letters.

# How to use a dictionary to count the frequency of letters in a string. 

# Operations, Methods, and Functions
# String Methods, Operations, and Functions

# .upper()

# .lower()

# .split()

# .format()

# .isnumeric()

# .isalpha()

# .replace()

# string index [ ]

# len()

# List Operations and Methods

# .reverse()

# .extend()

# .insert()

# .append()

# .remove()

# .sort()

# list comprehensions [ ]

# list comprehensions [ ] with if condition

# Dictionary Operations and Methods

# .items()

# .update()

# .keys()

# .values()

# .copy()

# dictionary[key]

# dictionary[key] = value 



# Coding Skills
# Skill 1: Using string methods
# Separate numerical values from text values in a string using .split(). 

# Iterate over the elements in a string.

# Test if the element contains letters with .isalpha().

# Assign the elements of the split string to new variables.

# Trim any extra white space using .strip().

# Format a string using .format() and { } variable placeholders.

# 1234567891011121314151617181920212223242526272829303132
# def sales_prices(item_and_price):
#     # Initialize variables "item" and "price" as strings
#     item = ""
#     price = ""
#     # Create a variable "item_or_price" to hold the result of the split. 
#     item_or_price = item_and_price.split()

#     # For each element "x" in the split variable "item_or_price" 
#     for x in item_or_price:


# Reset

# Use the len() function to measure a string.

# 1234567891011121314151617
# # This function accepts a string variable "data_field".  
# def count_words(data_field):

#     # Splits the string into individual words. 
#     split_data = data_field.split()
  
#     # Then returns the number of words in the string using the len()
#     # function. 
#     return len(split_data)
    

# Reset
# Skill 2: Using list methods
# Reverse the order of a list using the .reverse() method.

# Combine two lists using the .extend() method.

# 1234567891011121314151617181920212223242526272829
# # This function accepts two variables, each containing a list of years.
# # A current "recent_first" list contains [2022, 2018, 2011, 2006].
# # An older "recent_last" list contains [1989, 1992, 1997, 2001].
# # The lists need to be combined with the years in chronological order.
# def record_profit_years(recent_first, recent_last):

#     # Reverse the order of the "recent_first" list so that it is in 
#     # chronological order.
#     recent_first.reverse()


# Reset

# Skill 3: Using a list comprehension 
# Use a list comprehension [ ] as a shortcut for creating a new list from a range.

# Include a calculation with a for loop in a range with 2 parameters (lower, upper+1). 

# 123456789101112
# # The function accepts two parameters: a start year and an end year.
# def list_years(start, end):

#     # It returns a list comprehension that creates a list of years in a for
#     # loop using a range from the start year to the end year (inclusive of 
#     # the upper range year, using end+1).
#     return [year for year in range(start, end+1)]

def squares(start, end):
    return [ i**2 for i in range(start, end+1)] # Create the required list comprehension.


# # Call the years() function with two parameters.

# Reset

#  Use a list comprehension [ ] with a for loop and an if condition.   

# 12345678910111213141516171819
# # The function accepts two variable integers through the parameters and
# # returns all odd numbers between x and y-1.
# def odd_numbers(x, y):


# # This list comprehension uses a for loop to iterate through values 
# # of n in a range from x to y, with the value of y excluded (meaning
# # keep the default range() function behavior to exclude the
# # end-of-range value from the range). Since an incremental value is not 
# # specified, the range function uses the default increment of +1.

# Reset

# Skill 4: Using dictionary methods
# Iterate through the keys and values of a dictionary.

# Return the keys and values in a formatted string using the .format() function.

# 123456789101112131415161718192021222324252627
# # The network() function accepts a dictionary "servers" as a parameter.
# def network(servers):

#     # A string variable is initialized to hold the "result". 
#     result = ""

#     # For each "hostname" (key) and "IP address" (value) in the "server" dictionary items...
#     for hostname, IP_address in servers.items():

#         # A string identifying the hostname and IP address for each server is added

# Reset

# Create a copy of a dictionary.

# Iterate through the values of the new dictionary.

# Change each value in the new dictionary, while keeping the same keys. 

# 12345678910111213141516171819202122
# # The scores() function accepts a dictionary "game_scores" as a parameter.
# def reset_scores(game_scores):

#     # The .copy() dictionary method is used to create a new copy of the "game_scores".
#     new_game_scores = game_scores.copy() 

#     # The for loop iterates over new_game_scores items, with the player as the key
#     # and the score as the value. 
#     for player, score in new_game_scores.items():
    

# Reset
# Reminder: Correct syntax is critical
# Using precise syntax is critical when writing code in any programming language, including Python. Even a small typo 
# can cause a syntax error and the automated Python-coded quiz grader will mark your code as incorrect. This reflects 
# real life coding errors in the sense that a single error in spelling, case, punctuation, etc. can cause your code to
#  fail. Coding problems caused by imprecise syntax will always be an issue whether you are learning a programming 
# language or you are using programming skills on the job. So, it is critical to start the habit of being precise in your code now. 

# No credit will be given if there are any coding errors on the automated graded quizzes - including minor errors.
#  Fortunately, you have 3 optional retake opportunities on the graded quizzes in this course. Additionally, you have
#  unlimited retakes on practice quizzes and can review the videos and readings as many times as you need to master 
# the concepts in this course.  

# Now, before starting the graded quiz, please review this list of common syntax errors coders make when writing code.

# Common syntax errors:

# Misspellings

# Incorrect indentations

# Missing or incorrect key characters:

# Parenthetical types - ( curved ), [ square ], { curly }

# Quote types - "straight-double" or 'straight-single', “curly-double” or ‘curly-single’

# Block introduction characters, like colons - :

# Data type mismatches

# Missing, incorrectly used, or misplaced Python reserved words

# Using the wrong case (uppercase/lowercase) - Python is a case-sensitive language 

# Resources
# For additional Python practice, the following links will take you to several popular online interpreters and codepads:

# Welcome to Python
 

# Online Python Interpreter
 

# Create a new Repl
 

# Online Python-3 Compiler (Interpreter)

# Compile Python 3 Online

# Your Python Trinket

print("###############################");
print("list sorting");
print(" ")

def sort_distance(distances):
    # Sort the list
    temp = 0
    sort =[]
    size = len(distances)
    for i in range(size):
        for j in range(size):
            if(distances[i]>distances[j]):
                temp = distances[i]
                distances[i]=distances[j]
                distances[j]=temp
    
    print(distances)


                

       
  

    # Reverse the order of the list
    # return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]





print("###############################");
print("dict number of letter in string letter : frequency");
print(" ")



def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for letter in  text :
    
    lower_case_letter = letter.lower()

    # Complete the if-statement using a string method to check if the
    # character is a letter.

    if lower_case_letter.isalpha() :

      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.

        if letter not in dictionary: # key in dict
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
            dictionary[lower_case_letter]=1

        elif letter in dictionary:
            dictionary[lower_case_letter]+=1
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.

      
   # Increment the letter counter. 
  return dictionary



print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}





print("###############################");
print("test");
print(" ")
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for key , value in car_prices.items() :
    result += "A {0} Soul costs {1} dollar \n".format(key,value) # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars




print("###############################");
print("class");
print(" ")

class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "this_pun_is_for_you"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 


# Object-Oriented Programming Defined

# In object-oriented programming, concepts are modeled as classes and objects. 
# An idea is defined using a class, and an instance of this class is called an object.
#  Almost everything in Python is an object, including strings, lists, dictionaries, and numbers.
#  When we create a list in Python, we’re creating an object which is an instance of the list class,
#  which represents the concept of a list. Classes also have attributes and methods associated with them.
#  Attributes are the characteristics of the class, while methods are functions that are part of the class.





# Classes and Objects in Detail

# We can use the type() function to figure out what class a variable or value belongs to. For example, 
# type(" ") tells us that this is a string class. The only attribute in this case is the string value,
#  but there are a bunch of methods associated with the class. We've seen the upper() method, which returns 
#  the string in all uppercase, as well as isnumeric() which returns a boolean telling us whether or not the
#  string is a number. You can use the dir() function to print all the attributes and methods of an object. 
#  Each string is an instance of the string class, having the same methods of the parent class. Since the content 
#  of the string is different, the methods will return different values. You can also use the help() function on an object,
#  which will return the documentation for the corresponding class. This will show all the methods for the class, along with 
#  parameters the methods receive, types of return values, and a description of the methods

print("###############################DATA SCIENCE IBM##################################################");

print("")
#STRING INTERPOLATION (F-STRINGS)
print("#STRING INTERPOLATION (F-STRINGS)")
name = "John"
age = 30
print(f'My name is {name} and I am {age} years old.')


print("")
#str.format()
print("#str.format()")
name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))


# ADDITIONAL CAPABILITIES

#F-strings are also able to evaluate expressions inside the curly braces
print("")
print("F-strings ")
x = 10
y = 20
print(f'The sum of x and y is {x+y}.')

#Raw String (r’’)
#In Python, raw strings are a powerful tool for handling textual data, especially when dealing with escape characters. By prefixing a string literal with the letter ‘r’, Python treats the string as raw, meaning it interprets backslashes as literal characters rather than escape sequences

#Regular string:
print("")
print("#Regular string:")
regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)

#output
#Regular String:  C:
#ew_folderile.txt
print("")
print("#raw_string")
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)

#output
#Raw String: C:\new_folder\file.txt

#STRING MANIPULATION OPERATIONS


#Slice
#Stride -name[::2] --steps
print("")
name = "Michael Jackson"
name.find('el')
#output 5
#searching index of sub string in the string

#g.replace("Mary","Bob")


#RegEx

#In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings.
#This RegEx module provides several functions for working with regular expressions, including search, split, findall, and sub.
#Python provides a built-in module called re, which allows you to work with regular expressions. First, import the re module
print("")
print("#RegEx in python")
import re
s1 = "Michael Jackson is the best"

## Define the pattern to search for
pattern = r"Jackson"

## Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

## Check if a match was found
if result:
    print("Match found!")
#else:
    print("Match not found.")

print("")
print("# Matches any ten consecutive digits")
import re
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
	

#--findall
print("")
print("#--findall")
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

#--output
#Matches: [',', ' ', '!']
#
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

print("")
# Print out the list of matched words
print(result)


# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

print("")
# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 

#Michael Jackson was a singer and known as the 'legend'


#---------------------
#split the substring to list:
# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.

print("")
#FIND()
#The find() method finds the first occurrence of the specified value.

#The find() method returns -1 if the value is not found.

#The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)

#Syntax
#string.find(value, start, end)

#Parameter Values

#Parameter	Description
#value		Required. The value to search for
#start		Optional. Where to start the search. Default is 0
#		end Optional. Where to end the search. Default is to the end of the string
			
#txt = "Hello, welcome to my world."

#x = txt.find("e", 5, 10)

#print(x)

#--output
#8
#=======================LIST
#OBJECTIVE
#Perform list operations in Python, including indexing, list manipulation, and copy/clone list.


#Extend vs append
print("")
print("#Extend vs append")

print("")
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

print("")
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)

#extend to add new elements to the list:
#If we apply append instead of extend, we add one element to the list


# Copy (copy by reference) the list A
print("")
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# When we set one variable B equal to A, both A and B are referencing the same list in memory:

# Examine the copy by reference

print("")
print("# Examine the copy by reference")
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A

print("")
print("# Clone (clone by value) the list A")
B = A[:]
print(B)

print("")
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

# concatenate lists 
print("")
print("# concatenate lists ")
A = [1, 'a'] 
B = [2, 1, 'd']
C= A+B 
print(C)

#=========================Tuple
# Perform the basics tuple operations in Python, including indexing, slicing and sorting
print("")
tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco") 
tuple.index("disco")
print("disco".index("s"))
print("disco".find('s'))

print("")
C_tuple=(-5, 1, -3)
sorted_C_tuple = sorted (C_tuple)
print(sorted_C_tuple)

# tuple is immutable
# here new object is created which is ref by sorted_C_tuple

# Dictionaries 
# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.

print("")
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)
# The keys can be strings
# Keys can also be any immutable object such as a tuple

# Get all the keys in dictionary
# release_year_dict.keys() 

# Get all the values in dictionary
# release_year_dict.values() 

# Verify the key is in the dictionary
#'The Bodyguard' in release_year_dict


# syntax to extract the KEYS OF A DICTIONARY AS A LIST
#list(dict.keys())


#=================SET
# unordered 
# unique ,no duplicate
# set(list)
# A.add("str")
# set operations


#syntax is helpful to CLONE LIST A and assign the result to list B
# B=A[:]


# LOOPING

print("")
print("# LOOPING")
list = ["red","yellow","green"]
for i, element in enumerate(list):
	print(i,end = " ")
	print(element)
	
# Loop through the list and iterate on both index and element value

print("")
print("Loop through the list")
squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
    
 # FUNCTIONS
 
 # Example of global variable

print("")
print("# FUNCTIONS")
artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) 

#COLLECTIONS AND FUNCTIONS
#When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:

print("")
print("#COLLECTIONS AND FUNCTIONS *args dynamic arguments")
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


print("")
print("**args dict")
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')


# SORT VS SORTED FUNCTION IN PYTHON
# sort() will sort the list in-place, mutating its indexes and returning None , whereas sorted() will return a new sorted list leaving the original list unchanged


# EXCEPTION HANDLING
   
# try:
# except:
# else:
# finally:

#Python tries to execute the code in the try block. In this case if there is any exception raised by the code in the try block, it will be caught and the code block in the except block will be executed. After that, the code that comes after the try except will be executed.

print("")
print("# EXCEPTION HANDLING")

a = 1

try:
    b = int(input("Please enter a number to divide a "))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        
 # Try Except Specific Example
a = 1

print("")
print("# EXCEPTION HANDLING WITH ERROR")
try:
    b = int(input("Please enter a number to divide a "))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
    
# if there is an error the value of a is always printed. Let's use the else and print the value of a only if there is no error.

print("")
print("# EXCEPTION HANDLING WITH ERROR AND ELSE")

a = 1

try:
    b = int(input("Please enter a number to divide a "))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
    
# finally

print("")
print("# EXCEPTION HANDLING WITH FINALLY")
 
a = 1

try:
    b = int(input("Please enter a number to divide a "))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
    


 # class and objects
 # functions and method
 # attributes and objects
 
print("")
print("# CLASS AND OBJECTS")

class circle (object):
    
    def __init__(self, radius, color):# specail method or constructor used to initalize some data attributes
        self.radius = radius
        self.color = color
        
redCircle = circle(10,"red")
c1 = circle(10,'red')
c1.radius # 10
 
 # METHOD
 
 # EXAMPLE
 
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h
    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0
    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
        

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Accelerate the cars
car1.accelerate(30)
car2.accelerate(20)

# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")


###########################################################################

# PROGRAM TO CALCULATE FREQ OF WORDS IN STRING

print("")
#Press Shift+Enter to run the code
givenString="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

fmtText = givenString.split() # spliting string into words 
print(type(fmtText)) # split will return list

listTemp = fmtText # copying main list to listTemp

print("# PROGRAM TO CALCULATE FREQ OF WORDS IN STRING")
dict = {}


for i in listTemp:
    count=0
    for j in fmtText:
        if(i==j):
            count+=1
    dict[i]=count # adding elements in dict

print(dict)
    
    
###########################################################################

# CLASS AND METHOD TO CALCULATE FREQ OF ALL WORDS IN STRING

print("")
print("# CLASS AND METHOD TO CALCULATE FREQ OF ALL WORDS IN STRING")
 
class TextAnalyzer(object):
    
    def __init__ (self, text):
        newtext = text.replace(',','').replace('.','').replace('?','').replace('!','') # remove punctuation
        newtext = newtext.lower()# make text lowercase
        self.newtext  = newtext
    
    def freqAll(self):        
        
        fmtText = self.newtext.split()    # split text into words    
        
        listTemp = fmtText # copying main list to listTemp
        
        dict = {} # Create dictionary

        for i in listTemp:
            count=0
            for j in fmtText:
                if(i==j):
                    count+=1
            dict[i]=count # adding elements in dict
        return dict
    

givenString="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

object1  =  TextAnalyzer(givenString)

print(object1.freqAll())

print("")
print("case1:-variable assignment in python class")
class Points(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 


p2 = Points(1, 2) 
p2.x = 2 

print("")
print("case2:-variable assignment in python class")
class Points(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 


p2 = Points(1, 2) 
p2.x = 'A' 
p2.print_point()


# PROGRAM TO CALCULATE FREQ OF WORDS IN STRING

#Press Shift+Enter to run the code
givenString="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

fmtText = givenString.split() # spliting string into words 
print(type(fmtText)) # split will return list

print(fmtText)

listTemp = fmtText # copying main list to listTemp

dict = {}


for i in listTemp:
    count=0
    for j in fmtText:
        if(i==j):
            count+=1
    dict[i]=count # adding elements in dict

print(dict)
    
    
 ===============================================================
 
 #Press shift+Enter to run the code
class TextAnalyzer(object):
    
    def __init__ (self, text):
         # remove punctuation
        newtext = text.replace(',','').replace('.','').replace('?','').replace('!','')
        # make text lowercase
        mewtext = newtext.lower()
        self.newtext  = newtext
        
    def freqAll(self):        
        # split text into words
        fmttext = newtext.split()        
        # Create dictionary
        listTemp = fmtText 
        
        # copying main list to listTemp
        
        dict = {}
        for i in listTemp:
            count=0
            for j in fmtText:
                if(i==j):
                    count+=1
            dict[i]=count # adding elements in dict
        return dict
# FILE HANDLING:

# Copy file to another

#with open('/Example2.txt','r') as readfile:
#    with open('/Example3.txt','w') as writefile:
#          for line in readfile:
#                writefile.write(line)

# PANDAS

# Dataframe
# one of the ways pandas deals with data is in DATAFRAME
# other way is SERIES

#import pandas as pd

#Csv_path = "file.csv"
#df = pd.read_csv(Csv_path)
#df.head()

#xlsx_path  = "file2.xlsx"
#df = pd.read_excel(xlsx_path)
#df.head()

# data frame from dict

import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)


#	Name	ID	Department	    Salary
#0	Rose	1	Architect Group	100000
#1	John	2	Software Group	80000
#2	Jane	3	Design Team	    50000
#3	Mary	4	Infrastructure	60000

import pandas as pd
dict = {'Student':['David','Samuel','Terry','Evan'], 'Age':['27','24','22','32'], 'Country' :['UK','Canada','China','USA'], 'Course':['Python','Data Structures','Machine learning','Web Development'], 'Marks':['85','72','89','76']}
df = pd.DataFrame(dict)
print(df)

#-output
#  Student Age Country            Course Marks
#0   David  27      UK            Python    85
#1  Samuel  24  Canada   Data Structures    72
#2   Terry  22   China  Machine learning    89
#3    Evan  32     USA   Web Development    76

b = df[['Marks']]
print(b)

c = df[['Country','Course']]
print(c)


#PANDAS

#loading web file csv into dataframe

import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"

df = pd.read_csv(filename)

print(df)

# Print first five rows of the dataframe

first_5_rows = df.head()

print(first_5_rows)

y = df[['Artist','Length','Genre']]
print(y)

# Access the value on the first row and the first column

print(df.iloc[0, 0])

#df.ix[0,0]

# Slicing the dataframe

print(df.iloc[0:2, 0:3])



#loading xlsx file to dataframe in pandas

# Dependency needed to install file 

# If running the notebook on your machine, else leave it commented

# !pip install xlrd
# !pip install openpyxl 
# import piplite
# await piplite.install(['xlrd','openpyxl'])


# note for xlxs file loading we find XLRD and OPENPYXL and of course PANDAS


#import pandas as pd

#xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'

#df = pd.read_excel(xlsx_path)

#print(df)


# FOR READING SPECIFIC SHEETS
# xls = pd.ExcelFile('path_to_file.xls')
# df1 = pd.read_excel(xls, 'Sheet1')
# df2 = pd.read_excel(xls, 'Sheet2')


# NUMPY
# Python library serves as a foundation for Pandas and is used for scientific computing?

#Python and it is an open source project. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

import numpy as np 

a = np.array([0, 1, 2, 3, 4])

print(a)

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(type(a))

#numpy.ndarray


#2_D Array

import numpy as np

# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

print(a)

# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
print(A)
 
# Show the numpy array dimensions
# ndim to obtain the number of axes or dimensions, referred to as the rank

print(A.ndim)

# Show the numpy array shape
# Attribute shape returns a tuple corresponding to the size or number of each dimension.

print(A.shape)

# Show the numpy array size
# The total number of elements in the array is given by the attribute size.

print(A.size)

# ACCESSING DIFFERENT ELEMENTS OF A NUMPY ARRAY

# Access the element on the second row and third column

print('A[1, 2] ',A[1, 2])

# Access the element on the second row and third column

print('A[1][2] ',A[1][2])

# Access the element on the first row and first column

print('A[0][0]',A[0][0])

# Access the element on the first row and first and second columns

print(A[0][0:2])

# Access the element on the first and second rows and third column

print(A[0:2, 2])


# Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])
print('A',A)

# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])
print('B',B)

# Calculate the dot product

Z = np.dot(A,B)
print('Dot product of A and B',Z)

# Calculate the sine of Z

print(np.sin(Z))

# Create a matrix C
# transposed

C = np.array([[1,1],[2,2],[3,3]])
print(C)
print(C.T)


#exercise

import numpy as np

X=np.array([[1,0,1],[2,2,2]]) 

print(X)

#[[1 0 1]
# [2 2 2]]

out=X[0:2,2]

print(out)

#[1 2]


# API
#An API lets two pieces of software talk to each other. Just like a function, you don't have to know how the API works, only its inputs and outputs. An essential type of API is a REST API that allows you to access resources via the internet.

#API Libraries
#REST API ->Request and Response
#Rest APIs are another popular type if API; they allow you to communicate through the internet
#This aloows you to take advantage of resources like storage , access more data , artificial intelligence algorithms

#REST -> REpresentational State Transfer APIs

#HTTP methods are a way of transmitting data over the internet.
#HTTP
#RequestJSON:like Dictionary

# Pandas is an API

#Pandas is actually set of software components , much of which is not even written in Python.

import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
type(df)

# When you create a Pandas object with the dataframe constructor, in API lingo this is an "instance". The data in the dictionary is passed along to the pandas API. You then use the dataframe to communicate with the API.

# REST APIs 
# Rest APIs function by sending a request, the request is communicated via HTTP message. The HTTP message usually contains a JSON file. This contains instructions for what operation we would like the service or resource to perform. In a similar manner, API returns a response, via an HTTP message, this response is usually contained within a JSON.

# USING APIs

# first install APIs to use

# example this NBA API by cmd

# pip install nba_api

# The method get_teams() returns a list of dictionaries.

# nba_teams = teams.get_teams()

# nba_teams is the list of Dictionary

# print(nba_teams[0:3])

# output #JSON
# [{'id': 1610612737, 'full_name': 'Atlanta Hawks', 'abbreviation': 'ATL', 'nickname': 'Hawks', 'city': 'Atlanta', 'state': 'Georgia', 'year_founded': 1949}, {'id': 1610612738, 'full_name': 'Boston Celtics', 'abbreviation': 'BOS', 'nickname': 'Celtics', 'city': 'Boston', 'state': 'Massachusetts', 'year_founded': 1946}, {'id': 1610612739, 'full_name': 'Cleveland Cavaliers', 'abbreviation': 'CLE', 'nickname': 'Cavaliers', 'city': 'Cleveland', 'state': 'Ohio', 'year_founded': 1970}]

# DICT COMPREHENSION
# Using fromkeys() Method
dic=dict.fromkeys(range(5), True)
print(dic)

# Using dictionary comprehension make dictionary
# # creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)

sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)



# print("API DATA HANDLING IN PYTHON")

from nba_api.stats.static import teams
import matplotlib.pyplot as plt
import pandas as pd

nba_teams = teams.get_teams()

def one_dict(list_dict):
    
    keys=list_dict[0].keys() # this is dict keys <class 'dict_keys'> 
    # dict_keys(['id', 'full_name', 'abbreviation', 'nickname', 'city', 'state', 'year_founded'])
    # this will store keys of first elemnet of nba_teams to keys and as all keys are common
    
    out_dict={key:[] for key in keys} 
    
    #out_dict = {'id': [], 'full_name': [], 'abbreviation': [], 'nickname': [], 'city': [], 'state': [], 'year_founded': []} 
    
    #DICTIONARY COMPREHENSION
    # keys = ['a','b','c','d','e']
    # values = [1,2,3,4,5]  
    # myDict = { k:v for (k,v) in zip(keys, values)}  
    # We can use below too
    # myDict = dict(zip(keys, values))  
    # print (myDict)
    
    # LIST COMPREHENSION  
    # newlist = [expression for item in iterable if condition == True]
    # example
    # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    # newlist = [x for x in fruits if "a" in x]
    # print(newlist)
    
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict
    
    # values are added to each keys
    # output print(out_dict)
    # {'id': [1610612737, 1610612738, 1610612739, 1610612740, 1610612741, 1610612742, 1610612743, 1610612744, 1610612745, 1610612746, 1610612747, 1610612748, 1610612749, 1610612750, 1610612751, 1610612752, 1610612753, 1610612754, 1610612755, 1610612756, 1610612757, 1610612758, 1610612759,    1610612760, 1610612761, 1610612762, 1610612763, 1610612764, 1610612765, 1610612766], 'full_name': ['Atlanta Hawks', 'Boston Celtics', 'Cleveland Cavaliers', 'New Orleans Pelicans', 'Chicago Bulls', 'Dallas Mavericks', 'Denver Nuggets', 'Golden State Warriors', 'Houston Rockets', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'Brooklyn Nets', 'New York Knicks', 'Orlando Magic', 'Indiana Pacers', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Oklahoma City Thunder', 'Toronto Raptors', 'Utah Jazz', 'Memphis Grizzlies', 'Washington Wizards', 'Detroit Pistons', 'Charlotte Hornets'], 'abbreviation': ['ATL', 'BOS', 'CLE', 'NOP', 'CHI', 'DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL', 'MIA', 'MIL', 'MIN', 'BKN', 'NYK', 'ORL', 'IND', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'OKC', 'TOR', 'UTA', 'MEM', 'WAS', 'DET', 'CHA'], 'nickname': ['Hawks', 'Celtics', 'Cavaliers', 'Pelicans', 'Bulls', 'Mavericks', 'Nuggets', 'Warriors', 'Rockets', 'Clippers', 'Lakers', 'Heat', 'Bucks', 'Timberwolves', 'Nets', 'Knicks', 'Magic', 'Pacers', '76ers', 'Suns', 'Trail Blazers', 'Kings', 'Spurs', 'Thunder', 'Raptors', 'Jazz', 'Grizzlies', 'Wizards', 'Pistons', 'Hornets'], 'city': ['Atlanta', 'Boston', 'Cleveland', 'New Orleans', 'Chicago', 'Dallas', 'Denver', 'Golden State', 'Houston', 'Los Angeles', 'Los Angeles', 'Miami', 'Milwaukee', 'Minnesota', 'Brooklyn', 'New York', 'Orlando', 'Indiana', 'Philadelphia', 'Phoenix', 'Portland', 'Sacramento', 'San Antonio', 'Oklahoma City', 'Toronto', 'Utah', 'Memphis', 'Washington', 'Detroit', 'Charlotte'], 'state': ['Georgia', 'Massachusetts', 'Ohio', 'Louisiana', 'Illinois', 'Texas', 'Colorado', 'California', 'Texas', 'California', 'California', 'Florida', 'Wisconsin', 'Minnesota', 'New York', 'New York', 'Florida', 'Indiana', 'Pennsylvania', 'Arizona', 'Oregon', 'California', 'Texas', 'Oklahoma', 'Ontario', 'Utah', 'Tennessee', 'District of Columbia', 'Michigan', 'North Carolina'], 'year_founded': [1949, 1946, 1970, 2002, 1966, 1980, 1976, 1946, 1967, 1970, 1948, 1988, 1968, 1989, 1976, 1946, 1989, 1976, 1949, 1968, 1970, 1948, 1976, 1967, 1995, 1974, 1995, 1961, 1948, 1988]} 
    
dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team) # THIS ABOVE dICT IS CONVERTED INTO DATAFRAME
print(df_teams.head()) # 5 rows

#       id             full_name     abbreviation   nickname         city          state  year_founded
#0  1610612737         Atlanta Hawks          ATL      Hawks      Atlanta        Georgia          1949
#1  1610612738        Boston Celtics          BOS    Celtics       Boston  Massachusetts          1946
#2  1610612739   Cleveland Cavaliers          CLE  Cavaliers    Cleveland           Ohio          1970
#3  1610612740  New Orleans Pelicans          NOP   Pelicans  New Orleans      Louisiana          2002
#4  1610612741         Chicago Bulls          CHI      Bulls      Chicago       Illinois          1966


df_warriors=df_teams[df_teams['nickname']=='Warriors']
print(df_warriors)

#        id              full_name abbreviation  nickname          city       state  year_founded
#7  1610612744  Golden State Warriors          GSW  Warriors  Golden State  California          1946

id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
print(id_warriors)
# 1610612744


#The function "League Game Finder " will make an API call, it's in the module stats.endpoints.
#The parameter team_id_nullable is the unique ID for the warriors. Under the hood, the NBA API is making a HTTP request.
#The information requested is provided and is transmitted via an HTTP response this is assigned to the object game finder.


# CAN NOT ABLE TO FIGURE IT OUT
#from nba_api.stats.endpoints import leaguegamefinder
#
## Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
## The following code is commented out, you can run it on jupyter labs on your own computer.
#
#gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
#
## Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
## The following code is commented out, you can run it on jupyter labs on your own computer.
#
#gamefinder.get_json()
#
#
##WHAT DOES STATUS CODE 202 MEANS 
#
## example
## from google.appengine.api import urlfetch
## url = "http://www.google.com/"
## result = urlfetch.fetch(url)
## if result.status_code == 200:
##     doSomethingWithResult(result.content)
## It's a HTTP status code, it means "OK" (EG: The server successfully answered the http request)
#
#games = gamefinder.get_data_frames()[0]
#print(games)
#print(games.head())



#PRACTICE PROJECT: GDP DATA EXTRACTION AND PROCESSING

#Introduction
#In this practice project, you will put the skills acquired through the course to use. You will extract data from a website using webscraping and reqeust APIs process it using Pandas and Numpy libraries.

#Project Scenario:
#An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating a script that can extract the list of the top 10 largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF).

#The required data seems to be available on the URL mentioned below:

#URL: https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29


#After completing this lab you will be able to:

#Use Webscraping to extract required information from a website.
#Use Pandas to load and process the tabular data as a dataframe.
#Use Numpy to manipulate the information contatined in the dataframe.
#Load the updated dataframe to CSV file.


#URL : https://www.imdb.com/chart/top/

#Step 1: Choose the Website and Webpage URL

#Step 2: Inspect the website
#Note these elements' class names and ids as they will be used in the Python code.

#Step 3: Installing the important libraries

#requests - for making HTTP requests to the website
#BeautifulSoup - for parsing the HTML code
#pandas - for storing the scraped data in a data frame
#time - for adding a delay between requests to avoid overwhelming the website with requests

#pip install requests
#pip install BeautifulSoup
#pip install time
#pip install pandas
#pip install beautifulsoup4 #(error on this bs4) from bs4 import  BeautifulSoup

#Step 4: Write the Python code

#Now, it’s time to write the main python code. The code will perform the following steps:

#Using requests to send an HTTP GET request
#Using BeautifulSoup to parse the HTML code
#Extracting the required data from the HTML code
#Store the information in a pandas dataframe
#Add a delay between requests to avoid overwhelming the website with requests

#import requests

#from bs4 import BeautifulSoup
#import pandas as pd
#import time

## URL of the website to scrape
#url = "https://www.imdb.com/chart/top"

## Send an HTTP GET request to the website
#response = requests.get(url) # output <Response [403]> 
## <class 'requests.models.Response'>
## requests.get(url, params={key: value}, args)
## requests.get(url, timeout=2.50)
## The get() method sends a GET request to the specified url.

## Parse the HTML code using BeautifulSoup
#soup = BeautifulSoup(response.content, 'html.parser')

##output

##<html>
##<head><title>403 Forbidden</title></head>
##<body>
##<center><h1>403 Forbidden</h1></center>
##</body>
##</html>


## Extract the relevant information from the HTML code
#movies = []
#for row in soup.select('tbody.lister-list tr'):
#    title = row.find('td', class_='titleColumn').find('a').get_text()
#    year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
#    rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
#    movies.append([title, year, rating])

## Store the information in a pandas dataframe
#df = pd.DataFrame(movies, columns=['Title', 'Year', 'Rating'])

## Add a delay between requests to avoid overwhelming the website with requests
#time.sleep(1)

#print(df)

## THIS DOES NOT WORKED

##Empty DataFrame
##Columns: [Title, Year, Rating]
##Index: []





## THIS WORKS
# CONNECTING SNOWFLAKE TO PYTHON WITH SSO AUTH / AZURE AD (without password)

import pandas as pd
#import snowflake.connector

#credentials = {
#    'account'    : 'mt59224.east-us-2.privatelink'
#    , 'user'     : 'JSHARMA10@R1RCM.COM'
#    , 'authenticator' : 'externalbrowser'
#    ,'warehouse' : 'BISON_BI_WH_M',
#    'database' : 'RCM',
#    'schema' : 'RCM_DATAMART',
#    'authanticator' :'externalbrowser'
#    }
# 
#    with snowflake.connector.connect(**credentials) as cnx:
#    cur  = cnx.cursor()
#    cur.execute('''             
#        select distinct
#                *
#        from
#                (
#                        SELECT
#                                YEAR(DATEADD(MONTH, +6, txn_date)) AS FiscalYear,
#                                sum(txn_amt)                       as TXNAMOUNT ,
#                                facility_group_name                             ,
#                                b.facility_group_name                           ,
#                                txn_code_subcategory
#                        FROM
#                                RCM_DATAMART.fact_transaction a
#                        left join
#                                RCM_DATAMART.dim_facility b
#                        on
#                                a.facility_code = b.facility_code
#                        where
#                                txn_code_category in ('Denial - clinical',
#                                                    'denial - technical')
#                        and     b.facility_group_name = 'Baltimore'
#                        group by
#                                facility_group_name ,
#                                FiscalYear          ,
#                                txn_code_subcategory,
#                                b.facility_group_name)
#        where
#                fiscalyear = 2024''')
#    
#
#text = cur.fetchall() # list of tuple

text_for_example = [(1,2,3,4,5),(6,7,8,9,10)]

list_of_col = ['FiscalYear','TXNAMOUNT', 'facility_group_name', 'b.facility_group_name', 'txn_code_subcategory'] 

df = pd.DataFrame(columns = list_of_col )
    
for element  in text_for_example:
    individual_row_data = [data for data in element] 
    # list comprehension
    # [1, 2, 3, 4, 5]
    # [6, 7, 8, 9, 10]
    length = len(df) # assign row count of df
    df.loc[length]  = individual_row_data
    
print(df)
    
 # here account -> mt59224.east-us-2.privatelink if checked by link of SNOWFLAKE between https:// and .snowflakecomputing
 ######################################################################



#########################################################################################
#########################################################################################

# THIS WORKS

# BELOW EXAMPLE FOR WEB SCRAPPING

# TAKING WEBSITE 

# INSPECTING AND LOADING DATA ELEMENTS FROM TABLES TO DATAFRAME THEN EXCEL

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# after inspecting website and copying relevant table or element class name 
#<table class="wikitable sortable static-row-numbers plainrowheaders srn-white-background jquery-tablesorter" border="1" style="text-align:right;">

page = requests.get(url) 

# output <Response [403]> 
# <class 'requests.models.Response'>
# requests.get(url, params={key: value}, args)
# requests.get(url, timeout=2.50)
# The get() method sends a GET request to the specified url.
# Parse the HTML code using BeautifulSoup

soup = BeautifulSoup(page.text, 'html')

# output whole bunch of html code for the page

# all_table = soup.find_all('table')[0]

# ideally it should find out all table but there are some issues

specified_table_by_class = soup.find('table', class_ = 'wikitable sortable')

# here it should be class_

world_titles = specified_table_by_class.find_all('th')

#print(world_titles)

# output table header
#soup = BeautifulSoup(page.text, 'html')
#[<th>Rank
#</th>, <th>Name
#</th>, <th>Industry
#</th>, <th>Revenue <br/>(USD millions)
#</th>, <th>Revenue growth
#</th>, <th>Employees
#</th>, <th>Headquarters
#</th>, <th>Rank
#</th>, <th>Name
#</th>, <th>Industry
#</th>, <th>Revenue <br/>(USD billions)
#</th>, <th>Employees
#</th>, <th>Headquarters
#</th>, <th>Rank
#</th>, <th>Name
#</th>, <th>Industry
#</th>, <th>Profits<br/>(USD millio


# using list comprehension

#print(type(world_titles))
#print(world_titles[0])

# output for above 
# soup = BeautifulSoup(page.text, 'html')
# <class 'bs4.element.ResultSet'>
# <th>Rank
# </th> 

#print(world_titles[0].text)

# output 
# Rank

#world_table_titles = [title.text for title in world_titles]

#output 
#['Rank\n', 'Name\n', 'Industry\n', 'Revenue (USD millions)\n', 'Revenue growth\n', 'Employees\n', 'Headquarters\n', 'Rank\n', 'Name\n', 'Industry\n', 'Revenue (USD billions)\n', 'Emp

world_table_titles = [title.text.strip() for title in world_titles]

# alt solution  world_table_titles = [title.text[:-1:] for title in world_titles]

# world_titles = soup.find_all('th')
# here we need to change as soup.fin_all include all table
# instead use specified_table_by_class

# print(world_table_titles)

# output
# ['Rank', 'Name', 'Industry', 'Revenue (USD millions)', 'Revenue growth', 'Employees', 'Headquarters']

import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

# print(df.columns)

column_data  = specified_table_by_class.find_all('tr') # this will give all column data

for row in column_data[1::]:
    row_data = row.find_all('td') # this will result is all bunch of html coding including 'td'
    # what we want to do is similar to world_table_titles
    individual_row_data = [data.text.strip() for data in row_data]
    
# note here for row in column_data
# we are getting first element blank
#    []
#['1\n', 'Walmart\n', 'Retail\n', '611,289\n', '  6.7%\n', '2,100,000\n', 'Bentonville, Arkansas\n']
#['2\n', 'Amazon\n', 'Retail and cloud computing\n', '513,983\n', '  9.4%\n', '1,540,000\n', 'Seattle, Washington\n']
#['3\n', 'ExxonMobil\n', 'Petroleum industry\n', '413,680\n', '  44.8%\n', '62,000\n', 'Spring, Texas\n']

# so start with second element

# DataFrame

# Pandas DataFrame.loc attribute accesses a group of rows and columns by label(s) or a boolean array in the given Pandas DataFrame

# The loc property gets, or sets, the value(s) of the specified labels
# Specify both row and column with a label.

# To access more than one row, use double brackets and specify the labels, separated by commas:
 
# df.loc[["Sally", "John"]]
 
# Specify columns by including their labels in another list:
 
# df.loc[["Sally", "John"], ["age", "qualified"]]
 
# You can also specify a slice of the DataFrame with from and to labels, separated by a colon:
 
# df.loc["Sally": "John"]

    length = len(df) # assign row count of df
    df.loc[length]  = individual_row_data
    


print(df)

#output

#   soup = BeautifulSoup(page.text, 'html')
#    Rank                      Name                    Industry Revenue (USD millions) Revenue growth  Employees             Headquarters
# 0     1                   Walmart                      Retail                611,289           6.7%  2,100,000    Bentonville, Arkansas
# 1     2                    Amazon  Retail and cloud computing                513,983           9.4%  1,540,000      Seattle, Washington
# 2     3                ExxonMobil          Petroleum industry                413,680          44.8%     62,000            Spring, Texas
# 3     4                     Apple        Electronics industry                394,328           7.8%    164,000    Cupertino, California
# 4     5        UnitedHealth Group                  Healthcare                324,162          12.7%    400,000    Minnetonka, Minnesota
# ..  ...                       ...                         ...                    ...            ...        ...                      ...
# 95   96                  Best Buy                      Retail                 46,298          10.6%     71,100     Richfield, Minnesota
# 96   97      Bristol-Myers Squibb     Pharmaceutical industry                 46,159           0.5%     34,300  New York City, New York
# 97   98           United Airlines                     Airline                 44,955          82.5%     92,795        Chicago, Illinois
# 98   99  Thermo Fisher Scientific      Laboratory instruments                 44,915          14.5%    130,000   Waltham, Massachusetts
# 99  100                  Qualcomm                  Technology                 44,200          31.7%     51,000    San Diego, California


# Finally we can export our dataset to csv in local file using this 
# df.to_csv(r'C:\Users\IN10033204\Documents\Python Sheets\WEB SCRAPPING EXAMPLE.csv', index = False)


#=============================================================
#PYTHON PROJECT. During this process you will perform specific tasks such as extracting data, web scraping, visualizing data, and creating a dashboard.
#
#PROJECT OVERVIEW
#For this project, you will assume the role of a Data Scientist / Data Analyst working for a new startup investment firm that helps customers invest their money in stocks. Your job is to extract financial data like historical share price and quarterly revenue reportings from various sources using Python libraries and webscraping on popular stocks. After collecting this data you will visualize it in a dashboard to identify patterns or trends. The stocks we will work with are Tesla, Amazon, AMD, and GameStop
#
#==============================================================
#
#SHINY - OPEN SOURCE WEB FRAME WORK FOR PYTHON AND R
#
#VScode -> Terminal
#Pip install shiny
#pip install rsconnect #-python
#
## here we are struck
#STEP 2 – AUTHORIZE ACCOUNT
#rsconnect::setAccountInfo(name='rootshinyapp',token='6BC11432EF820F52366A0D3748CC398C',secret='<SECRET>')

# import graphics from turtle

# make cool diagrams

from turtle import Turtle, Screen

tinny_the_turtle = Turtle() # object of Turtle class

tinny_the_turtle.shape("turtle") # this is the shape of the cursor
tinny_the_turtle.color("red")

step = 175
iteration = 91

# for step 10 iteration = 10 and this will move turtle in circle  

# so basically left will just changes direction of turtle by angle

# step = 90 # square 

# flower
# step = 100
# iteration = 21  

# step =120 # trinangle

# more detailed flower
# step = 130
# iteration = 51 

# step = 170
# iteration = 51

# as we go from >90 to <180 circle of flower becomes smallers , at 170 it is smallest


# cool shape @ 179 japanese fan

# cool shape @ 
# step = 175
# iteration = 91


for i in range(iteration): 
    tinny_the_turtle.forward(step)
    tinny_the_turtle.left(step) # here step means angle
        


screen = Screen()
screen.exitonclick() # turtle graphics screen


##########################################
#penup() and pendown()

from turtle import Turtle, Screen

tin= Turtle() # object of Turtle class

for i in range(16):
    tin.forward(10)
    tin.penup()
    tin.forward(10)
    tin.pendown()

screen = Screen()
screen.exitonclick() # turtle graphics screen


# draw triangle square pentagon hexagon heptagon octagon nonagon and decagon
# 60 90 108 120 128.57

# NOTE
# A regular polygon of n sides has each exterior angle = 360/n
# So, the angle between two sides, or the interior angle = 180 -360/n = (180n-360)/n = 180(n-2)/n.

from turtle import Turtle , Screen
import random 

tin = Turtle() # object

tin.color()

side = 100

color_list = ['crimson','dark violet', 'spring green', 'medium slate blue']

for i in range (3,10): # for the different shapes 
	for j in range(i): # for drawing each shape
		tin.color(random.choices(color_list))
		tin.forward(side)
		tin.right(360/i)

screen = Screen()
screen.exitonclick()

# RANDOM WALK 

# random walk, in probability theory, a process for determining the probable location of a point subject to random motions, 
# given the probabilities (the same at each step) of moving some distance in some direction.

# path traced by  the moleculues of liquid and gases

# In psychology, random walks explain accurately the relation between the time needed to make a decision and the probability that a certain decision will be made

# Brownian motion is the random motion of particles suspended in a medium (a liquid or a gas). The motion is caused by fast-moving atoms or molecules that hit the particles.

from turtle import Turtle, Screen
import turtle as t
import random

tin = Turtle() # object of Turtle class

t.colormode(255)

def randon_color_gen():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_color = (r, b, g)
    return random_color

list_of_direction = [x for x in range(361) if x % 90 == 0]

tin.pensize(7)

tin.speed(1)

# setheading is just orientation

for i in range(1001):
    
    tin.color(randon_color_gen()) # calling random color generator
    tin.forward(30)
    tin.setheading(random.choice(list_of_direction))
    

screen = Screen()
screen.exitonclick() # turtle graphics screen


# MAKE a Spirograph

# my method by circle and left

from turtle import Turtle, Screen
import turtle as t
import random

tin = Turtle() # object of Turtle class

t.colormode(255)

def randon_color_gen():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_color = (r, b, g)
    return random_color


tin.speed("fastest")

r = 100
angle =5

for i in range(1,51):
    t.color(randon_color_gen())
    t.circle(r) 
    t.left(angle)
  
screen = Screen()
screen.exitonclick() # turtle graphics screen


# in second method we can use t.setheading()

#####################################################################################################################################################################
#####################################################################################################################################################################

# HACKERRANK PROBLEM SOLVING

# working with array

#1 finding difference in sum of two digonals

a=[[1,2,3],[2,4,6],[3,6,9]]

count = 0

for row in a: # row element will contain list 
    count += 1

for i in range(count):
    for j in range(count):
        print(a[i][j], end=" ")
    print('')

# principle diagonal
    
for i in range(count):
    for j in range(count):
        if(i == j):
            print(a[i][j], end=" ")
        else :
            print(" ",end=" ")
    print('')

# anti-diagonal

for i in range(count):
    for j in range(count):
        if(i == count-1-j):
            print(a[i][j], end=" ")
        else :
            print(" ",end=" ")
    print('')



def diagonal_difference(a):
    
    count_row = 0
    for row in a: # row element will contain list 
        count_row += 1


    # principle diagonal
    sum_principle=0

    for i in range(count):
        for j in range(count):
            if(i == j):
                sum_principle += a[i][j]
            else :
                pass

    # anti-principle diagonal
    sum_Anti_principle=0

    for i in range(count):
        for j in range(count):
            if(i == count-1-j):
                sum_Anti_principle += a[i][j]
            else :
                pass

    return abs(sum_principle-sum_Anti_principle)

print("Result")
print(diagonal_difference(a))


################################################

#2 find the ratio of the postive , negative and zero

a=[-4,3,-9,0,4,1]

count_positive = 0
count_negative = 0
count_zero = 0
count_total = 0

# Formatting expressions

# floating point with that many decimals

# this method will place certain number of decimal in division result despite of the result

# '{:.2f}'.format(0.5) → '0.50'

for i in a:
    count_total +=1
    if (i > 0 ):
        count_positive +=1
    elif (i<0):
        count_negative +=1
    else :
        count_zero +=1

print('{:.6F}'.format(count_positive/count_total))
print('{:.6F}'.format(count_negative/count_total))
print('{:.6f}'.format(count_zero/count_total))


# output 

# 0.500000
# 0.333333
# 0.166667