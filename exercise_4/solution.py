def solution(m, f):
    m = int(m)
    f = int(f)

    cycles = 0
    while True:
        if m == 1 == f:
            return str(cycles)
        elif m < 1 or f < 1 or m == f:
            break

        if m > f:
            m, new_cycles = subtract_with_multiplier(m, f)
        else:
            f, new_cycles = subtract_with_multiplier(f, m)

        cycles += new_cycles

    return "impossible"


def subtract_with_multiplier(bigger, smaller):
    multiplier = (bigger / smaller) - (smaller == 1)
    return bigger - smaller * multiplier, multiplier
