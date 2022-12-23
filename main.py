
from src.nh_data.terrain import NH_Terrain_Map
from src.nh_data.converter import convert_nhmap_to_basicmap, convert_basicmap_to_rectified_nhmap

if __name__ == '__main__':

    imported_map = NH_Terrain_Map()

    with open('terrainAcres.nht', 'rb') as f:
        data = f.read()

    imported_map.load_all(data)

    converted_map = convert_nhmap_to_basicmap(imported_map)
    # converted_map.save_img()

    rectified_nh_map = convert_basicmap_to_rectified_nhmap(converted_map)

    with open('terrainAcres_rectified.nht', 'wb') as f:
        f.write(rectified_nh_map.dump_all())

