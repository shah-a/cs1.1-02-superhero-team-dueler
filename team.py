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
