from random import choice

class Team:
    """Class for hero teams."""

    def __init__(self, name):
        """Constructor for hero team."""
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        """Add hero to team."""
        self.heroes.append(hero)

    def remove_hero(self, name):
        """Remove hero from team."""
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
        if not found_hero:
            return 0

    def view_all_heroes(self):
        """View heroes on team."""
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        """Print team kill/death ratio."""
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} kill/deaths: ", end="")
            print("{:.2f}".format(kd))

    def revive_heroes(self, health=100):
        """Restore heroes to 100 health."""
        for hero in self.heroes:
            hero.current_health = health

    def attack(self, opponent_team):
        """Duels hero teams (self and opponent_team)."""
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in opponent_team.heroes:
            living_opponents.append(hero)

        while living_heroes and living_opponents:
            hero = choice(living_heroes)
            opponent = choice(living_opponents)
            hero.fight(opponent)

            if not hero.is_alive():
                living_heroes.remove(hero)
            elif not opponent.is_alive():
                living_opponents.remove(opponent)
