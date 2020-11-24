# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Nov. 17, 2020
# CS1.1 Assignment 2: Superhero Team Dueler

from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Hero:
    """Class for hero objects."""

    def __init__(self, name, starting_health=100):
        """Constructor for hero instances. Starting health = 100."""
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def fight(self, opponent):
        """Duels heroes (self and opponent)."""
        if self.abilities or opponent.abilities:
            while (self.is_alive() and opponent.is_alive()):
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            winner = self.name if self.is_alive() else opponent.name
            print(f"{winner} won!")
        else:
            print("Draw!")

    def add_ability(self, ability):
        """Append ability to self.abilities."""
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        """"Append weapon to self.abilities."""
        self.abilities.append(weapon)

    def add_armor(self, armor):
        """Append armor to self.armors."""
        self.armors.append(armor)

    def attack(self):
        """Calculate total damage from all abilities."""
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage_amt):
        """Calculate total defense from all armors."""
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        if damage_amt - total_defense < 0:
            return 0
        else:
            return damage_amt - total_defense

    def take_damage(self, damage):
        """Adjusts hero's health after taking an attack."""
        self.current_health -= self.defend(damage)

    def is_alive(self):
        """Return True or False depending on whether hero has health remaining."""
        return False if self.current_health <= 0 else True

if __name__ == "__main__":
    goku = Hero("Goku")
    frieza = Hero("Frieza")
    # kamehameha = Ability("Kamehameha", 10)
    # death_beam = Ability("Death Beam", 10)
    bansho_fan = Weapon("Bansho Fan", 20)
    # goku.add_ability(kamehameha)
    # frieza.add_ability(death_beam)
    goku.add_weapon(bansho_fan)
    print(goku.attack())
