"""
    # While Loops
        Generally, we use while loops when we don't know when a particular
        condition will end i.e., we don't know the limit of the condition.

"""
reps = 0
not_tired = True
while not_tired:
    user_input = input('Are a you tired (y/n)? ').lower()
    if user_input == 'n':
        print(reps)
        reps += 1  # reps = reps+ 1
    else:
        print('Awesome! You did it!')
        break
