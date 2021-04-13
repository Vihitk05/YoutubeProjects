"""
    # More about Strings
        Indexing in Strings
    Every character and a whitespace(i.e. a space in between two words) has an index
    starting from 0.
    In the example below 'Python is  a   w  e  s  o  m  e' this string is indexed as
                          0123456789 10 11 12 13 14 15 16
    You can access the string by indexing it.
    Python also supports "NEGATIVE INDEXING" starting from the end of the string.
"""

appreciation = 'Python is awesome'
# print(appreciation[0:10])  # Positive Indexing

# print(appreciation[1:-1])  # Negative Indexing

# print(appreciation[:])  # The Entire String

'''
    # String Concatenation & Formatted String
    String concatenation is sometimes difficult to visualise. For that reason we
    use Formatted Strings. To implement formatted strings we use '{}' (curly braces) 
    to dynamically insert values in your string.

'''
# first_name = input('First Name: ')
# last_name = input('Last Name: ')
# message = 'My name is ' + first_name +' ' + last_name  # String Concatenation
# print(message)
# intro = f'My name is {first_name} {last_name}'  # Formatted String
# print(intro)
'''  
    You can also use string concatenation and formatted strings without declaring a 
    separate variable for it by using the print statement
'''
# print(f'My name is {first_name} {last_name}') # formatted string
# print('My name is ' + first_name + ' ' + last_name) # string concatenation

'''
 There is another type of method by which you can insert values in a string that method 
 is called as a "Dot Format method". But this method also makes its readability a 
 bit hard. So its better to use the Formatted strings in your code. 
'''
# print('My name is {} {}'.format(first_name, last_name))  # Dot Format Method

'''
 # String Methods
 String Methods are there to do some editing work in the string. For example,
 Lets take the above 'appreciation' variable to explore some string methods.
'''
# appreciation = 'Python is awesome'
# print(appreciation.upper())  # Changes the Whole String to Upper Case

# print(appreciation.lower())  # Changes the Whole String to Lower Case

# print(appreciation.find('is'))  # Gives the index from where the character or word starts

# print('python' in appreciation)  # Returns a BOOLEAN value if the paricular word or character exists in the string.

# print(appreciation.replace('Python', 'Java'))  # Replaces a word or character from the string to another

# print(appreciation.capitalize())  # Capitalizes only the first letter of the String

# print(appreciation.title())  # Capitalizes the first letter of every word in the String
