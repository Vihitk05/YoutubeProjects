"""
    Exercise: To find a number is Even Or Odd
    Step 1: Take an "Integer" Input from the user and type convert the input function.
    Step 2: Add an If statement which says value of input % 2 == 0
    Step 3: If Step 2 is True then print {Value of Input} is Even in Formatted Strings.
    Step 4: If Step 2 if False then add an else statement in that print {Value Of input}
            is Odd in Formatted Strings.

"""
user_input = int(input('Enter a number: '))
if user_input % 2 == 0:
    print(f'{user_input} is an Even Number.')
else:
    print(f'{user_input} is an Odd Number.')