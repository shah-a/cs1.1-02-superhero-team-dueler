from random import randint

class Ability:
    """Class for hero abilities."""

    def __init__(self, name, max_damage):
        """Constructor for hero abiliity."""
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """Return value for attack between 0 and max_damage."""
        return randint(0, self.max_damage)

if __name__ == "__main__":
    ability = Ability("Debug Ability", 20)
    print(ability.name)
    print(ability.attack())
