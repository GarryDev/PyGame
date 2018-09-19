import resources as res
from tile import Tile
from random import randint, choice
import itertools

from enum import Enum
class TerrainType(Enum):
    FOREST = 0
    DESERT = 1

def create_chunk(terrain_type, _size):

    if (terrain_type is TerrainType.FOREST):

        tile_grid = []

        for _ in itertools.repeat(None, _size * _size):

            tile_id = None

            rand = randint(0, 2)

            if rand == 0:
                tile_id = choice([
                    res.TERRAIN_FOREST_GRASS_0 + randint(0, 6),
                    res.TERRAIN_FOREST_GRASS_7 + randint(0, 4)])
            elif rand == 1:
                tile_id = res.TERRAIN_FOREST_GRASS_2_0 + randint(0, 2)
            else:
                tile_id = choice([
                    res.TERRAIN_FOREST_GRASS_3_0 + randint(0, 6),
                    res.TERRAIN_FOREST_GRASS_3_7 + randint(0, 4)])

            tile_grid.append(Tile(tile_id))

        return tile_grid

    if (terrain_type is TerrainType.DESERT):
        raise Exception("NOT IMPLEMENTED")