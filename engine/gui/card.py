import pygame

from .widget import Widget

# Do some kind of parent font thing
from ..constants import FONT


class Card(Widget):
    def __init__(self, parent_surf, rsurf, rpos, text, colour=[200, 20, 25]):
        super().__init__()
        self.rsurf = rsurf
        self.rpos = rpos
        if not type(text) == list:
            text = [str(text)]
        self.text = text
        self.adjust(parent_surf)
        self.colour = colour
        self.i_colour = self.colour[:]

    def adjust(self, parent_surf, parent=None):
        self.adjust_p(parent_surf, parent)
        self.adjust_r()
        font_size = int(self.rect.width / len(self.text)) + 5
        if font_size > self.rect.height:
            font_size = self.rect.height
        self.font = pygame.font.SysFont(FONT, font_size)

    def change_text(self, new_text):
        if not type(new_text) == list:
            new_text = [str(new_text)]
        old_text = self.text
        self.text = new_text
        self.create_lines()
        w = max(map(lambda line: line.get_width(), self.lines)) * 1.05
        wold = self.surf.get_width()
        if not len(self.text) == len(old_text) or (abs(wold - w) > 0.02 * wold):
            self.adjust_r()

    def create_lines(self):
        self.lines = []
        for t in self.text:
            line = self.font.render(t, 1, (250, 250, 250))
            self.lines.append(line)

    def draw(self):
        self.surf.fill(self.i_colour)
        x = 0
        for line in self.lines:
            self.surf.blit(line, (0, self.font_size * x))
            x += 1

    def change_colours(self):
        c = self.i_colour[:]
        self.i_colour = self.b_colour[:]
        self.b_colour = c
        self.draw()
        self.blit()

    def on_click(self, event):
        return False
