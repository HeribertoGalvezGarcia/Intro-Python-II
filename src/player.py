# Write a class to hold player information, e.g. what room they are in
# currently.

__all__ = ('Player',)

from typing import Optional

from room import Room


class Player:
    current_room: Optional[Room] = None
