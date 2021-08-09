from itertools import combinations
from max_sum_of_subarray.input import get_input


def main():
    array_length = get_input()
    elements = [int(num_str) for num_str in get_input().split(" ")]
    sums = sum(
        [
            sum(combo)
            for combination_length in range(1, int(array_length) + 1)
            for combo in combinations(elements, combination_length)
        ]
    )
    print(sums)


main()
