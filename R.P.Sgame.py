import random


def get_choices():
    options = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input(
            'Enter a choice (rock, paper, scissors): '
        ).lower()

        if player_choice in options:
            computer_choice = random.choice(options)
            return {
                'player': player_choice,
                'computer': computer_choice
            }

        print('Invalid choice. Please try again.')


def check_win(player, computer):
    print(f'You chose {player}, computer chose {computer}.')

    if player == computer:
        return "It's a tie!"

    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! You win!'
        else:
            return 'Paper covers rock! You lose.'

    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! You win!'
        else:
            return 'Scissors cuts paper! You lose.'

    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts paper! You win!'
        else:
            return 'Rock smashes scissors! You lose.'


def play_game():
    player_score = 0
    computer_score = 0

    print('\n=== ROCK PAPER SCISSORS ===')

    while True:
        choices = get_choices()
        result = check_win(
            choices['player'],
            choices['computer']
        )

        print(result)

        if 'You win' in result:
            player_score += 1
        elif 'You lose' in result:
            computer_score += 1

        print(f'Score: You {player_score} - {computer_score} Computer')

        play_again = input(
            '\nPlay again? (yes/no): '
        ).lower()

        if play_again != 'yes':
            print('\nThanks for playing!')
            print(
                f'Final score: You {player_score} - '
                f'{computer_score} Computer'
            )
            break


play_game()