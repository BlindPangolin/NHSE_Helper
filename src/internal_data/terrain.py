from enum import Enum
from PIL import Image


class BasicTileType(Enum):
    GROUND = 0
    WATER = 1


class BasicTile(object):
    """
    Simple representation of the terrain
    Handles Ground, Water and elevation
    """
    def __init__(self, elevation=0, type=BasicTileType.GROUND, is_triangle=False):
        self.elevation = elevation
        self.type = type
        self.is_triangle = is_triangle  # for future use


class BasicMap(object):
    WIDTH = 112
    HEIGHT = 96

    def __init__(self):
        self.array = [[BasicTile() for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]

    def save_img(self):
        """
        Debug utility to visualize map as image
        """
        img = Image.new('RGB', (self.WIDTH, self.HEIGHT))

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                tile = self.array[y][x]
                if tile.type == BasicTileType.GROUND:
                    color = (
                        tile.elevation * 25,
                        100 + tile.elevation * 15,
                        tile.elevation * 25
                    )
                else:
                    color = (
                        tile.elevation * 25,
                        tile.elevation * 25,
                        150 + tile.elevation * 10
                    )

                img.putpixel((x, y), tuple(color))
        img.save('map.png')

    def from_img(self, img):
        """
        Load from PIL image
        Could be use after user modifications from external image-editing tools
        """
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                color = img.getpixel((x, y))

                if color[1] > color[2]:
                    self.array[y][x].type = BasicTileType.GROUND
                else:
                    self.array[y][x].type = BasicTileType.WATER
                self.array[y][x].elevation = int(round(color[0] / 25))
