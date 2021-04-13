"""

    # For Loops
        It's Almost similar to the "While" Loop but the only difference is that
        here in for loops, we know when a particular condition will end, i.e.,
        we know the limit of that particular condition.

    # range Function
        Range function is basically used to print a range or a series of numbers.
        The range function is converted into a list first and then it is processed
        or passed for further execution.
        It takes 3 arguments which are :
        start,stop,step
        start -  is used to give the starting point to the range function
        stop -  is used to tell the range function where to stop excluding the number
                which is entered in the place of stop argument.
        step - is used to just increment or jump from one value to next the number that
                is entered in the place of step argument until the range function comes to
                an end.



"""
reps = range(1, 9, 2)
for rep in reps:
    print(f'Rep number: {rep}')
print("Amazing bud!")
