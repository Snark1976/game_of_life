import random
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class GameOfLife(metaclass=SingletonMeta):
    def __init__(self, width=20, height=20, counter=0):
        self.__width = width
        self.__height = height
        self.counter = counter
        self.world = self.generate_universe()

    def form_new_generation(self):
        universe = self.world
        new_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]

        for i in range(len(universe)):
            for j in range(len(universe[0])):

                if universe[i][j] == 1:
                    if self.__get_near(universe, [i, j]) not in (2, 3):
                        new_world[i][j] = 2
                        continue
                    new_world[i][j] = 1
                    continue

                if self.__get_near(universe, [i, j]) == 3:
                    new_world[i][j] = 1
                    continue
                new_world[i][j] = 0
        self.world = new_world

    def generate_universe(self):
        return [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    @staticmethod
    def __get_near(universe, pos, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        count = 0
        for i in system:
            if universe[(pos[0] + i[0]) % len(universe)][(pos[1] + i[1]) % len(universe[0])] == 1:
                count += 1
        return count
