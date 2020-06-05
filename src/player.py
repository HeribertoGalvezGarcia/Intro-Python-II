# Write a class to hold player information, e.g. what room they are in
# currently.

__all__ = ('Player',)

from room import Room


class Player:
    def __init__(self, name: str, room: Room) -> None:
        self.name = name
        self.current_room = room

    def move(self, direction: str) -> None:
        if direction not in ('n', 'e', 's', 'w'):
            raise ValueError('Invalid direction given.')

        if (room := self.current_room.directions[direction]) is None:
            raise ValueError('There is no room in that direction')

        self.current_room = room
