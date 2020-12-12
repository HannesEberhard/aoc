
from common import Day


class Day_2020_12(Day):

    def parse(self):
        return [[instruction[0], int(instruction[1:])] for instruction in super().parse()]

    def move_ship(self, position, orientation, instruction):
        action = instruction[0]
        value = instruction[1]
        if action == "N":
            return position + complex(0, value), orientation
        elif action == "S":
            return position + complex(0, -value), orientation
        elif action == "E":
            return position + complex(value, 0), orientation
        elif action == "W":
            return position + complex(-value, 0), orientation
        elif action == "L":
            angle = 1j ** (value / 90)
            return position, orientation * angle
        elif action == "R":
            angle = 1j ** (value / 90)
            return position, orientation / angle
        elif action == "F":
            displacement = value * orientation
            return position + displacement, orientation

    def move_waypoint(self, ship_position, waypoint_position, instruction):
        action = instruction[0]
        value = instruction[1]
        if action == "N":
            return ship_position, waypoint_position + complex(0, value)
        elif action == "S":
            return ship_position, waypoint_position + complex(0, -value)
        elif action == "E":
            return ship_position, waypoint_position + complex(value, 0)
        elif action == "W":
            return ship_position, waypoint_position + complex(-value, 0)
        elif action == "L":
            angle = 1j ** (value / 90)
            return ship_position, waypoint_position * angle
        elif action == "R":
            angle = 1j ** (value / 90)
            return ship_position, waypoint_position / angle
        elif action == "F":
            return ship_position + waypoint_position * value, waypoint_position

    def part_1(self):
        position = complex(0, 0)
        orientation = complex(1, 0)
        for instruction in self.parsed:
            position, orientation = self.move_ship(position, orientation, instruction)
        return int(abs(position.real) + abs(position.imag))

    def part_2(self):
        ship_position = complex(0, 0)
        waypoint_position = complex(10, 1)
        for instruction in self.parsed:
            ship_position, waypoint_position = self.move_waypoint(ship_position, waypoint_position, instruction)
        return int(abs(ship_position.real) + abs(ship_position.imag))


if __name__ == "__main__":
    Day_2020_12().solve()
