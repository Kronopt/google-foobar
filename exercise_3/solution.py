def solution(xs):
    final = 1
    highest_negative = -1001
    at_least_one_positive = False
    at_least_one_zero = False

    for i in xs:
        if i != 0:
            final *= i

            if i > 0:
                at_least_one_positive = True

            if 0 > i > highest_negative:
                highest_negative = i
        else:
            at_least_one_zero = True

    if final < 0:
        if at_least_one_positive:
            final /= highest_negative
        elif at_least_one_zero:
            final = "0"

    return str(final)
