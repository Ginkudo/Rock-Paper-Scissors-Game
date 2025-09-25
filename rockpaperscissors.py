import random
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

player_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
if player_choice not in choices:
    print('Invalid choice')

cpu_choice = random.choice(choices)

print(f'Player chose {emojis[player_choice]}')
print(f'CPU chose {emojis[cpu_choice]}')

if player_choice == cpu_choice:
    print('Tie!')
elif (player_choice == 's' and cpu_choice == 'p') or (player_choice == 'p' and cpu_choice == 'r') or (player_choice == 'r' and cpu_choice == 's'):
    print('You win!')
else:
    print('You lose!')