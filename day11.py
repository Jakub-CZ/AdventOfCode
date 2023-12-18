import re
from itertools import combinations

image = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()
image = """
.........#................................#................#.................#..........................#...........................#.......
.#............#...................................................................................#.........................................
...................................................................................................................#...........#............
.........................#......................................#........#..................................................................
...................#.....................................................................................................#..................
.......................................#..................................................#.......................................#.........
.............#..................#.....................................#............................#.....#.......#........................#.
...........................................#................................................................................................
#...................................#............................................#....................................#.....................
............................................................................................#...............................................
.............................................................................#.........#....................................................
....#....................#...............#.........#...............#....................................................................#...
..................#.........................................................................................................................
.........................................................#................................#......................#.............#............
...................................................................................#...................#....................................
.....................#...............#........#............................#................................................................
..#.....#......#................#......................................................#....................................................
.........................#......................................#............................................#..........#..............#....
..........................................................#.................................................................................
............................................................................................................................................
...................................#.................................#........#............#.......................#........................
.............#.............................#.........................................................#......................................
..................................................#............................................................................#.....#......
.........................#.....................................................................................#............................
.......#......................................#....................................#.........#..........#...................................
....................#.....................................#..............#..................................................................
.............................#......#.......................................................................................................
............................................................................................................................#.....#.........
...........#................................#...............................................................................................
....#............................#................................................................#..........#..............................
..................................................................................................................#.......................#.
................#........#..............#...................#..........................................#....................................
...................................................#........................#...................................................#...........
.........#....................................#..............................................#........................................#.....
..#...........................................................................................................#.............................
...................................................................................................#....................#...................
...........................................#.....................#.......................#.........................................#........
...................#.........#..............................#............#.....#............................................................
..............#..................................#...................................................................#......................
........................#...................................................................................................................
.......................................#...................................................#.....#.....#.................#..................
................................#............#......#...........................................................#...............#...........
........#.........#..................................................#..................................................................#...
..........................#.................................................................................#...............................
..........................................#.....................#........#........#.........................................#...............
.........................................................#....................................#.............................................
....................................#..........#............................................................................................
..#......#..................#...............................................#...........#................#........#.........................
......................................................................#.....................................................................
............................................................................................................................................
..........................................................#.................................#...........................#.............#.....
............................................................................................................................................
......................#.............................................................#............#..........#...............................
#..........#................................................................................................................................
.................#.................#................................#.........................................................#.............
............................................................................................................................................
..........................#.............#...................................#................#.......................#......................
............................................................................................................................................
........................................................#..................................................................................#
..........#.....................#............#...............#...................#..........................................................
#...................#..................................................................................#....................................
............................................................................................................................................
.........................................#.........................#......#......................#....................#.....................
..........................#.................................................................#...................#.................#.........
..................................................#.........................................................................#...............
............................................................................................................................................
.....#......................................................................#........................#..................#...................
................................................................#.....#...................................#.................................
..........#.......................#.....................#......................................................................#......#.....
................#................................#..............................................#...........................................
#.....................#......#.................................................#............................................................
............................................................................................................................................
..............................................................#.......................................................#.................#...
......#.............................#......#.......#...............#.......................#.............#.................#.....#..........
....................#....................................#..................................................................................
...............................#................................................................................#...........................
..........................#.......................................................................#.........................................
.#............................................#..........................#..................................................................
........#.....#...............................................#..........................#............#......#........................#.....
............................................................................................................................................
........................................................#.................................................................#.................
............................................................................................................................................
............#................#.........#.................................................................#.......#................#........#
.................................................#..........................#..............#...........................#....................
...#.............#.......#.................#................................................................................................
............................................................................................................................................
.....................................#....................#.............#.......................#...........................................
.....................#.............................#....................................................#...................................
............#..................................................................................................#............................
.............................................................................#.....#........................................#...............
..................#...........................................#............................................................................#
...............................#........#.............................#.....................................................................
.........#...............#................................#.................................................................................
...#...............................#...................................................................#....................................
...........................................................................#...........#....................................................
................................................................................#...........................................................
.............................#.................#...................#............................................................#..........#
............#...............................................................................#...............................................
.....................#..................#.....................#....................#...............................#......#.................
................#.......................................................................#.........#.........................................
..........................................................................#................................#................................
................................................#................#...............................................................#..........
.........................#......#..............................................#.................................#..........................
..................#..................#...............................#.....................#.........................................#......
............#......................................................................#..................#.....................................
.....#......................................................................................................#...............................
......................#.....#...............#......#..........................................#...........................#...............#.
............................................................#..........................#....................................................
......................................#.........................................................................#...........................
......................................................................#................................................#......#.............
....................#..........................................#...................#.......#................................................
#.........................................#.................................#............................................................#..
...................................................#...................................................#...................#................
............................................................#......#.................................................#......................
.....#.........................#.............................................................#..................#...........................
.........................................................................#........................................................#.........
............................................................................................................................................
.....................................#......................................................................................................
........................#..................................#...............................#................#.......#......#................
.............................#....................#....................................................#...................................#
..................#..........................#.....................................................................................#........
...............................................................#...........#..................#.............................................
.................................#.................................................................#........................................
.......................................................................................#....................................................
..#................................................#........#...............................................................................
...........#...............................#......................................#.............................#.......#...........#.......
........................#...................................................................................................................
......#................................#....................................#..................#.....#......................................
..................#.....................................#..........#........................................................#...............
.............................#.............................................................................................................#
............#.....................................................................................................................#.........
..............................................#.........................#.................#.................................................
.....#.......................................................#..............................................................................
.....................................#...................................................................#..............#...................
...................................................................................................................#........................
...................#......#.....#........#.........................#...............#........................................................
.....................................................................................................................................#......
...........#.......................................#............................................................#..........#................
......................#.................................#..............#.....#...................#.......................................#..
............................#........#...........................#..........................#...............................................
""".strip()
width = image.find("\n")


def get_galaxies_and_gaps():
    _galaxies = []
    row_gaps = []
    cols_with_galaxies = set()
    for r, line in enumerate(image.splitlines()):
        cols = [m.start() for m in re.finditer("#", line)]
        if not cols:
            row_gaps.append(r)
        for c in cols:
            cols_with_galaxies.add(c)
            _galaxies.append((r, c))
    col_gaps = [i for i in range(width) if i not in cols_with_galaxies]
    return _galaxies, row_gaps, col_gaps


def calculate_distance(g1, g2, rows_without_galaxies, cols_without_galaxies, factor):
    row_min, row_max = min(g1[0], g2[0]), max(g1[0], g2[0])
    col_min, col_max = min(g1[1], g2[1]), max(g1[1], g2[1])
    dilated_rows = sum(row_min < r < row_max for r in rows_without_galaxies) * factor
    dilated_cols = sum(col_min < c < col_max for c in cols_without_galaxies) * factor
    return row_max - row_min + col_max - col_min + dilated_rows + dilated_cols


def calculate_all_distances(factor=1):
    galaxies, rows_without_galaxies, cols_without_galaxies = get_galaxies_and_gaps()
    return sum(calculate_distance(g1, g2, rows_without_galaxies, cols_without_galaxies, factor)
               for g1, g2 in combinations(galaxies, 2))


if __name__ == '__main__':
    print(f"Sum of all distances: {calculate_all_distances()}")
    print(f"Sum of all distances in much older universe: {calculate_all_distances(999999)}")
