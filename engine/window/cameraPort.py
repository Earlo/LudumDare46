from pygame import Rect
import itertools

from .viewPort import ViewPort
from ..graphicalAssetHandler import GraphicalAssetHandler


class CameraPort(ViewPort):
    graphicalAssetHandler = GraphicalAssetHandler()

    def __init__(self, x, y):
        super().__init__(x, y)
        self.erase = []
        self.previous = Rect(0, 0, x, y)
        self.camera = Rect(-100, -50, x, y)
        self.movement_direction = 0

    def get_updates(self):
        return self.erase + self.updates

    def clear_updates(self):
        self.debug_move()

        self.erase = []
        for r in self.updates:
            self.clear_at(r)
        self.updates = []

    @property
    def x(self):
        return self.camera.x

    @property
    def y(self):
        return self.camera.y

    def move_camera(self, x, y):
        self.previous = self.camera.copy()
        self.camera.move_ip(x, y)
        self.updates.append(self.get_rect())

    @property
    def background(self):
        return self._bgr

    @background.setter
    def background(self, new_bgr):
        print("setting bgr to {}".format(new_bgr))
        self._bgr = new_bgr
        self._tile = self.graphicalAssetHandler["bgr"][new_bgr]

        self.updates.append(self.get_rect())

    def clear_at(self, r):
        cx = r.x + self.x
        cy = r.y + self.y

        tw = self._tile.get_width()
        th = self._tile.get_height()
        tile_rect = self._tile.get_rect()

        clip_r = r.copy()
        rangX = [cx] + [(1 + n) * tw for n in range(cx // tw, (cx + r.w) // tw)]
        rangY = [cy] + [(1 + n) * th for n in range(cy // th, (cy + r.h) // th)]
        for x, y in itertools.product(rangX, rangY):
            clip_r.topleft = (x % tw, y % th)
            area = clip_r.clip(tile_rect)
            self.draw(self._tile, (x, y), area)
        self.erase.append(r)

    def draw(self, surf, pos, area):
        pos = (pos[0] - self.x, pos[1] - self.y)
        return super().draw(surf, pos, area)

    def display(self, surf, pos, area):
        self.updates.append(self.draw(surf, pos, area))

    def debug_move(self):
        from math import sin, cos

        self.movement_direction += 0.05
        self.move_camera(
            5 * cos(self.movement_direction), 5 * sin(self.movement_direction)
        )
        # self.move_camera(5, 5)
