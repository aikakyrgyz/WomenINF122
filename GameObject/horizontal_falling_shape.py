from Board.tiles_board import TilesBoard
from Errors.errors import InvalidIndexError
from GameObject.falling_shape import FallingShape
from Tile.tileAbstractFactory import TileAbstractFactory


class HorizontalFallingShape(FallingShape):

    def __init__(self, number_of_tiles: int, tile_types: list[str], tile_factory: TileAbstractFactory,
                 tiles_board: TilesBoard, c):
        super(number_of_tiles, tile_types, tile_factory, tiles_board)
        self.isValidCol(c)
        self.col = c

    def isValidRow(self):
        if self.col < 0 or self.col + self.number_of_tiles > len(self.board.get_num_columns()):
            raise InvalidIndexError("The tile cannot fit within the board with the specified index")

    def create(self):
        for i in range(self.number_of_tiles):
            tile = self.tile_factory.create_tile(self.tile_types[i])
            tile.set_index(0, i)
            self._instance.append(tile)



