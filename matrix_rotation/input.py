_sample_input = iter(["3", "1 2 3", "4 5 6", "7 8 9"])


def get_input() -> str:
    try:
        return next(_sample_input)
    except StopIteration:
        return ""
