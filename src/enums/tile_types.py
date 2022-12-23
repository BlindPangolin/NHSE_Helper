import numpy as np
from enum import Enum


class TerrainType(Enum):
    """
    Tile types and their corresponding NHSE dump code

    Comments try to represent the context of the tile with symbols, centered on the tile itself

    For ground types:
    - ■ elevation >= current
    - □ elevation < current
    - x that one invisible base tile

    For water types:
    - ■ ground
    - □ water
    - ▽ waterfall; not an actual tile, just representing the waterfall
    - _ like ground but seem closer to the waterfall, don't know the context

    """

    # ■ ■ ■
    # ■ ■ ■
    # ■ ■ ■
    Base = b'\x00\x00'

    # □ □ □
    # □ ■ □
    # □ □ □
    Cliff0A = b'\x16\x00'
    Cliff0A_2 = b'\x17\x00'  # difference ?
    Cliff0A_3 = b'\x18\x00'  # difference ?
    # □ □ □
    # □ ■ □
    # □ ■ □
    Cliff1A = b'\x19\x00'
    Cliff1A_2 = b'\x1A\x00'  # difference ?
    Cliff1A_3 = b'\x1B\x00'  # difference ?

    # □ ■ □
    # □ ■ □
    # □ ■ □
    Cliff2A = b'\x1C\x00'
    # □ □ □
    # □ ■ ■
    # □ ■ □
    Cliff2C = b'\x1D\x00'

    # □ □ □
    # □ ◢■
    # □ ■ ■
    Cliff3B = b'\x1F\x00'
    # □ □ □
    # □ ■ ■
    # □ ■ ■
    Cliff3C = b'\x20\x00'

    # □ ■ □
    # □ ■ ■
    # □ ■ □
    Cliff3A = b'\x1E\x00'
    # □ ■ □
    # □ ■ ■
    # □ ■ ■
    Cliff4A = b'\x21\x00'
    # □ ■ ■
    # □ ■ ■
    # □ ■ □
    Cliff4B = b'\x22\x00'
    # □ ■ □
    # ■ ■ ■
    # □ ■ □
    Cliff4C = b'\x23\x00'
    # □ ■ □
    # ■ ■ ■
    # ■ ■ □
    Cliff5A = b'\x24\x00'
    # □ ■ ■
    # □ ■ ■
    # □ ■ ■
    Cliff5B = b'\x25\x00'
    # □ ■ ■
    # ■ ■ ■
    # ■ ■ □
    Cliff6A = b'\x26\x00'
    # ■ ■ ■
    # ■ ■ ■
    # □ ■ □
    Cliff6B = b'\x27\x00'
    # ■ ■ ■
    # ■ ■ ■
    # □ ■ ■
    Cliff7A = b'\x28\x00'
    # □ □ □
    # □ x □
    # □ □ □
    Cliff8 = b'\x29\x00'  # invisible
    # □ □ □
    # □ ◢■
    # □ ■ □
    Cliff2B = b'\x93\x00'

    # WATER

    # ■ ■ ■
    # ■ □ ■
    # ■ ■ ■
    River0A = b'\x01\x00'
    # ■ ■ ■
    # ■ □ ■
    # ■ □ ■
    River1A = b'\x04\x00'
    # ■ □ ■
    # ■ □ ■
    # ■ □ ■
    River2A = b'\x07\x00'
    # ■ ■ ■
    # ■ ◤□
    # ■ □ ■
    River2B = b'\x08\x00'
    # ■ ■ ■
    # ■ □ □
    # ■ □ ■
    River2C = b'\x09\x00'
    # ■ □ ■
    # ■ □ □
    # ■ □ ■
    River3A = b'\x0A\x00'
    # ■ ■ ■
    # ■ ◤□
    # ■ □ □
    River3B = b'\x0B\x00'
    # ■ ■ ■
    # ■ □ □
    # ■ □ □
    River3C = b'\x0C\x00'
    # ■ □ ■
    # ■ □ □
    # ■ □ □
    River4A = b'\x0D\x00'
    # ■ □ □
    # ■ □ □
    # ■ □ ■
    River4B = b'\x0E\x00'
    # ■ □ ■
    # □ □ □
    # ■ □ ■
    River4C = b'\x0F\x00'
    # ■ □ ■
    # □ □ □
    # □ □ ■
    River5A = b'\x10\x00'
    # ■ □ □
    # ■ □ □
    # ■ □ □
    River5B = b'\x11\x00'
    # ■ □ □
    # □ □ □
    # □ □ ■
    River6A = b'\x12\x00'
    # □ □ □
    # □ □ □
    # ■ □ ■
    River6B = b'\x13\x00'
    # □ □ □
    # □ □ □
    # ■ □ □
    River7A = b'\x14\x00'
    # □ □ □
    # □ □ □
    # □ □ □
    River8A = b'\x15\x00'
    # ■ □ ■
    # ■ □ ■
    # ■ ▽ ■
    # ■ _ ■
    Fall101 = b'\x3A\x00'
    # ■ □ ■
    # ■ □ ■
    # ■ ▽ ■
    # ■ □ ■
    Fall100 = b'\x3B\x00'
    # ■ □ □
    # ■ □ □
    # ■ ▽ ▽
    # ■ □ □
    Fall300 = b'\x3C\x00'
    # ■ □ □
    # ■ □ □
    # ■ ▽ ▽
    # ■ □ ■
    Fall301 = b'\x3D\x00'
    # ■ □ □
    # ■ □ □
    # ■ ▽ ▽
    # ■ _ ■
    Fall302 = b'\x3E\x00'
    # □ □ ■
    # □ □ ■
    # ▽ ▽ ■
    # □ □ ■
    Fall200 = b'\x3F\x00'
    # □ □ ■
    # □ □ ■
    # ▽ ▽ ■
    # ■ □ ■
    Fall201 = b'\x40\x00'
    # □ □ ■
    # □ □ ■
    # ▽ ▽ ■
    # ■ _ ■
    Fall202 = b'\x41\x00'
    # □ □ □
    # □ □ □
    # ▽ ▽ ▽
    # □ □ □
    Fall400 = b'\x42\x00'
    # □ □ □
    # □ □ □
    # ▽ ▽ ▽
    # □ □ ■
    Fall401 = b'\x43\x00'
    # □ □ □
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ □
    Fall402 = b'\x44\x00'
    # □ □ □
    # □ □ □
    # ▽ ▽ ▽
    # □ ■ □
    Fall403 = b'\x45\x00'
    # □ □ □
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ ■
    Fall404 = b'\x46\x00'
    # ■ ■ ■
    # ■ □ ■
    # ■ ▽ ■
    # ■ _ ■
    Fall103 = b'\x71\x00'
    # ■ ■ ■
    # ■ □ ■
    # ■ ▽ ■
    # ■ □ ■
    Fall102 = b'\x72\x00'
    # ■ □ ■
    # ■ □ □
    # ■ ▽ ▽
    # ■ □ □
    Fall303 = b'\x73\x00'
    # ■ ■ ■
    # ■ □ □
    # ■ ▽ ▽
    # ■ □ □
    Fall304 = b'\x74\x00'
    # ■ □ ■
    # ■ □ □
    # ■ ▽ ▽
    # ■ □ ■
    Fall305 = b'\x75\x00'
    # ■ ■ ■
    # ■ □ □
    # ■ ▽ ▽
    # ■ □ ■
    Fall306 = b'\x76\x00'
    # ■ □ ■
    # ■ □ □
    # ■ ▽ ▽
    # ■ ■ □
    Fall307 = b'\x77\x00'
    # ■ ■ ■
    # ■ □ □
    # ■ ▽ ▽
    # ■ ■ □
    Fall308 = b'\x78\x00'
    # ■ □ ■
    # □ □ ■
    # ▽ ▽ ■
    # □ □ ■
    Fall203 = b'\x79\x00'
    # ■ ■ ■
    # □ □ ■
    # ▽ ▽ ■
    # □ □ ■
    Fall204 = b'\x7A\x00'
    # ■ □ ■
    # □ □ ■
    # ▽ ▽ ■
    # ■ □ ■
    Fall205 = b'\x7B\x00'
    # ■ ■ ■
    # □ □ ■
    # ▽ ▽ ■
    # ■ □ ■
    Fall206 = b'\x7C\x00'
    # ■ □ ■
    # □ □ ■
    # ▽ ▽ ■
    # □ ■ ■
    Fall207 = b'\x7D\x00'
    # ■ ■ ■
    # □ □ ■
    # ▽ ▽ ■
    # □ ■ ■
    Fall208 = b'\x7E\x00'
    # □ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # □ □ □
    Fall405 = b'\x7F\x00'
    # ■ □ □
    # □ □ □
    # ▽ ▽ ▽
    # □ □ □
    Fall406 = b'\x80\x00'
    # ■ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # □ □ □
    Fall407 = b'\x81\x00'
    # ■ ■ ■
    # □ □ □
    # ▽ ▽ ▽
    # □ □ □
    Fall408 = b'\x82\x00'
    # □ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ □
    Fall410 = b'\x83\x00'
    # ■ □ □
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ □
    Fall409 = b'\x84\x00'
    # ■ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ □
    Fall411 = b'\x85\x00'
    # ■ ■ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ □
    Fall412 = b'\x86\x00'
    # □ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # □ □ ■
    Fall414 = b'\x87\x00'
    # ■ □ □
    # □ □ □
    # ▽ ▽ ▽
    # □ □ ■
    Fall413 = b'\x88\x00'
    # ■ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # □ □ ■
    Fall415 = b'\x89\x00'
    # ■ ■ ■
    # □ □ □
    # ▽ ▽ ▽
    # □ □ ■
    Fall416 = b'\x8A\x00'
    # □ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ ■
    Fall418 = b'\x8B\x00'
    # ■ □ □
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ ■
    Fall417 = b'\x8C\x00'
    # ■ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ ■
    Fall419 = b'\x8D\x00'
    # ■ ■ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ □ ■
    Fall420 = b'\x8E\x00'
    # □ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ ■ ■
    Fall422 = b'\x8F\x00'
    # ■ □ □
    # □ □ □
    # ▽ ▽ ▽
    # ■ ■ ■
    Fall421 = b'\x90\x00'
    # ■ □ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ ■ ■
    Fall423 = b'\x91\x00'
    # ■ ■ ■
    # □ □ □
    # ▽ ▽ ▽
    # ■ ■ ■
    Fall424 = b'\x92\x00'

    def is_ground(self):
        return self in [
            TerrainType.Base, TerrainType.Cliff0A, TerrainType.Cliff0A_2, TerrainType.Cliff0A_3, TerrainType.Cliff1A,
            TerrainType.Cliff1A_2, TerrainType.Cliff1A_3, TerrainType.Cliff2A, TerrainType.Cliff2C, TerrainType.Cliff3B,
            TerrainType.Cliff3C, TerrainType.Cliff3A, TerrainType.Cliff4A, TerrainType.Cliff4B, TerrainType.Cliff4C,
            TerrainType.Cliff5A, TerrainType.Cliff5B, TerrainType.Cliff6A, TerrainType.Cliff6B, TerrainType.Cliff7A,
            TerrainType.Cliff8, TerrainType.Cliff2B
        ]


