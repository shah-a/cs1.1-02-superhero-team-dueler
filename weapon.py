from random import randint
from ability import Ability

class Weapon(Ability):
    """Class for hero weapons."""

    def attack(self):
        """Return value for attack between max_damage//2 and max_damage."""
        return randint(self.max_damage // 2, self.max_damage)

if __name__ == "__main__":
    weapon = Weapon("Debug Weapon", 20)
    print(weapon.name)
    print(weapon.attack())
