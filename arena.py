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
        max_damage = int(input("Max damage?: "))
        return Ability(name, max_damage)

    def create_weapon(self):
        """Prompt for Weapon information."""
        name = input("Weapon name?: ")
        max_damage = int(input("Max damage?: "))
        return Weapon(name, max_damage)

    def create_armor(self):
        """Prompt for Armor information."""
        name = input("Armor name?: ")
        max_block = int(input("Max block?: "))
        return Armor(name, max_block)

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

    def team_battle(self):
        """Duels hero teams (team_one and team_two)."""
        self.team_one.attack(self.team_two)

        # Error trap method 1:
        # assert isinstance(self.team_one, Team)
        # assert isinstance(self.team_two, Team)
        # self.team_one.attack(self.team_two)

        # Error trap method 2:
        # try:
        #     self.team_one.attack(self.team_two)
        # except:
        #     print("Build both teams first!")


    def show_stats(self):
        """Show team statistics."""
        print(f"\nTeam \"{self.team_one.name}\" statistics:")
        self.team_one.stats()

        print(f"\nTeam \"{self.team_two.name}\" statistics:")
        self.team_two.stats()

        print()
        team_kdr(self.team_one)
        team_kdr(self.team_two)

        print()
        print("Survivors:")
        survivors(self.team_one)
        survivors(self.team_two)
        print()

def team_kdr(team):
    """Helper function for show_stats method."""
    team_kills = 0
    team_deaths = 0
    for hero in team.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(f"Team \"{team.name}\" average K/D: ", end="")
    print("{:.2f}".format(team_kills/team_deaths))

def survivors(team):
    """Helper function for show_stats method."""
    for hero in team.heroes:
        if hero.current_health > 0:
            print(f"  - {hero.name} from team \"{team.name}\"")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play again? ([Y] or [N]): ")

        # Check player's input
        if play_again.lower() == "n":
            game_is_running = False
        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
