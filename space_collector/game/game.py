import random
from time import perf_counter


from space_collector.game.player import Player
from space_collector.game.planet import Planet
from space_collector.game.player_orientations import player_orientations
from space_collector.game.math import Vector


class Game:
    def __init__(self) -> None:
        self.start_time = perf_counter()
        self.last_update_time = self.start_time
        self.players: list[Player] = []

        nb_planets = random.randint(2, 10)
        all_planets_positions = set()
        self.planets_positions = []
        while len(self.planets_positions) < nb_planets:
            planets_positions = set()
            planet = Planet(
                x=random.randrange(-7000, 7001, 1000),
                y=random.randrange(3000, 17001, 1000),
                size=random.randint(20, 40),
                id=random.randint(1, 65535),
            )
            planet_vector = Vector([planet.x, planet.y])
            for orientation in player_orientations:
                player_planet_position = orientation.rotate_around_base(planet_vector)
                planets_positions.add(tuple(player_planet_position))
            if len(planets_positions) < len(player_orientations):
                continue
            if planets_positions & all_planets_positions:
                # conflict with existing planets
                continue
            all_planets_positions.update(planets_positions)
            self.planets_positions.append(planet)

    def manage_command(self, command: str) -> str:
        return "OK"

    def add_player(self, player_name: str) -> None:
        if len(self.players) >= 4:
            return
        player = Player(player_name)
        player.reset_spaceships_and_planets(len(self.players), self.planets_positions)
        self.players.append(player)

    def update(self) -> None:
        pass

    def state(self) -> dict:
        return {
            "time": perf_counter() - self.start_time,
            "players": [player.state() for player in self.players],
        }
