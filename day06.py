import math
from itertools import starmap

races = """
Time:        42     68     69     85
Distance:   284   1005   1122   1341"""


def get_time_dist(lines: str):
    return list(zip(*(map(int, line.split(":")[1].split()) for line in lines.strip().splitlines())))


# PART 1
def count_solutions(lines):
    for max_t, record_d in get_time_dist(lines):
        all_distances = [(max_t - charging) * charging for charging in range(1, max_t)]
        yield sum(d > record_d for d in all_distances)


# PART 2
def calculate_solutions(max_t, dist):
    # solve quadratic equation: (max_t - x ) * x = dist
    discriminant = math.sqrt(max_t ** 2 - 4 * dist)
    x1, x2 = (max_t - discriminant) / 2, (max_t + discriminant) / 2
    # number of integers N such that a < N < b.
    return math.ceil(x2) - math.floor(x1) - 1


if __name__ == '__main__':
    print(f"Ways to beat past records: {math.prod(count_solutions(races))}")
    print(f"     (same using algebra): {math.prod(starmap(calculate_solutions, get_time_dist(races)))}")
    mega_time, mega_dist = get_time_dist(races.replace(" ", ""))[0]
    print(f"Ways to beat past record in mega race: {calculate_solutions(mega_time, mega_dist)}")
