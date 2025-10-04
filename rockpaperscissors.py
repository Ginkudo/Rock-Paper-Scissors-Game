import random
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

def get_player_choice():
    while True:
        player_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if player_choice in choices:
            return player_choice
        else:
            print('Invalid choice')

while True:
    player_choice = get_player_choice()

    cpu_choice = random.choice(choices)

    print(f'Player chose {emojis[player_choice]}')
    print(f'CPU chose {emojis[cpu_choice]}')

    if player_choice == cpu_choice:
        print('Tie!')
    elif (
        (player_choice == 's' and cpu_choice == 'p') or 
        (player_choice == 'p' and cpu_choice == 'r') or 
        (player_choice == 'r' and cpu_choice == 's')):
        print('You win!')
    else:
        print('You lose!')

    another_round = input('Continue? (y/n): ').lower()
    if another_round == 'n':
        break