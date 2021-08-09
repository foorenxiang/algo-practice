_sample_input = iter(["10", "-1 1 2 -2 3 -3 4 -4 5 -5 6 -6 7 -7 9 -8 9 -9 10 -10"])


def get_input() -> str:
    try:
        return next(_sample_input)
    except StopIteration:
        return ""
