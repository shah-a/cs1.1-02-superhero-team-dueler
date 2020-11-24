# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Nov. 17, 2020
# CS1.1 Assignment 2: Superhero Team Dueler

from ability import Ability
from weapon import Weapon
from armor import Armor

class Hero:
    """Class for hero objects."""

    def __init__(self, name, starting_health=100):
        """Constructor for hero instances. Starting health = 100."""
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def fight(self, opponent):
        """Duels heroes (self and opponent)."""

        if self.abilities or opponent.abilities:
            while (self.is_alive() and opponent.is_alive()):
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())

            winner = self if self.is_alive() else opponent
            loser = opponent if self.is_alive() else self
            winner.add_kill(1)
            loser.add_death(1)

            print(f"{winner.name} won against {loser.name}!")
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

    def add_kill(self, num_kills):
        """Update self.kills by num_kills amount"""
        self.kills += num_kills

    def add_death(self, num_deaths):
        """Update self.deaths by num_deaths amount"""
        self.deaths += num_deaths

    def attack(self):
        """Calculate total damage from all abilities."""
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        """Calculate total defense from all armors."""
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        """Adjusts hero's health after taking an attack."""
        if damage - self.defend() < 0:
            self.current_health -= 0
        else:
            self.current_health -= (damage - self.defend())

    def is_alive(self):
        """Return True or False depending on whether hero has health remaining."""
        return False if self.current_health <= 0 else True

if __name__ == "__main__":
    goku = Hero("Goku")
    frieza = Hero("Frieza")
    kamehameha = Ability("Kamehameha", 10)
    death_beam = Ability("Death Beam", 10)
    power_pole = Weapon("Power Pole", 10)
    goku.add_ability(kamehameha)
    frieza.add_ability(death_beam)
    goku.add_weapon(power_pole)
    goku.fight(frieza)
