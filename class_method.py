from dataclasses import dataclass
import math
@dataclass
class Coordinate:
    x: int = 0
    y: int = 0

    def show_coordinate(self):
        print(self.x, self.y)

    @classmethod
    def create_new_cood(cls, x, y):
        new_cood = cls()
        new_cood.x = x
        new_cood.y = y
        return new_cood

    @staticmethod
    def calc_dist(cood1, cood2):
        x = cood1.x - cood2.x
        y = cood1.y - cood2.y
        return math.sqrt((math.pow(x, 2) + math.pow(y, 2)))

# class method
cood = Coordinate()
cood2 = cood.create_new_cood(10, 20)
cood2.show_coordinate()

# static_method
cood1 = Coordinate(100, 100)
cood2 = Coordinate(200, 200)

dist = Coordinate.calc_dist(cood1, cood2)
print(dist)