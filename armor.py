from random import randint

class Armor:
    """Class for hero armor."""

    def __init__(self, name, max_block):
        """Constructor for hero armor."""
        self.name = name
        self.max_block = max_block

    def block(self):
        """Return value for block between 0 and max_block."""
        return randint(0, self.max_block)

if __name__ == "__main__":
    armor = Armor("Debug Shield", 10)
    print(armor.name)
    print(armor.block())
