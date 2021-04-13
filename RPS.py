import random

human_choice = 0
human_score = 0
computer_choice = 0
computer_score = 0
rps_dict = {
    0: 'Rock',
    1: 'Paper',
    2: 'Scissors'
}


def inputs_of_human_and_computer():
    while True:
        global human_choice
        global computer_choice
        global rps_dict
        try:
            human_choice = int(input('Enter your choice [0:Rock,1:Paper,2:Scissors]: '))
            if human_choice == 0 or human_choice == 1 or human_choice == 2:
                computer_choice = random.randint(0, 2)
                print(f'Your Choice: {rps_dict[human_choice]}')
                print(f'Computer Choice: {rps_dict[computer_choice]}')
                return human_choice, computer_choice
            else:
                print('Enter numbers between 0,1,2!')
                print('[0:Rock,1:Paper,2:Scissors]')
        except ValueError:
            print('Enter a Valid Choice!')
            print('[0:Rock,1:Paper,2:Scissors]')


def rps():
    while True:
        global human_choice
        global human_score
        global computer_choice
        global computer_score

        inputs_of_human_and_computer()

        if (human_choice - computer_choice) % 3 == 1:
            print('You win this Turn!')
            human_score = human_score + 1
            print(f'Human Score: {human_score}')
            print(f'Computer Score: {computer_score}')
            if human_score == 3:
                print('Congratulations! You won this Round!')
                replay()
                break
        elif human_choice == computer_choice:
            print('Its a Tie.')
            print(f'Human Score: {human_score}')
            print(f'Computer Score: {computer_score}')
        else:
            print('Computer wins this Turn!')
            computer_score = computer_score + 1
            print(f'Human Score: {human_score}')
            print(f'Computer Score: {computer_score}')
            if computer_score == 3:
                print('Sorry! Computer won this Round!')
                replay()
                break


def replay():
    global human_score
    global computer_score
    user_input = input('Do you want to play again [y/n]? ').lower()
    if user_input == 'y':
        print('Welcome Back!')
        human_score = 0
        computer_score = 0
        rps()
        return human_score, computer_score
    else:
        print('Thank you!')


rps()

"""

 0:rock   1:paper    2:scissors
  0                     2
  0-2= -2%3 =

"""
