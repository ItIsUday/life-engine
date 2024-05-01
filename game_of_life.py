from collections import defaultdict
from itertools import product
from pprint import pprint


def init_world(size):
    world = [[0] * size for _ in range(size)]
    return world


def neighbors(world, row, col):
    neighbor_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in neighbor_cells:
        if 0 <= (x := row + dx) <= len(world) - 1 and 0 <= (y := col + dy) <= len(world) - 1:
            yield world[x][y]


def alive_neighbor_count(world, row, col):
    return sum(neighbors(world, row, col))


def apply_rules(world):
    delta = defaultdict(int)

    for x, y in product(range(len(world)), range(len(world))):
        alive_neighbor = alive_neighbor_count(world, x, y)
        if world[x][y]:
            delta[(x, y)] = 1 if alive_neighbor in (2, 3) else 0
        if not world[x][y] and alive_neighbor == 3:
            delta[(x, y)] = 1

    return delta


def next_world(world):
    delta = apply_rules(world)
    new_world = init_world(len(world))
    for (x, y), state in delta.items():
        new_world[x][y] = state

    return new_world


def init_blinker_world():
    world = init_world(5)
    world[2][1] = 1
    world[2][2] = 1
    world[2][3] = 1

    return world


def init_toad_world():
    world = init_world(6)
    world[3][1] = 1
    world[3][2] = 1
    world[3][3] = 1
    world[2][2] = 1
    world[2][3] = 1
    world[2][4] = 1

    return world


def main():
    world = init_toad_world()
    iterations = 4
    pprint(world)
    for _ in range(iterations):
        world = next_world(world)
        print()
        pprint(world)


if __name__ == "__main__":
    main()
