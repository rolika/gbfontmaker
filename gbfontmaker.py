"""Utility to create a font image for GB Studio."""


import pygame as pg


FONT_SIZE = 8  # font size in pixels
LAYOUT = (16, 14)   # layout of the font set per character (width, height)
BACKGROUND_COLOR = "#e0f8cf"


def make_image() -> pg.Surface:
    """Create a pygame.Surface object holding the characters."""
    # steup the canvas
    canvas_width = FONT_SIZE * LAYOUT[0]
    canvas_height = FONT_SIZE * LAYOUT[1]
    background_color = pg.Color(BACKGROUND_COLOR)
    canvas = pg.Surface((canvas_width, canvas_height))
    canvas.fill(background_color)
    return canvas


def save2png(image:pg.Surface) -> None:
    """Save the image in .png format."""
    pg.image.save(image, "font.png")


if __name__ == "__main__":
    save2png(make_image())