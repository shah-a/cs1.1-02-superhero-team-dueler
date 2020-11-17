# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Nov. 17, 2020
# CS1.1 Assignment 2: Superhero Team Dueler

from random import choice

class Hero:
    """Class for hero objects."""

    def __init__(self, name, starting_health=100):
        """Constructor for hero instances. Starting health = 100."""
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        """Duels heroes (self and opponent)."""
        winner = choice([self.name, opponent.name])
        print(f"{winner} won!")

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero1.fight(hero2)
