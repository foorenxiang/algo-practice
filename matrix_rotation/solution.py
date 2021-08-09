"""Rotate an image give by a NxM matrix by 90 degrees. Extra points if done without using an extra buffer"""
import pandas as pd
from matrix_rotation.input import get_input


def main():
    rows = int(get_input())
    input_array = [get_input().split(" ") for _ in range(rows)]
    [
        print(" ".join(rows))
        for rows in pd.DataFrame(input_array, index=None).transpose().values
    ]


if __name__ == "__main__":
    main()
