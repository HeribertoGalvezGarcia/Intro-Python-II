# Write a class to hold player information, e.g. what room they are in
# currently.

__all__ = ('Player',)

from room import Room


class Player:
    def __init__(self, name: str, room: Room) -> None:
        self.name = name
        self.current_room = room
