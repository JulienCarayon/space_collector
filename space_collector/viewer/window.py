import logging
from queue import Queue

import arcade

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1777
SCREEN_TITLE = "Space collector"


class Window(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.input_queue: Queue = Queue()

    def setup(self):
        self.background_list = arcade.SpriteList()
        # grass = arcade.Sprite("space_collector/viewer/images/grass.jpeg")
        # grass_width = grass.width
        # grass_height = grass.height
        # for x in range(0, SCREEN_WIDTH, grass_width):
        #     for y in range(0, SCREEN_HEIGHT, grass_height):
        #         grass = arcade.Sprite("chronobio/viewer/images/grass.jpeg")
        #         grass.position = x + grass_width // 2, y + grass_height // 2
        #         self.background_list.append(grass)

    def on_draw(self):
        if not self.input_queue.empty():
            data = self.input_queue.get()
            # for index, farm in enumerate(self.farms):
            #     farm.update(data["farms"][index])
            #     farm.update_climate(data["events"])
            # self.score.update(data)

        self.clear()
        self.background_list.draw()
        # for farm_background in self.farm_backgrounds:
        #     farm_background.draw()
        # for farm in self.farms:
        #     farm.draw()
        # self.score.draw()


def gui_thread(window):
    try:
        window.setup()
        arcade.run()
    except Exception:  # noqa: PIE786
        logging.exception("uncaught exception")
