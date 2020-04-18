import pygame

from .widget import Widget

# Do some kind of parent font thing
from ..constants import FONT


class Button(Widget):  # Menu Button
    def __init__(self, parent_surf, rsurf, rpos, text, func, colour=[200, 20, 25]):
        super().__init__()
        self.rsurf = rsurf
        self.rpos = rpos
        self.text = text
        self.adjust(parent_surf)
        self.down = False
        self.func = func
        self.colour = colour
        self.i_colour = self.colour[:]
        self.cb_colour = [colour[0] / 2, colour[1] / 2, colour[2] / 2]
        self.b_colour = [colour[0] / 4, colour[1] / 4, colour[2] / 4]

    def adjust(self, parent_surf, parent=None):
        self.adjust_p(parent_surf, parent)
        self.adjust_r()

        font_size = int(self.rect.width / len(self.text)) + 5
        if font_size > self.rect.height:
            font_size = self.rect.height
        self.font = pygame.font.SysFont(FONT, font_size)
        self.label = self.font.render(self.text, 1, (1, 1, 1))

    def draw(self):
        self.surf.fill(self.i_colour)
        # old
        pygame.draw.rect(self.surf, self.cb_colour, self.rect.inflate(-2, -2), 1)
        pygame.draw.rect(self.surf, self.b_colour, self.rect, 1)

        self.surf.blit(
            self.label,
            (
                (self.rect.width / 2) - self.label.get_width() / 2,
                (self.rect.height / 2) - self.label.get_height() / 2,
            ),
        )

    def change_colours(self):
        c = self.i_colour[:]
        self.i_colour = self.b_colour[:]
        self.b_colour = c
        self.draw()
        self.blit()

    def on_click(self, event):
        if self.c_rect.collidepoint(event.pos):
            if event.type == pygame.MOUSEBUTTONUP:
                self.down = True
                self.change_colours()
                self.trigger(self.func[:])
