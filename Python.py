
print("1->###############################Welocome to reality###############################");

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

# Sring in python are imutable
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

#STRING INTERPOLATION (F-STRINGS)

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

#My name is Johnathan and I am 30 years old.

str.format()

name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))



# % Operator

name = "Johnathan"
age = 30
print("My name is %s and I am %d years old." % (name, age))


# ADDITIONAL CAPABILITIES

F-strings are also able to evaluate expressions inside the curly braces

x = 10
y = 20
print(f"The sum of x and y is {x+y}.")

#Raw String (r’’)
#In Python, raw strings are a powerful tool for handling textual data, especially when dealing with escape characters. By prefixing a string literal with the letter ‘r’, Python treats the string as raw, meaning it interprets backslashes as literal characters rather than escape sequences

#Regular string:

regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)

#output
#Regular String:  C:
#ew_folderile.txt

raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)

#output
#Raw String: C:\new_folder\file.txt

#STRING MANIPULATION OPERATIONS

#Slice
#Stride -name[::2] --steps
#
name = "Michael Jackson"
name.find('el')
#output 5
#searching index of sub string in the string

#g.replace("Mary","Bob")


#RegEx

#In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings.
#This RegEx module provides several functions for working with regular expressions, including search, split, findall, and sub.
#Python provides a built-in module called re, which allows you to work with regular expressions. First, import the re module

import re
s1 = "Michael Jackson is the best"

## Define the pattern to search for
pattern = r"Jackson"

## Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)
#
## Check if a match was found
if result:
    print("Match found!")
#else:
    print("Match not found.")



#Special Sequence																Meaning	Example
#\d		Matches any digit character (0-9)										"123" matches "\d\d\d"
#\D		Matches any non-digit character											"hello" matches "\D\D\D\D\D"
#\w		Matches any word character (a-z, A-Z, 0-9, and _)						"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
#\W		Matches any non-word character											"@#$%" matches "\W\W\W\W"
#\s		Matches any whitespace character (space, tab, newline, etc.)			"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
#\S		Matches any non-whitespace character									"hello_world" matches "\S\S\S\S\S\S\S\S\S"
#\b		Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
#\B		Matches any position that is not a word boundary						"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"

import re
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
	
#--findall
#	
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

# Print out the list of matched words
print(result)



---------------
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 

#Michael Jackson was a singer and known as the 'legend'


#---------------------
#split the substring to list:
#



