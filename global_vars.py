from enum import Enum

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
VIEWPORT_SIZE = 512

class ObjectType(Enum):
    POINT = 1
    LINE = 2
    POLYGON = 3