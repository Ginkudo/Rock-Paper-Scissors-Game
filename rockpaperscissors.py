import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
choices = (ROCK, PAPER, SCISSORS)

def get_player_choice():
    while True:
        player_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if player_choice in choices:
            return player_choice
        else:
            print('Invalid choice')

def display_choices(player_choice, cpu_choice):
    print(f'Player chose {emojis[player_choice]}')
    print(f'CPU chose {emojis[cpu_choice]}')

def win_condition(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        print('Tie!')
    elif (
        (player_choice == SCISSORS and cpu_choice == PAPER) or 
        (player_choice == PAPER and cpu_choice == ROCK) or 
        (player_choice == ROCK and cpu_choice == SCISSORS)):
        print('You win!')
    else:
        print('You lose!')

def play_game():
    while True:
        player_choice = get_player_choice()

        cpu_choice = random.choice(choices)

        display_choices(player_choice, cpu_choice)

        win_condition(player_choice, cpu_choice)

        another_round = input('Continue? (y/n): ').lower()
        if another_round == 'n':
            break

play_game()