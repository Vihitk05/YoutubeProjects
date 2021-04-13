"""
    Type conversion is done just to change the type of data and it doesnt change the data.
"""
percentage = 85
final_percentage = float(percentage)  # Explicit Type Conversion
print(type(percentage))
print(type(final_percentage))

'''
    Input function is a built in function in Python for receiving an input from the user.
    By default the input function takes the input as a string. You can type convert it to 
    any other type by just adding the type data type you want to convert it to.👇
'''

user_input = int(input('Enter your age: '))
print(type(user_input))
