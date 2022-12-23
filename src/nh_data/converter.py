import numpy as np
import scipy.signal

from src.enums.tile_types import dict_patches
from src.nh_data.terrain import NH_Terrain_Map
from src.internal_data.terrain import BasicMap, BasicTileType


def convert_nhmap_to_basicmap(nh_map: NH_Terrain_Map):
    """
    Converter from NHSE_Map to Map
    """
    basic_map = BasicMap()

    for y in range(basic_map.HEIGHT):
        letter = chr(ord('A') + (y//16))
        for x in range(basic_map.WIDTH):
            digit = x // 16
            acre = nh_map.acre_dict[f'{letter}{digit}']
            block = acre.block_array[y % 16][x % 16]

            elevation = block.elevation
            terrain_type = block.terrain_type

            basic_map.array[y][x].elevation = elevation
            basic_map.array[y][x].type = BasicTileType.GROUND if terrain_type.is_ground() else BasicTileType.WATER

    return basic_map


def convert_basicmap_to_rectified_nhmap(basic_map: BasicMap):
    """
    Converter from Map to NH_Map
    """
    nh_map = NH_Terrain_Map()

    array_types = np.array([
        [
            1 if basic_map.array[l][c].type == BasicTileType.GROUND else -1
            for c in range(basic_map.WIDTH)
        ]
        for l in range(basic_map.HEIGHT)
    ])

    array_elevations = np.array([
        [
            basic_map.array[l][c].elevation
            for c in range(basic_map.WIDTH)
        ]
        for l in range(basic_map.HEIGHT)
    ])

    mask_map_edges = np.ones_like(array_types)  # to prevent modification on map edges, underwater
    mask_map_edges[0, :] = 0
    mask_map_edges[basic_map.HEIGHT-1, :] = 0
    mask_map_edges[:, 0] = 0
    mask_map_edges[:, basic_map.WIDTH-1] = 0

    for terrain_type, (kernel_type, kernel_elevation) in dict_patches.items():

        thr_elev = np.sum(kernel_elevation[kernel_elevation > 0])
        thr_type = len(np.nonzero(kernel_type[kernel_type != 0])[0])

        for rotation in range(4):
            # create mask for right tiles type
            corr_type = scipy.signal.correlate2d(array_types, kernel_type, mode="same")
            corr_type[corr_type < thr_type] = 0
            corr_type[corr_type >= thr_type] = 1

            if np.sum(corr_type) == 0:
                kernel_type = np.rot90(kernel_type)
                kernel_elevation = np.rot90(kernel_elevation)
                continue

            for elevation in range(0, 7):
                if not isinstance(elevation, int):  # weird glitch when debugging, unnecessary on normal runtime
                    break
                # select specific elevation
                ael2 = array_elevations.copy()
                ael2[array_elevations < elevation] = 0
                ael2[array_elevations >= elevation] = 1

                # create mask for right tiles elevation
                matches = scipy.signal.correlate2d(ael2, kernel_elevation, mode="same")
                matches[matches < thr_elev] = 0

                matches[corr_type == 0] = 0  # remove wrong types
                matches[mask_map_edges == 0] = 0  # remove edges

                list_x, list_y = np.nonzero(matches)
                for (y, x) in list(zip(list_x, list_y)):

                    letter = chr(ord('A') + (y // 16))
                    digit = x // 16
                    acre = nh_map.acre_dict[f'{letter}{digit}']
                    block = acre.block_array[y % 16][x % 16]

                    if block.elevation > elevation:
                        continue

                    block.terrain_type = terrain_type
                    block.terrain_rotation = rotation
                    block.elevation = elevation

            kernel_type = np.rot90(kernel_type)
            kernel_elevation = np.rot90(kernel_elevation)

    return nh_map


