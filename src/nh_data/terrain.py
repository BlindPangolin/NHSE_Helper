from src.enums.tile_types import TerrainType, RoadType


class NH_Terrain_Tile(object):
    def __init__(self):
        self.elevation = 0

        self.terrain_type = TerrainType.Base
        self.terrain_variation = 0  # don't know what it is used for
        self.terrain_rotation = 0

        # TODO not yet handled beyond load/dump
        self.road_type = RoadType.Base
        self.road_variation = 0
        self.road_rotation = 0

    def dump(self):
        """
        Encode tile to NHSE dump format
        """
        data = self.terrain_type.value
        data += self.terrain_variation.to_bytes(1, byteorder='big') + b'\x00'
        data += self.terrain_rotation.to_bytes(1, byteorder='big') + b'\x00'

        # TODO
        data += self.road_type.value
        data += self.road_variation.to_bytes(1, byteorder='big') + b'\x00'
        data += self.road_rotation.to_bytes(1, byteorder='big') + b'\x00'

        data += self.elevation.to_bytes(1, byteorder='big') + b'\x00'
        return data

    def load(self, data):
        """
        Decode tile from NHSE dump
        """
        self.terrain_type = TerrainType(data[0:2])
        self.terrain_variation = data[2:4]
        self.terrain_rotation = int.from_bytes(data[4:5], byteorder='big')
        self.road_type = RoadType(data[6:8])
        self.road_variation = data[8:10]
        self.road_rotation = int.from_bytes(data[10:11], byteorder='big')
        self.elevation = int.from_bytes(data[12:13], byteorder='big')


class NH_Terrain_Acre(object):
    def __init__(self):
        self.block_array = [[NH_Terrain_Tile() for _ in range(16)] for _ in range(16)]

    def dump(self):
        """
        Encode acre to NHSE single-acre dump format
        """
        data = b''
        for y in range(16):
            for x in range(16):
                data += self.block_array[y][x].dump()
        return data

    def dump_cols(self):
        """
        Utility to dump all acre in the order NHSE export
        """
        list_dumps_columns = []
        for c in range(16):
            column = b''
            for y in range(16):
                column += self.block_array[y][c].dump()
            list_dumps_columns.append(column)
        return list_dumps_columns


class NH_Terrain_Map(object):
    def __init__(self):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F']
        self.acre_dict = {
            f"{l}{c}": NH_Terrain_Acre()
            for l in self.letters
            for c in range(7)
        }

    def dump_all(self):
        """
        Encode map to NHSE import-all format
        """
        data = b''
        for c in range(7):
            dict_dumps = {}
            for l in ['A', 'B', 'C', 'D', 'E', 'F']:
                dict_dumps[l] = self.acre_dict[f'{l}{c}'].dump_cols()
            for x in range(16):
                for l in ['A', 'B', 'C', 'D', 'E', 'F']:
                    data += dict_dumps[l].pop(0)
        return data

    def load_all(self, data):
        """
        Decode map from NHSE dump-all format
        """
        assert len(data) == 150528
        for letter_index, letter in enumerate(self.letters):
            offset_y = letter_index * 16
            for digit in range(7):
                acre = self.acre_dict[f'{letter}{digit}']
                offset_x = digit * 16

                for y in range(16):
                    for x in range(16):
                        offset = ((offset_y + y) + 96*(offset_x + x))*14
                        block_data = data[offset:offset+14]
                        acre.block_array[y][x].load(block_data)

    def debug_visualize_terrain_type_enum(self):
        """
        Creates an array of all terrain types and rotation
        This is intended to visualize those types and should be call on flattened map
        """
        list_terrains_types = [o for o in TerrainType]

        for l in self.letters[1:-1]:
            for c in range(1, 6):
                acre = self.acre_dict[f'{l}{c}']

                for b in range(8):
                    terrain = list_terrains_types.pop(0)

                    y = b * 2

                    for idx, orientation in enumerate([b'\x00\x00', b'\x01\x00', b'\x02\x00', b'\x03\x00']):
                        x = idx * 2

                        acre.map[y][x].terrain_type = terrain
                        acre.map[y][x].terrain_rotation = orientation
                        acre.map[y][x].elevation = 1

                    if len(list_terrains_types) == 0:
                        break
                if len(list_terrains_types) == 0:
                    break
            if len(list_terrains_types) == 0:
                break
