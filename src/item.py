class Item:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return self.name


class LightSource(Item):
    pass
