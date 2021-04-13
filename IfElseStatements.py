"""

    # If Else statements
    These are decision making statements. In this,if we have multiple
    conditions then what this if else statements does that it goes through all the
    conditions one by one and if any one of the condition is "True" then only it will
    execute the code which is in that if or elif (else-if) block. Otherwise, it won't
    execute any of the block if none of the conditions gives True as the result in the
    'if' or 'elif' conditions.It will execute whatever code exists in the else
    statement block.


"""

user_input = int(input('Enter the amount of water you drink everyday(in litres): '))

"""
    if the user drinks less than 1 litre everyday then
        we'll tell him to drink more water
    else if the user drinks water upto 3 litres everyday then
        we'll just give him or her a compliment like Very Good!
    else 
        we'll appreciate him or her like Amazing! Keep it up!
    
"""
if user_input <= 1:
    print('You drink very less water. Please drink more water!')
elif user_input <= 3:
    print('Very Good!')
else:
    print('Amazing! Keep it up!')
