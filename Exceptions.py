"""

    # Exception Handling
    There are 2 types of Errors in Python:
    1. Syntax Error - Caused because of entering the wrong syntax
    2. Exception Error - Caused because of some invalid change occuring in the program
            Python Interpreter doesn't understand it and it gives an Error.

    But we can handle these exceptions by entering something when that particular
    exception occurs so that our program won't stop the execution and it will go
    naturally to the end of the program,i.e., It wont give us any Exception
    errors while Executing the program.

"""


def even_odd():
    while True:
        try:
            user_input = int(input('Enter a number: '))
        except ValueError:
            print('Its not a  Integer.')
        else:
            if user_input % 2 == 0:
                print('Number is Even.')
                break
            else:
                print('Number is Odd.')
                break
        finally:
            print('Code Executed Successfully!')


even_odd()
