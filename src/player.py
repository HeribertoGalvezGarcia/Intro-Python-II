# Write a class to hold player information, e.g. what room they are in
# currently.

__all__ = ('Player',)

from room import Room
from item import Item


class Player:
    def __init__(self, name: str, room: Room) -> None:
        self.name = name
        self.current_room = room
        self.inventory = []

    def move(self, direction: str) -> None:
        if direction not in ('n', 'e', 's', 'w'):
            raise ValueError('Invalid direction given.')

        if (room := self.current_room.directions[direction]) is None:
            raise ValueError('There is no room in that direction')

        self.current_room = room

    def pickup(self, item: Item) -> None:
        if item not in self.current_room.items:
            raise ValueError('Item is not in current room.')

        self.inventory.append(item)
        self.current_room.items.remove(item)

    def drop(self, item: Item) -> None:
        if item not in self.inventory:
            raise ValueError('Item is not in inventory.')

        self.inventory.remove(item)
        self.current_room.items.append(item)
