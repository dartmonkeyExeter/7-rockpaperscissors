# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
options = ['rock', 'fire', 'scissors', 'sponge', 'paper', 'air', 'water']  # ordered list, each item beats the two ahead
win_words = [['puts out', 'crushes', 'crushes'], ['melts', 'burns', 'burns'], ['cuts', 'cuts', 'slice through'],
             ['soaks', 'absorbs', 'absorbs'], ['fans', 'floats on', 'covers'],
             ['evaporates', 'erodes', 'blows out'],
             ['erodes', 'puts out', 'rusts']]  # list of lists containing beating words


def game(options, win_words):  # define function for gameloop
    player_choice = ''  # sets player_choice so it can be looped later
    computer_choice = random.randint(0, len(options) - 1)  # random number 0- length of options
    options_as_string = ', '.join(options)  # joins the list together

    while player_choice not in options:  # stops user from inputting something not in the list
        player_choice = input(f'choose from: {options_as_string}\n').lower().strip()  # prints list and gets input

    player_choice_index = options.index(player_choice)  # checks where the players choice is in the list
    print(
        f'you chose {player_choice} and computer chose {options[computer_choice]}!')  # tells what player and computer chose

    if player_choice_index == computer_choice:  # checks if indexes are same
        print('its a draw!')
    else:
        for i in range(3):
            j = i + 1
            if computer_choice == (player_choice_index + j) % len(options):  # if the com choice is the remainder of 1 divided by the length of options
                print(f'{player_choice} {win_words[player_choice_index][i]} {options[computer_choice]}, so you won!')
                break
            if player_choice_index == (computer_choice + j) % len(options):  # if the player choice is the remainder of 1 divided by the length of options
                print(f'{options[computer_choice]} {win_words[computer_choice][i]} {player_choice}, so you lost...')
                break


def main():  # main function
    while True:
        game(options, win_words)


if __name__ == '__main__':  # if file name is main run main
    main()
