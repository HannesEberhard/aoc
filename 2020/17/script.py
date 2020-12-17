
from common import Day
from copy import deepcopy
from itertools import product


class Day_2020_17(Day):

    def initialize_state(self, dimensions, cycles):
        state = 0
        size = 2 + len(self.parsed) + 2 * cycles
        for d in range(dimensions):
            state = [deepcopy(state) for _ in range(size)]
        for y, row in enumerate(self.parsed):
            for x, cube_state in enumerate(row):
                if cube_state == "#":
                    coordinate = [size // 2] * dimensions
                    coordinate[1] = cycles + y + 1
                    coordinate[2] = cycles + x + 1
                    self.set_state(coordinate, state, 1)
        return state

    def get_state(self, coordinates, state):
        for index in reversed(coordinates):
            state = state[index]
        return state

    def set_state(self, coordinates, state, value):
        for index in list(reversed(coordinates))[:-1]:
            state = state[index]
        state[coordinates[0]] = value

    def count_active_neighbors(self, coordinate, state, dimensions):
        active_neighbors = 0
        for relative in product(range(-1, 2), repeat=dimensions):
            if len([1 for component in relative if component != 0]) != 0:
                neighbor = tuple(sum(x) for x in zip(coordinate, relative))
                active_neighbors += self.get_state(neighbor, state)
        return active_neighbors

    def step(self, state, dimensions):
        new_state = deepcopy(state)
        for coordinate in product(range(1, len(state) - 1), repeat=dimensions):
            cube_state = self.get_state(coordinate, state)
            active_neighbors = self.count_active_neighbors(coordinate, state, dimensions)
            if cube_state == 1 and active_neighbors not in [2, 3]:
                self.set_state(coordinate, new_state, 0)
            elif cube_state == 0 and active_neighbors == 3:
                self.set_state(coordinate, new_state, 1)
        return new_state

    def simulate(self, dimensions, cycles):
        state = self.initialize_state(dimensions, cycles)
        for _ in range(cycles):
            state = self.step(state, dimensions)
        return state

    def part_1(self):
        state = self.simulate(3, 6)
        active_cubes = 0
        for z in state:
            for y in z:
                active_cubes += sum(y)
        return active_cubes

    def part_2(self):
        state = self.simulate(4, 6)
        active_cubes = 0
        for z in state:
            for y in z:
                for x in y:
                    active_cubes += sum(x)
        return active_cubes


if __name__ == "__main__":
    Day_2020_17().solve()