class RoadType(Enum):
    """
    TODO handle roads
    """
    Base = b'\x00\x00'
    RoadSoil0A = b'\x47\x00'
    RoadSoil1A = b'\x48\x00'
    RoadSoil0B = b'\x49\x00'
    RoadSoil1B = b'\x4B\x00'
    RoadSoil1C = b'\x4C\x00'
    RoadSoil2A = b'\x4D\x00'
    RoadSoil2B = b'\x4E\x00'
    RoadSoil2C = b'\x4F\x00'
    RoadSoil3A = b'\x50\x00'
    RoadSoil3B = b'\x51\x00'
    RoadSoil3C = b'\x52\x00'
    RoadSoil4A = b'\x53\x00'
    RoadSoil4B = b'\x54\x00'
    RoadSoil4C = b'\x55\x00'
    RoadSoil5A = b'\x56\x00'
    RoadSoil5B = b'\x57\x00'
    RoadSoil6A = b'\x58\x00'
    RoadSoil6B = b'\x59\x00'
    RoadSoil7A = b'\x5A\x00'
    RoadSoil8A = b'\x5B\x00'
    RoadStone0A = b'\x5C\x00'
    RoadStone0B = b'\x5D\x00'
    RoadStone1A = b'\x5F\x00'
    RoadStone1B = b'\x60\x00'
    RoadStone1C = b'\x61\x00'
    RoadStone2A = b'\x62\x00'
    RoadStone2B = b'\x63\x00'
    RoadStone2C = b'\x64\x00'
    RoadStone3A = b'\x65\x00'
    RoadStone3B = b'\x66\x00'
    RoadStone3C = b'\x67\x00'
    RoadStone4A = b'\x68\x00'
    RoadStone4B = b'\x69\x00'
    RoadStone4C = b'\x6A\x00'
    RoadStone5A = b'\x6B\x00'
    RoadStone5B = b'\x6C\x00'
    RoadStone6A = b'\x6D\x00'
    RoadStone6B = b'\x6E\x00'
    RoadStone7A = b'\x6F\x00'
    RoadStone8A = b'\x70\x00'
    RoadBrick0A = b'\x94\x00'
    RoadBrick0B = b'\x95\x00'
    RoadBrick1A = b'\x97\x00'
    RoadBrick1B = b'\x98\x00'
    RoadBrick1C = b'\x99\x00'
    RoadBrick2A = b'\x9A\x00'
    RoadBrick2B = b'\x9B\x00'
    RoadBrick2C = b'\x9C\x00'
    RoadBrick3A = b'\x9D\x00'
    RoadBrick3B = b'\x9E\x00'
    RoadBrick3C = b'\x9F\x00'
    RoadBrick4A = b'\xA0\x00'
    RoadBrick4B = b'\xA1\x00'
    RoadBrick4C = b'\xA2\x00'
    RoadBrick5A = b'\xA3\x00'
    RoadBrick5B = b'\xA4\x00'
    RoadBrick6A = b'\xA5\x00'
    RoadBrick6B = b'\xA6\x00'
    RoadBrick7A = b'\xA7\x00'
    RoadBrick8A = b'\xA8\x00'
    RoadDarkSoil0A = b'\xA9\x00'
    RoadDarkSoil0B = b'\xAA\x00'
    RoadDarkSoil1A = b'\xAC\x00'
    RoadDarkSoil1B = b'\xAD\x00'
    RoadDarkSoil1C = b'\xAE\x00'
    RoadDarkSoil2A = b'\xAF\x00'
    RoadDarkSoil2B = b'\xB0\x00'
    RoadDarkSoil2C = b'\xB1\x00'
    RoadDarkSoil3A = b'\xB2\x00'
    RoadDarkSoil3B = b'\xB3\x00'
    RoadDarkSoil3C = b'\xB4\x00'
    RoadDarkSoil4A = b'\xB5\x00'
    RoadDarkSoil4B = b'\xB6\x00'
    RoadDarkSoil4C = b'\xB7\x00'
    RoadDarkSoil5A = b'\xB8\x00'
    RoadDarkSoil5B = b'\xB9\x00'
    RoadDarkSoil6A = b'\xBA\x00'
    RoadDarkSoil6B = b'\xBB\x00'
    RoadDarkSoil7A = b'\xBC\x00'
    RoadDarkSoil8A = b'\xBD\x00'
    RoadFanPattern0A = b'\xBE\x00'
    RoadFanPattern0B = b'\xBF\x00'
    RoadFanPattern1A = b'\xC1\x00'
    RoadFanPattern1B = b'\xC2\x00'
    RoadFanPattern1C = b'\xC3\x00'
    RoadFanPattern2A = b'\xC4\x00'
    RoadFanPattern2B = b'\xC5\x00'
    RoadFanPattern2C = b'\xC6\x00'
    RoadFanPattern3A = b'\xC7\x00'
    RoadFanPattern3B = b'\xC8\x00'
    RoadFanPattern3C = b'\xC9\x00'
    RoadFanPattern4A = b'\xCA\x00'
    RoadFanPattern4B = b'\xCB\x00'
    RoadFanPattern4C = b'\xCC\x00'
    RoadFanPattern5A = b'\xCD\x00'
    RoadFanPattern5B = b'\xCE\x00'
    RoadFanPattern6A = b'\xCF\x00'
    RoadFanPattern6B = b'\xD0\x00'
    RoadFanPattern7A = b'\xD1\x00'
    RoadFanPattern8A = b'\xD2\x00'
    RoadSand0A = b'\xD3\x00'
    RoadSand0B = b'\xD4\x00'
    RoadSand1A = b'\xD6\x00'
    RoadSand1B = b'\xD7\x00'
    RoadSand1C = b'\xD8\x00'
    RoadSand2A = b'\xD9\x00'
    RoadSand2B = b'\xDA\x00'
    RoadSand2C = b'\xDB\x00'
    RoadSand3A = b'\xDC\x00'
    RoadSand3B = b'\xDD\x00'
    RoadSand3C = b'\xDE\x00'
    RoadSand4A = b'\xDF\x00'
    RoadSand4B = b'\xE0\x00'
    RoadSand4C = b'\xE1\x00'
    RoadSand5A = b'\xE2\x00'
    RoadSand5B = b'\xE3\x00'
    RoadSand6A = b'\xE4\x00'
    RoadSand6B = b'\xE5\x00'
    RoadSand7A = b'\xE6\x00'
    RoadSand8A = b'\xE7\x00'
    RoadTile0A = b'\xE8\x00'
    RoadTile0B = b'\xE9\x00'
    RoadTile1A = b'\xEB\x00'
    RoadTile1B = b'\xEC\x00'
    RoadTile1C = b'\xED\x00'
    RoadTile2A = b'\xEE\x00'
    RoadTile2B = b'\xEF\x00'
    RoadTile2C = b'\xF0\x00'
    RoadTile3A = b'\xF1\x00'
    RoadTile3B = b'\xF2\x00'
    RoadTile3C = b'\xF3\x00'
    RoadTile4A = b'\xF4\x00'
    RoadTile4B = b'\xF5\x00'
    RoadTile4C = b'\xF6\x00'
    RoadTile5A = b'\xF7\x00'
    RoadTile5B = b'\xF8\x00'
    RoadTile6A = b'\xF9\x00'
    RoadTile6B = b'\xFA\x00'
    RoadTile7A = b'\xFB\x00'
    RoadTile8A = b'\xFC\x00'
    RoadWood0A = b'\xFD\x00'
    RoadWood0B = b'\xFE\x00'
    RoadWood1A = b'\x10\x00'
    RoadWood1B = b'\x10\x01'
    RoadWood1C = b'\x10\x02'
    RoadWood2A = b'\x10\x03'
    RoadWood2B = b'\x10\x04'
    RoadWood2C = b'\x10\x05'
    RoadWood3A = b'\x10\x06'
    RoadWood3B = b'\x10\x07'
    RoadWood3C = b'\x10\x08'
    RoadWood4A = b'\x10\x09'
    RoadWood4B = b'\x10\x0A'
    RoadWood4C = b'\x10\x0B'
    RoadWood5A = b'\x10\x0C'
    RoadWood5B = b'\x10\x0D'
    RoadWood6A = b'\x10\x0E'
    RoadWood6B = b'\x10\x0F'
    RoadWood7A = b'\x11\x00'
    RoadWood8A = b'\x11\x01'


