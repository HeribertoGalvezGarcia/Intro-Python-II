import sys
import textwrap

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('John Doe', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def main() -> None:
    while True:
        desc = '\n'.join(textwrap.wrap(player.current_room.surroundings))
        items = '\n'.join(player.current_room.items)
        print(f'Location: {player.current_room}\n\n{desc}\nItems: {items or None}')

        while True:
            if (user_input := input('What will you do? ').lower()) not in ('n', 'e', 's', 'w', 'q'):
                print('Invalid option given.')
                continue

            if user_input == 'q':
                print('Exiting')
                sys.exit(0)

            try:
                player.move(user_input)
            except ValueError as e:
                print(e)
                continue

            print(f'\nMoved to {player.current_room}\n')
            break


if __name__ == '__main__':
    main()
