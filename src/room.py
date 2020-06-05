from __future__ import annotations

# Implement a class to hold room information. This should have name and
# description attributes.

__all__ = ('Room',)

from typing import Dict, Optional, Sequence

from item import Item


class Room:
    n_to: Optional[Room] = None
    e_to: Optional[Room] = None
    s_to: Optional[Room] = None
    w_to: Optional[Room] = None

    def __init__(self, name: str, surroundings: str, items: Sequence[Item]) -> None:
        self.name = name
        self.surroundings = surroundings
        self.items = items

    def __str__(self):
        return f'{self.name}'

    @property
    def directions(self) -> Dict[str, Room]:
        return {'n': self.n_to, 'e': self.e_to, 's': self.s_to, 'w': self.w_to}
