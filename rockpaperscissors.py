import random
choices = ('r', 'p', 's')
player_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
if player_choice not in choices:
    print('Invalid choice')
cpu_choice = random.choice(choices)
print(f'Player chose {player_choice}')
print(f'CPU chose {cpu_choice}')