"""
    Arithmetic Operators
    + Addition
    - Subtraction
    * Multiplication
    / Division which returns the original value with the decimal in it
    // Division which returns only the integer value i.e. the numbers before the decimal value
    ** Exponential
    % Modulus which returns the remainder of the division

    # Operators Precedence or BODMAS
    ()
    **
    * or /
    + or -

"""
print(10 / 3)  # returns the original value with the decimal in it
print(10 // 3)  # returns only the integer value i.e. the numbers before the decimal value
print(10 ** 3)  # returns the exponential value of 10 which means (10^3) which means 10*10*10
print(10 % 3)  # returns the remainder of the division

# IMPLICIT TYPE CONVERSION
x = 10
y = 11.1
print(type(x))
print(type(y))
z = x + y  # implicit type conversion
print(z)
print(type(z))
