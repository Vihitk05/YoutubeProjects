"""

    # Functions
    In programming, we have a principle named "DRY" which basically means
    "DON'T REPEAT YOURSELF". We have to write a particular part of code more than
    once.This violates the DRY principle.So, to avoid that Functions were introduced.
    Functions are used to avoid that practice of writing that particular code more
    than once. We just have to call the function instead of writing that entire part
    of code.

"""


#              PARAMETER
def even_odd(user_input):
    if user_input % 2 == 0:
        print('Number is Even.')
    else:
        print('Number is Odd.')


number = int(input('Enter a number: '))
#        ARGUMENT
even_odd(number)
