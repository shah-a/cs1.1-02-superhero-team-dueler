from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    """Arena class for heroes' battleground."""

    def __init__(self):
        """Constructor for arena."""
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        """Prompt for Ability information."""
        name = input("Ability name?: ")
        max_damage = input("Max damage?: ")
        return Ability(name, max_damage)

    def create_weapon(self):
        """Prompt for Weapon information."""
        name = input("Weapon name?: ")
        max_damage = input("Max damage?: ")
        return Weapon(name, max_damage)

    def create_armor(self):
        """Prompt for Armor information."""
        name = input("Armor name?: ")
        max_block = input("Max block?: ")
        return Weapon(name, max_block)

    def create_hero(self):
        """Prompt for Hero information."""

        hero_name = input("Hero name?: ")
        hero = Hero(hero_name)

        equip_menu = None
        while equip_menu != "4":
            equip_menu = input(
                "\n[1] Add ability\n"
                "[2] Add weapon\n"
                "[3] Add armor\n"
                "[4] Done adding equips\n\n"
                "Your choice: "
            )
            print()

            if equip_menu == "1":
                hero.add_ability(self.create_ability())
            elif equip_menu == "2":
                hero.add_weapon(self.create_weapon())
            elif equip_menu == "3":
                hero.add_armor(self.create_armor())

        return hero

    def build_team_one(self):
        """Prompt for team one."""
        team_name = input("Team one name?: ")
        num_heroes = int(input(f"How many heroes on team \"{team_name}\"?: "))
        self.team_one = Team(team_name)
        for _ in range(num_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        """Prompt for team two."""
        team_name = input("Team two name?: ")
        num_heroes = int(input(f"How many heroes on team \"{team_name}\"?: "))
        self.team_two = Team(team_name)
        for _ in range(num_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
