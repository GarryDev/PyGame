#from enum import Enum, auto
#from random import choice

WIDTH = 32
HEIGHT = 32

# class Direction(Enum):
#     North = auto()
#     East = auto()
#     West = auto()
#     South = auto()

#     @classmethod
#     def rand(cls):
#         return choice(list(cls.__members__.values()))

#     def __repr__(self):
#         return '<%s.%s>' % (self.__class__.__name__, self.name)

class Tile:
    def __init__(self, id):
        self.id = id
#       self._dir = Direction.rand()