def create_patches_array(string):
    dv = {
        "G": 1,
        "W": -1,
        "■": 1,
        "□": -1,
        ".": 0
    }

    patch_type = np.array([dv[o] for o in string[0::2]]).reshape((3, 3))
    patch_elevation = np.array([dv[o] for o in string[1::2]]).reshape((3, 3))

    return patch_type, patch_elevation


dict_patches = {
    TerrainType.Base: create_patches_array('.■.■.■'
                                           '.■G■.■'
                                           '.■.■.■'),
    
    TerrainType.Cliff0A: create_patches_array('...□..'
                                              '.□G■.□'
                                              '...□..'),

    TerrainType.Cliff1A: create_patches_array('...□..'
                                              '.□G■.□'
                                              '...■..'),

    TerrainType.Cliff2A: create_patches_array('...■..'
                                              '.□G■.□'
                                              '...■..'),

    TerrainType.Cliff2C: create_patches_array('...□..'
                                              '.□G■.■'
                                              '...■.□'),  # default square

    TerrainType.Cliff3B: create_patches_array('...□..'
                                              '.□G■.■'
                                              '...■.■'),  # default triangle

    TerrainType.Cliff3A: create_patches_array('...■.□'
                                              '.□G■.■'
                                              '...■.□'),

    TerrainType.Cliff4A: create_patches_array('...■.□'
                                              '.□G■.■'
                                              '...■.■'),

    TerrainType.Cliff4B: create_patches_array('...■.■'
                                              '.□G■.■'
                                              '...■.□'),

    TerrainType.Cliff4C: create_patches_array('.□.■.□'
                                              '.■G■.■'
                                              '.□.■.□'),

    TerrainType.Cliff5A: create_patches_array('.□.■.□'
                                              '.■G■.■'
                                              '.■.■.□'),

    TerrainType.Cliff5B: create_patches_array('...■.■'
                                              '.□G■.■'
                                              '...■.■'),

    TerrainType.Cliff6A: create_patches_array('.□.■.■'
                                              '.■G■.■'
                                              '.■.■.□'),

    TerrainType.Cliff6B: create_patches_array('.■.■.■'
                                              '.■G■.■'
                                              '.□.■.□'),

    TerrainType.Cliff7A: create_patches_array('.■.■.■'
                                              '.■G■.■'
                                              '.□.■.■'),

    TerrainType.River0A: create_patches_array('..G■..'
                                              'G■W■G■'
                                              '..G■..'),

    TerrainType.River1A: create_patches_array('..G■..'
                                              'G■W■G■'
                                              '.■W■.■'),

    TerrainType.River2A: create_patches_array('.■W■.■'
                                              'G■W■G■'
                                              '.■W■.■'),

    TerrainType.River2C: create_patches_array('..G■.■'
                                              'G■W■W■'
                                              '.■W■G■'),  # default square

    TerrainType.River3A: create_patches_array('.■W■G■'
                                              'G■W■W■'
                                              '.■W■G■'),

    TerrainType.River3B: create_patches_array('..G■.■'
                                              'G■W■W■'
                                              '.■W■W■'),  # default triangle

    TerrainType.River4A: create_patches_array('.■W■G■'
                                              'G■W■W■'
                                              '.■W■W■'),

    TerrainType.River4B: create_patches_array('.■W■W■'
                                              'G■W■W■'
                                              '.■W■G■'),

    TerrainType.River4C: create_patches_array('G■W■G■'
                                              'W■W■W■'
                                              'G■W■G■'),

    TerrainType.River5A: create_patches_array('G■W■G■'
                                              'W■W■W■'
                                              'W■W■G■'),

    TerrainType.River5B: create_patches_array('.■W■W■'
                                              'G■W■W■'
                                              '.■W■W■'),

    TerrainType.River6A: create_patches_array('G■W■W■'
                                              'W■W■W■'
                                              'W■W■G■'),

    TerrainType.River6B: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'G■W■G■'),

    TerrainType.River7A: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'G■W■W■'),

    TerrainType.River8A: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'W■W■W■'),

    TerrainType.Fall101: create_patches_array('.■W■.■'
                                              'G■W■G■'
                                              'G.G□G.'),  #

    TerrainType.Fall100: create_patches_array('.■W■.■'
                                              'G■W■G■'
                                              'G.W□G.'),

    TerrainType.Fall300: create_patches_array('.■W■W■'
                                              'G■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall301: create_patches_array('.■W■W■'
                                              'G■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall302: create_patches_array('.■W■W■'
                                              'G■W■W■'
                                              'G.G□G.'),  #

    TerrainType.Fall200: create_patches_array('W■W■.■'
                                              'W■W■G■'
                                              'W□W□G.'),

    TerrainType.Fall201: create_patches_array('W■W■.■'
                                              'W■W■G■'
                                              'G.W□G.'),

    TerrainType.Fall202: create_patches_array('W■W■.■'
                                              'W■W■G■'
                                              'G.G□G.'),  #

    TerrainType.Fall400: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'W□W□W□'),

    TerrainType.Fall401: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'W□W□G.'),

    TerrainType.Fall402: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall403: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'W□G□W□'),  #

    TerrainType.Fall404: create_patches_array('W■W■W■'
                                              'W■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall103: create_patches_array('..G■..'
                                              'G■W■G■'
                                              'G.G□G.'),  #

    TerrainType.Fall102: create_patches_array('..G■..'
                                              'G■W■G■'
                                              'G.W□G.'),

    TerrainType.Fall303: create_patches_array('.■W■G■'
                                              'G■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall304: create_patches_array('.■G■.■'
                                              'G■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall305: create_patches_array('.■W■.■'
                                              'G■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall306: create_patches_array('.■G■.■'
                                              'G■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall307: create_patches_array('.■W■.■'
                                              'G■W■W■'
                                              'G.G□W□'),

    TerrainType.Fall308: create_patches_array('.■G■G■'
                                              'G■W■W■'
                                              'G.G□W□'),

    TerrainType.Fall203: create_patches_array('G■W■.■'
                                              'W■W■G■'
                                              'W□W□G.'),

    TerrainType.Fall204: create_patches_array('.■G■.■'
                                              'W■W■G■'
                                              'W□W□G.'),

    TerrainType.Fall205: create_patches_array('.■W■.■'
                                              'W■W■G■'
                                              'G.W□G.'),

    TerrainType.Fall206: create_patches_array('.■G■.■'
                                              'W■W■G■'
                                              'G□W□G.'),

    TerrainType.Fall207: create_patches_array('.■W■.■'
                                              'W■W■G■'
                                              'W□G□G.'),

    TerrainType.Fall208: create_patches_array('.■G■.■'
                                              'W■W■G■'
                                              'W□G□G.'),

    TerrainType.Fall405: create_patches_array('W■W■G■'
                                              'W■W■W■'
                                              'W□W□W□'),

    TerrainType.Fall406: create_patches_array('G■W■W■'
                                              'W■W■W■'
                                              'W□W□W□'),

    TerrainType.Fall407: create_patches_array('G■W■G■'
                                              'W■W■W■'
                                              'W□W□W□'),

    TerrainType.Fall408: create_patches_array('.■G■.■'
                                              'W■W■W■'
                                              'W□W□W□'),

    TerrainType.Fall410: create_patches_array('W■W■G■'
                                              'W■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall409: create_patches_array('G■W■W■'
                                              'W■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall411: create_patches_array('G■W■G■'
                                              'W■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall412: create_patches_array('.■G■.■'
                                              'W■W■W■'
                                              'G.W□W□'),

    TerrainType.Fall414: create_patches_array('W■W■G■'
                                              'W■W■W■'
                                              'W□W□G.'),

    TerrainType.Fall413: create_patches_array('G■W■W■'
                                              'W■W■W■'
                                              'W□W□G.'),

    TerrainType.Fall415: create_patches_array('G■W■G■'
                                              'W■W■W■'
                                              'W□W□G.'),

    TerrainType.Fall416: create_patches_array('.■G■.■'
                                              'W■W■W■'
                                              'W□W□G.'),

    TerrainType.Fall418: create_patches_array('W■W■G■'
                                              'W■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall417: create_patches_array('G■W■W■'
                                              'W■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall419: create_patches_array('G■W■G■'
                                              'W■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall420: create_patches_array('.■G■.■'
                                              'W■W■W■'
                                              'G.W□G.'),

    TerrainType.Fall422: create_patches_array('W■W■G■'
                                              'W■W■W■'
                                              'G.G□G.'),

    TerrainType.Fall421: create_patches_array('G■W■W■'
                                              'W■W■W■'
                                              'G.G□G.'),

    TerrainType.Fall423: create_patches_array('G■W■G■'
                                              'W■W■W■'
                                              'G.G□G.'),

    TerrainType.Fall424: create_patches_array('.■G■.■'
                                              'W■W■W■'
                                              'G.G□G.'),
}

# Stores corresponding tiles with alternative shapes
dict_alternatives = {
    TerrainType.Cliff3B: TerrainType.Cliff3C,  # default triangle
    TerrainType.Cliff3C: TerrainType.Cliff3B,
    TerrainType.Cliff2C: TerrainType.Cliff2B,  # default square
    TerrainType.Cliff2B: TerrainType.Cliff2C,
    TerrainType.River2C: TerrainType.River2B,  # default square
    TerrainType.River2B: TerrainType.River2C,
    TerrainType.River3B: TerrainType.River3C,  # default triangle
    TerrainType.River3C: TerrainType.River3B,
}