"""Utility to create a font image for GB Studio."""


import pygame as pg
import pygame.freetype as freetype


FONT_SIZE = 16  # font size in pixels
LAYOUT = (16, 14)   # layout of the font set per character (width, height)
BACKGROUND_COLOR = "#e0f8cf"
DEFAULT_FONT = "m5x7.ttf"
DEFAULT_FONT_COLOR = "black"


class Char(pg.sprite.Sprite):
    def __init__(self, char, fonttype, color, pos):
        super().__init__()
        self._char = char
        self._fonttype = fonttype
        self._color = color
        self.rect = self.image.get_rect(topleft=pos)

    @property
    def image(self):
        return self._fonttype.render(self._text, self._color)[0]


def make_image(font:str=DEFAULT_FONT,
               size:int=FONT_SIZE,
               fontcolor:str=DEFAULT_FONT_COLOR,
               background:str=BACKGROUND_COLOR) -> pg.Surface:
    """Create a pygame.Surface object holding the characters."""
    # setup the canvas
    canvas_width = FONT_SIZE * LAYOUT[0]
    canvas_height = FONT_SIZE * LAYOUT[1]
    fontcolor = pg.Color(fontcolor)
    background = pg.Color(background)
    canvas = pg.Surface((canvas_width, canvas_height))
    canvas.fill(background)
    
    # setup font
    fonttype = freetype.Font(font, size)

    # draw a text
    text, _ = fonttype.render("GB Studio Font Maker", fontcolor)
    canvas.blit(text, (0, 0))

    return canvas


def save2png(image:pg.Surface) -> None:
    """Save the image in .png format."""
    pg.image.save(image, "font.png")


if __name__ == "__main__":
    pg.init()
    save2png(make_image())
    pg.quit()